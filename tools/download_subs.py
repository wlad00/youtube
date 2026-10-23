"""Пакетное скачивание оригинальных субтитров по списку роликов (локально, без куки и входа в аккаунт).

Запуск:
    python tools/download_subs.py <список.tsv> <рабочая папка репо> [--log <файл>] [--author <имя>] [--no-git]

Список — TSV: Video ID <TAB> папка ролика относительно корня репо (например
bible/ivan-pendlishak/2025-11-21-totalne-rabstvo). Пустые строки, строки с # и заголовок пропускаются.
Папка с «/» на конце (например margulan-seysembaev/self-realization/) — имя ролика скрипт строит сам
из тех же метаданных: <ГГГГ-ММ-ДД>-<транслит оригинального названия> (х → kh, щ → shch, ё → e;
для языка uk — г → h, и → y; части названия через «|», равные author или каналу, отбрасываются;
слаг до 100 знаков), занятое имя — суффикс -2, -3. Ролик, уже записанный в этой папке, берётся по video_id.

По одному ролику: --list-subs с метаданными → выбор оригинальной дорожки (правила AGENTS.md,
«Скачивание субтитров») → скачивание → очистка через tools/materialize_sections.py --transcript →
README.md → удаление сырого SRT. В папке ролика остаются только README.md и transcript.cleaned.md.
Пауза 2 с между роликами. Каждые 20 готовых роликов — git add этих папок, коммит, push в текущую ветку.
Журнал: строка на ролик (время | ID | ok/ошибка | N из M), в конце итог цифрами.
Затык ролика — в журнал и дальше. 429 или «not a bot» 2 раза подряд — коммит готового и стоп.
Author в README: --author, иначе общий author соседних README коллекции, иначе пусто.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

YTDLP = Path(os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe"))
FFMPEG = Path(os.path.expandvars(
    r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\ffmpeg-N-125875-g5d4d3bdc61-win64-gpl\bin"))
CLEANER = Path(__file__).resolve().parent / "materialize_sections.py"
YT = "https://www.youtube.com/watch?v="
PAUSE = 2
BATCH = 20
BLOCK_MARKS = ("HTTP Error 429", "Too Many Requests", "Sign in to confirm", "not a bot")
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
CODE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9-]*)\s{2,}\S")
VID_RE = re.compile(r'^video_id:\s*"([A-Za-z0-9_-]{11})"', re.M)
AUTHOR_RE = re.compile(r'^author:\s*"([^"]*)"', re.M)


class Blocked(Exception):
    pass


class Stuck(Exception):
    pass


def run(args, cwd=None):
    p = subprocess.run([str(a) for a in args], cwd=str(cwd) if cwd else None, capture_output=True)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def clip(s, n=200):
    return " ".join(s.split())[-n:]


def check_block(text):
    if any(k in text for k in BLOCK_MARKS):
        raise Blocked(clip(text))


def yaml_str(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def read_list(path):
    items = []
    for ln in path.read_text(encoding="utf-8-sig").splitlines():
        parts = [p.strip() for p in ln.split("\t")]
        if len(parts) < 2 or not ID_RE.match(parts[0]):
            continue
        p = parts[1].replace("\\", "/")
        items.append((parts[0], p.strip("/") + ("/" if p.endswith("/") else "")))
    return items


TR = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i",
    "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch", "ъ": "", "ы": "y", "ь": "",
    "э": "e", "ю": "yu", "я": "ya",
    "ә": "a", "ғ": "gh", "қ": "q", "ң": "n", "ө": "o", "ұ": "u", "ү": "u", "һ": "h", "і": "i",
    "є": "ie", "ї": "i", "ґ": "g",
}
TR_UK = {**TR, "г": "h", "и": "y", "й": "i"}
SLUG_MAX = 100


def slugify(title, lang, drop):
    parts = [p for p in re.split(r"\s*\|\s*", title) if p.strip().casefold() not in drop]
    tr = TR_UK if lang == "uk" else TR
    out = []
    for ch in " ".join(parts).lower():
        if ch in tr:
            out.append(tr[ch])
        elif ch in "'’ʼ`":
            continue
        elif ch.isascii() and ch.isalnum():
            out.append(ch)
        else:
            out.append("-")
    s = re.sub(r"-+", "-", "".join(out)).strip("-")
    if len(s) > SLUG_MAX:
        cut = s[:SLUG_MAX + 1]
        s = cut[:cut.rfind("-")] if "-" in cut else s[:SLUG_MAX]
    return s.strip("-") or "video"


def auto_name(parent_dir, meta, lang, author):
    u = meta["date"]
    if not re.fullmatch(r"\d{8}", u):
        raise Stuck(f"нет даты публикации для имени папки ({u or '—'})")
    drop = {s.strip().casefold() for s in (author or "", meta["channel"]) if s and s.strip()}
    name = base_name = f"{u[:4]}-{u[4:6]}-{u[6:]}-{slugify(meta['title'], lang, drop)}"
    n = 2
    while (parent_dir / name).exists():
        name, n = f"{base_name}-{n}", n + 1
    return name


def repo_owners(repo):
    """Video ID → папки, где он уже записан (README.md и строки INDEX.md)."""
    owners = {}
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d != ".git"]
        if "README.md" in files and root != str(repo):
            m = VID_RE.search((Path(root) / "README.md").read_text(encoding="utf-8", errors="replace"))
            if m:
                owners.setdefault(m.group(1), set()).add(Path(root).relative_to(repo).as_posix())
    index = repo / "INDEX.md"
    if index.exists():
        for ln in index.read_text(encoding="utf-8", errors="replace").splitlines():
            link = re.search(r"\]\(([^)]+)/README\.md\)", ln)
            for vid in re.findall(r"v=([A-Za-z0-9_-]{11})", ln):
                if link:
                    owners.setdefault(vid, set()).add(link.group(1))
    return owners


def collection_author(coll_dir, cache):
    if coll_dir not in cache:
        names = set()
        if coll_dir.is_dir():
            for d in coll_dir.iterdir():
                rd = d / "README.md"
                if rd.is_file():
                    m = AUTHOR_RE.search(rd.read_text(encoding="utf-8", errors="replace"))
                    if m and m.group(1).strip():
                        names.add(m.group(1).strip())
        cache[coll_dir] = names.pop() if len(names) == 1 else ""
    return cache[coll_dir]


def list_subs(vid):
    rc, out, err = run([YTDLP, "--no-quiet", "--no-warnings", "--encoding", "utf-8", "--list-subs",
                        "--print", "META\t%(language)s\t%(upload_date)s\t%(channel)s\t%(title)s", YT + vid])
    check_block(out + err)
    auto, manual, meta, section = [], [], None, None
    for ln in out.splitlines():
        if ln.startswith("[info] Available automatic captions"):
            section = auto
        elif ln.startswith("[info] Available subtitles"):
            section = manual
        elif ln.startswith("META\t"):
            p = ln.split("\t", 4)
            meta = {"language": p[1], "date": p[2], "channel": p[3], "title": p[4]}
        elif ln.startswith("[") or " has no " in ln:
            section = None
        elif section is not None and not ln.startswith("Language "):
            m = CODE_RE.match(ln)
            if m:
                section.append(m.group(1))
    if meta is None:
        raise Stuck("нет метаданных: " + clip(err or out))
    return auto, manual, meta


def base(code):
    return code.split("-")[0].lower()


def choose_track(auto, manual, meta_lang):
    """Код дорожки для --sub-langs и язык для README."""
    ml = "" if meta_lang in ("", "NA", "None") else meta_lang
    origs = [c for c in auto if c.endswith("-orig")]
    if len(origs) == 1:
        return origs[0], base(origs[0])
    if len(origs) > 1:
        hit = [c for c in origs if ml and base(c) == base(ml)]
        if len(hit) == 1:
            return hit[0], base(hit[0])
        raise Stuck(f"несколько -orig {origs}, язык в метаданных: {ml or '—'}")
    hit = [c for c in manual if ml and base(c) == base(ml)]
    if hit:
        code = ml if ml in hit else hit[0]
        return code, base(code)
    raise Stuck(f"нет -orig и ручной дорожки языка оригинала ({ml or '—'}); ручные: {manual or '—'}")


def download(vid, folder, code, lang):
    rc, out, err = run([YTDLP, "--no-warnings", "--skip-download", "--write-auto-subs", "--write-subs",
                        "--sub-langs", code, "--convert-subs", "srt", "--no-progress",
                        "--ffmpeg-location", FFMPEG, "--sleep-subtitles", "2",
                        "-o", folder / "subtitles.%(ext)s", YT + vid])
    check_block(out + err)
    srts = sorted(folder.glob("subtitles.*.srt"))
    if len(srts) != 1:
        raise Stuck(f"SRT не получен ({len(srts)} файлов): " + clip(out + err))
    target = folder / f"subtitles.{lang}.srt"
    if srts[0] != target:
        srts[0].rename(target)


def clean(folder):
    tr = folder / "transcript.cleaned.md"
    rc, out, err = run([sys.executable, CLEANER, folder, "--transcript", "--out", tr])
    if rc != 0 or not tr.is_file() or not tr.read_text(encoding="utf-8").lstrip().startswith("[00:"):
        tr.unlink(missing_ok=True)
        raise Stuck("очистка не прошла: " + clip(out + err))
    return len(tr.read_text(encoding="utf-8"))


def write_readme(folder, rel, vid, meta, lang, author):
    rd = folder / "README.md"
    if rd.is_file():
        text = rd.read_text(encoding="utf-8")
        text = re.sub(r'^language:.*$', f'language: "{lang}"', text, count=1, flags=re.M)
        if meta["channel"]:
            text = re.sub(r'^channel:\s*""\s*$', f'channel: "{yaml_str(meta["channel"])}"', text, count=1, flags=re.M)
        rd.write_bytes(text.encode("utf-8"))
        return
    m = re.match(r"(\d{4}-\d{2}(?:-\d{2})?)-", folder.name)
    u = meta["date"]
    date = m.group(1) if m else (f"{u[:4]}-{u[4:6]}-{u[6:]}" if re.fullmatch(r"\d{8}", u) else "")
    coll = rel.rsplit("/", 1)[0] if "/" in rel else ""
    rd.write_bytes((
        "---\n"
        f'title: "{yaml_str(meta["title"])}"\n'
        f'youtube: "{YT}{vid}"\n'
        f'video_id: "{vid}"\n'
        f'date: "{date}"\n'
        f'collection: "{coll}"\n'
        f'author: "{yaml_str(author)}"\n'
        f'channel: "{yaml_str(meta["channel"])}"\n'
        f'language: "{lang}"\n'
        "tags: []\n"
        "---\n\n"
        f"# {meta['title']}\n"
    ).encode("utf-8"))


def one(repo, vid, rel, owners, args, cache):
    """Возвращает (статус, пояснение, папка ролика относительно репо)."""
    subs = None
    if rel.endswith("/"):
        parent = rel.rstrip("/")
        mine = sorted(o for o in owners.get(vid, ()) if o.rsplit("/", 1)[0] == parent)
        if mine:
            rel = mine[0]
        else:
            subs = list_subs(vid)
            code, lang = choose_track(subs[0], subs[1], subs[2]["language"])
            author = args.author if args.author is not None else collection_author(repo / parent, cache)
            rel = f"{parent}/{auto_name(repo / parent, subs[2], lang, author)}"
    folder = repo / rel
    if (folder / "transcript.cleaned.md").exists():
        return "skip", "transcript.cleaned.md уже есть", rel
    other = owners.get(vid, set()) - {rel}
    if other:
        raise Stuck("дубль: Video ID уже в " + ", ".join(sorted(other)))
    rd = folder / "README.md"
    if rd.is_file():
        m = VID_RE.search(rd.read_text(encoding="utf-8", errors="replace"))
        if m and m.group(1) != vid:
            raise Stuck(f"в README папки другой video_id {m.group(1)}")
    auto, manual, meta = subs or list_subs(vid)
    code, lang = choose_track(auto, manual, meta["language"])
    created = not folder.exists()
    folder.mkdir(parents=True, exist_ok=True)
    try:
        download(vid, folder, code, lang)
        n = clean(folder)
        author = args.author if args.author is not None else collection_author(folder.parent, cache)
        write_readme(folder, rel, vid, meta, lang, author)
    except BaseException:
        if created:
            shutil.rmtree(folder, ignore_errors=True)
        raise
    finally:
        for f in folder.glob("subtitles.*"):
            f.unlink()
    owners.setdefault(vid, set()).add(rel)
    return "ok", f"{lang} ({code}), {n} знаков, {rel}", rel


def git(repo, *a):
    return run(["git", *a], cwd=repo)


def commit_push(repo, ready, log):
    if not ready:
        return True
    dates = sorted(Path(r).name[:10] for _, r in ready)
    colls = sorted({r.rsplit("/", 1)[0] for _, r in ready if "/" in r})
    msg = f"{', '.join(colls) or 'ролики'}: субтитры {len(ready)} роликов {dates[0]} … {dates[-1]} (без выжимок)"
    paths = [r for _, r in ready]
    rc, out, err = git(repo, "add", "--", *paths)
    if rc == 0:
        rc, out, err = git(repo, "commit", "-m", msg, "--", *paths)
    if rc != 0:
        log(f"git: коммит не прошёл: {clip(out + err)}")
        return False
    branch = git(repo, "rev-parse", "--abbrev-ref", "HEAD")[1].strip()
    rc, out, err = git(repo, "push", "origin", "HEAD")
    if rc != 0:
        git(repo, "pull", "--rebase", "--autostash", "origin", branch)
        rc, out, err = git(repo, "push", "origin", "HEAD")
    sha = git(repo, "rev-parse", "--short", "HEAD")[1].strip()
    if rc != 0:
        log(f"git: коммит {sha} есть, push в {branch} не прошёл: {clip(out + err)}")
        ready.clear()
        return False
    log(f"git: коммит {sha} ({len(ready)} роликов) и push в {branch}")
    ready.clear()
    return True


def main():
    ap = argparse.ArgumentParser(description="Пакетное скачивание оригинальных субтитров по списку")
    ap.add_argument("list", type=Path, help="TSV: Video ID <TAB> папка ролика относительно корня репо")
    ap.add_argument("repo", type=Path, help="рабочая папка репозитория")
    ap.add_argument("--log", type=Path, help="журнал (по умолчанию <список>.log)")
    ap.add_argument("--author", help="author для новых README (по умолчанию — общий у соседних README)")
    ap.add_argument("--no-git", action="store_true", help="без git add/commit/push (для проверки)")
    args = ap.parse_args()
    repo = args.repo.resolve()
    log_path = args.log or args.list.with_suffix(".log")
    items = read_list(args.list)
    total = len(items)

    def log(line):
        s = f"{datetime.now():%Y-%m-%d %H:%M:%S} | {line}"
        print(s, flush=True)
        with log_path.open("a", encoding="utf-8") as f:
            f.write(s + "\n")

    log(f"старт: {total} роликов из {args.list}, репо {repo}" + (" (без git)" if args.no_git else ""))
    owners = repo_owners(repo)
    cache, ready = {}, []
    cnt = {"ok": 0, "skip": 0, "err": 0, "block": 0}
    streak, stop, done, t0 = 0, "", 0, time.time()
    try:
        for i, (vid, rel) in enumerate(items, 1):
            if i > 1:
                time.sleep(PAUSE)
            try:
                status, note, rel = one(repo, vid, rel, owners, args, cache)
                streak = 0
            except Blocked as e:
                status, note = "block", f"блокировка YouTube: {e}"
                streak += 1
            except Stuck as e:
                status, note = "err", str(e)
                streak = 0
            except Exception as e:  # один ролик не роняет пакет
                status, note = "err", f"{type(e).__name__}: {e}"
                streak = 0
            done = i
            cnt[status] += 1
            word = {"ok": "ok", "skip": "пропуск", "err": "ошибка", "block": "ошибка"}[status]
            log(f"{vid} | {word}: {note} | {i} из {total}")
            if status == "ok":
                ready.append((vid, rel))
                if not args.no_git and len(ready) >= BATCH and not commit_push(repo, ready, log):
                    stop = "git"
                    break
            if streak >= 2:
                stop = "429 / «not a bot» 2 раза подряд"
                break
    except KeyboardInterrupt:
        stop = "прервано вручную"
    if not args.no_git and stop != "git":
        commit_push(repo, ready, log)
    log(f"ИТОГ: всего {total}, пройдено {done}, ok {cnt['ok']}, пропущено (транскрипт уже был) {cnt['skip']}, "
        f"ошибок {cnt['err']}, блокировок {cnt['block']}, не закоммичено {0 if args.no_git else len(ready)}, "
        f"время {round(time.time() - t0)} с" + (f"; СТОП: {stop}" if stop else ""))
    return 1 if stop else 0


if __name__ == "__main__":
    sys.exit(main())
