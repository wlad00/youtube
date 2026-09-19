#!/usr/bin/env python3
"""Materialize semantic video sections and cleaned transcript derivatives.

The primary semantic map is sections.yaml: the agent chooses only boundaries
and short titles. For older videos without YAML, the managed README.md block is
still supported.

Section files use the same rolling-caption deduplication as --transcript.
With --transcript the script writes a timestamped cleaned reading copy.
With --chunks it can still create optional deterministic fallback chunks.
With --partial it materializes a confirmed prefix whose last section ends at an explicit timecode.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path

SECTION_BLOCK_RE = re.compile(
    r"<!-- sections:begin -->(.*?)<!-- sections:end -->",
    re.DOTALL,
)
HEADING_RE = re.compile(r"^###\s+(\d+)\.\s+(.+?)\s*$")
INTERVAL_RE = re.compile(
    r"^\*\*Интервал:\*\*\s+`([^`]+?)\s+-->\s+([^`]+?)`\s*$"
)
TIMECODE_RE = re.compile(
    r"^(?:(\d+):)?(\d{1,2}):(\d{2})(?:[,.](\d{1,3}))?$"
)
SRT_TIME_RE = re.compile(
    r"^\s*((?:\d+:)?\d{1,2}:\d{2}[,.]\d{3})\s+-->\s+"
    r"((?:\d+:)?\d{1,2}:\d{2}[,.]\d{3})"
)
DEFAULT_WINDOW_SECONDS = 30
DEFAULT_CHUNK_CHARS = 6000


@dataclass(frozen=True)
class Section:
    number: int
    title: str
    start_ms: int
    end_ms: int | None  # None means END
    enrichment: str


@dataclass(frozen=True)
class Cue:
    start_ms: int
    end_ms: int
    text: str


@dataclass(frozen=True)
class TranscriptBlock:
    start_ms: int
    text: str

    def render(self) -> str:
        return f"[{format_timecode(self.start_ms)}] {self.text}"


@dataclass(frozen=True)
class TranscriptChunk:
    number: int
    start_ms: int
    end_ms: int
    body: str


def parse_timecode(value: str) -> int:
    value = value.strip()
    match = TIMECODE_RE.fullmatch(value)
    if not match:
        raise ValueError(f"Некорректный таймкод: {value!r}")
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    millis_text = match.group(4) or "0"
    millis = int(millis_text.ljust(3, "0"))
    if minutes >= 60 or seconds >= 60:
        raise ValueError(f"Некорректный таймкод: {value!r}")
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + millis


def format_timecode(ms: int) -> str:
    total_seconds = ms // 1000
    hours, rem = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"




def parse_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError) as exc:
            raise ValueError(f"Некорректная строка YAML: {value!r}") from exc
        if not isinstance(parsed, str):
            raise ValueError(f"Ожидалась строка YAML: {value!r}")
        return parsed
    return value


def parse_sections_yaml(raw: str) -> list[Section]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_sections = False

    for line_number, raw_line in enumerate(raw.splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line == "sections:":
            if in_sections:
                raise ValueError("В sections.yaml блок sections: указан больше одного раза")
            in_sections = True
            continue
        if not in_sections:
            raise ValueError("sections.yaml должен начинаться с блока sections:")

        if line.startswith("- "):
            if current is not None:
                entries.append(current)
            current = {}
            line = line[2:].strip()
            if not line:
                continue
        elif current is None:
            raise ValueError(
                f"Некорректная запись sections.yaml в строке {line_number}: {raw_line!r}"
            )

        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(
                f"Некорректная запись sections.yaml в строке {line_number}: {raw_line!r}"
            )
        key = key.strip()
        if key not in {"title", "start", "end"}:
            raise ValueError(f"Неизвестное поле sections.yaml: {key!r}")
        if key in current:
            raise ValueError(f"Поле {key!r} повторяется в одном разделе")
        current[key] = parse_yaml_scalar(value)

    if current is not None:
        entries.append(current)
    if not in_sections or not entries:
        raise ValueError("В sections.yaml не найдено ни одного раздела")

    sections: list[Section] = []
    for number, entry in enumerate(entries, 1):
        missing = {"title", "start", "end"} - entry.keys()
        if missing:
            raise ValueError(
                f"У раздела {number} не хватает полей: {', '.join(sorted(missing))}"
            )
        title = entry["title"].strip()
        if not title:
            raise ValueError(f"У раздела {number} пустое название")
        start_ms = parse_timecode(entry["start"])
        end_text = entry["end"].strip()
        end_ms = None if end_text.upper() == "END" else parse_timecode(end_text)
        sections.append(Section(number, title, start_ms, end_ms, ""))

    if sections[0].start_ms != 0:
        raise ValueError("Первый раздел должен начинаться с 00:00:00")
    for previous, current_section in zip(sections, sections[1:]):
        if previous.end_ms is None:
            raise ValueError("END допустим только у последнего раздела")
        if previous.start_ms >= previous.end_ms:
            raise ValueError(f"Пустой или обратный интервал у раздела {previous.number}")
        if previous.end_ms != current_section.start_ms:
            raise ValueError(
                "Разделы должны покрывать ролик непрерывно: "
                f"конец {previous.number} ({format_timecode(previous.end_ms)}) "
                f"!= начало {current_section.number} "
                f"({format_timecode(current_section.start_ms)})"
            )
    if sections[-1].end_ms is not None and sections[-1].start_ms >= sections[-1].end_ms:
        raise ValueError(f"Пустой или обратный интервал у раздела {sections[-1].number}")
    return sections


def render_sections_block(sections: list[Section]) -> str:
    lines = ["<!-- sections:begin -->", ""]
    for section in sections:
        end_text = "END" if section.end_ms is None else format_timecode(section.end_ms)
        lines.extend(
            [
                f"### {section.number}. {section.title}",
                f"**Интервал:** `{format_timecode(section.start_ms)} --> {end_text}`",
                f"**Файл:** [sections/{section.number:02d}.md](sections/{section.number:02d}.md)",
                "",
            ]
        )
    lines.append("<!-- sections:end -->")
    return "\n".join(lines)


def sync_readme_sections(readme_path: Path, sections: list[Section]) -> None:
    readme = readme_path.read_text(encoding="utf-8")
    rendered = render_sections_block(sections)
    if SECTION_BLOCK_RE.search(readme):
        updated = SECTION_BLOCK_RE.sub(rendered, readme, count=1)
    else:
        updated = readme.rstrip() + "\n\n## Разделы\n\n" + rendered + "\n"
    readme_path.write_text(updated, encoding="utf-8")


def parse_sections(readme: str) -> list[Section]:
    block_match = SECTION_BLOCK_RE.search(readme)
    if not block_match:
        raise ValueError(
            "В README.md нет блока <!-- sections:begin --> ... <!-- sections:end -->"
        )

    lines = block_match.group(1).splitlines()
    heading_positions: list[tuple[int, re.Match[str]]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            heading_positions.append((index, match))

    if not heading_positions:
        raise ValueError("В блоке разделов не найдено ни одного раздела")

    sections: list[Section] = []
    for pos, (start_index, heading) in enumerate(heading_positions):
        stop_index = (
            heading_positions[pos + 1][0]
            if pos + 1 < len(heading_positions)
            else len(lines)
        )
        chunk = lines[start_index + 1 : stop_index]

        interval_index = None
        interval_match = None
        for index, line in enumerate(chunk):
            match = INTERVAL_RE.match(line)
            if match:
                interval_index = index
                interval_match = match
                break
        if interval_index is None or interval_match is None:
            raise ValueError(
                f"У раздела {heading.group(1)} нет строки "
                "**Интервал:** `HH:MM:SS --> HH:MM:SS|END`"
            )

        enrichment_lines = [
            line
            for line in chunk[interval_index + 1 :]
            if not line.startswith("**Файл:**")
        ]
        enrichment = "\n".join(enrichment_lines).strip()

        start_text = interval_match.group(1).strip()
        end_text = interval_match.group(2).strip()
        start_ms = parse_timecode(start_text)
        end_ms = None if end_text.upper() == "END" else parse_timecode(end_text)

        sections.append(
            Section(
                number=int(heading.group(1)),
                title=heading.group(2).strip(),
                start_ms=start_ms,
                end_ms=end_ms,
                enrichment=enrichment,
            )
        )

    expected_numbers = list(range(1, len(sections) + 1))
    actual_numbers = [section.number for section in sections]
    if actual_numbers != expected_numbers:
        raise ValueError(
            f"Разделы должны быть пронумерованы подряд с 1: {actual_numbers}"
        )

    if sections[0].start_ms != 0:
        raise ValueError("Первый раздел должен начинаться с 00:00:00")

    for previous, current in zip(sections, sections[1:]):
        if previous.end_ms is None:
            raise ValueError("END допустим только у последнего раздела")
        if previous.end_ms != current.start_ms:
            raise ValueError(
                "Разделы должны покрывать ролик непрерывно: "
                f"конец {previous.number} ({format_timecode(previous.end_ms)}) "
                f"!= начало {current.number} ({format_timecode(current.start_ms)})"
            )
        if previous.start_ms >= previous.end_ms:
            raise ValueError(f"Пустой или обратный интервал у раздела {previous.number}")

    if sections[-1].end_ms is not None:
        if sections[-1].start_ms >= sections[-1].end_ms:
            raise ValueError(f"Пустой или обратный интервал у раздела {sections[-1].number}")

    return sections


def parse_srt(path: Path) -> list[Cue]:
    raw = path.read_text(encoding="utf-8-sig")
    blocks = re.split(r"\r?\n\s*\r?\n", raw.strip())
    cues: list[Cue] = []

    for block in blocks:
        lines = block.splitlines()
        if not lines:
            continue

        time_index = None
        time_match = None
        for index, line in enumerate(lines[:3]):
            match = SRT_TIME_RE.match(line)
            if match:
                time_index = index
                time_match = match
                break

        if time_index is None or time_match is None:
            continue

        start_ms = parse_timecode(time_match.group(1))
        end_ms = parse_timecode(time_match.group(2))
        text_lines = [line.rstrip() for line in lines[time_index + 1 :]]
        text = "\n".join(text_lines).strip()
        if text:
            cues.append(Cue(start_ms, end_ms, text))

    if not cues:
        raise ValueError(f"Не удалось прочитать SRT: {path}")
    return cues


def find_subtitles(video_dir: Path) -> Path:
    candidates = sorted(video_dir.glob("subtitles.*.srt"))
    if len(candidates) != 1:
        raise ValueError(
            f"Ожидался ровно один subtitles.*.srt в {video_dir}, найдено {len(candidates)}"
        )
    return candidates[0]


def section_text(cues: list[Cue], start_ms: int, end_ms: int) -> str:
    # Assign every cue to exactly one section by its start time.
    # The original SRT text, including any YouTube rolling-caption repetitions,
    # is preserved as-is.
    selected = [
        cue.text
        for cue in cues
        if start_ms <= cue.start_ms < end_ms
    ]
    return "\n\n".join(selected).strip()



def section_text_cleaned(
    cues: list[Cue],
    start_ms: int,
    end_ms: int,
    window_ms: int = DEFAULT_WINDOW_SECONDS * 1000,
) -> str:
    selected = [
        (line_start_ms, line)
        for line_start_ms, line in dedupe_cues(cues)
        if start_ms <= line_start_ms < end_ms
    ]
    if not selected:
        return ""

    grouped: list[tuple[int, list[str]]] = []
    for line_start_ms, line in selected:
        if grouped and line_start_ms - grouped[-1][0] < window_ms:
            grouped[-1][1].append(line)
        else:
            grouped.append((line_start_ms, [line]))

    return "\n\n".join(
        f"[{format_timecode(block_start_ms)}] {' '.join(lines)}"
        for block_start_ms, lines in grouped
    )


def dedupe_cues(cues: list[Cue]) -> list[tuple[int, str]]:
    # YouTube rolling captions repeat each line across consecutive cues:
    # [A, B], [B, C], [C, D]. Drop the leading lines that already ended the
    # emitted text, keeping the first timestamp at which each line appeared.
    emitted: list[str] = []
    result: list[tuple[int, str]] = []

    for cue in cues:
        lines = [line.strip() for line in cue.text.splitlines() if line.strip()]
        if not lines:
            continue

        overlap = 0
        for size in range(min(len(lines), len(emitted)), 0, -1):
            if emitted[-size:] == lines[:size]:
                overlap = size
                break

        for line in lines[overlap:]:
            emitted.append(line)
            result.append((cue.start_ms, line))

    return result


def build_transcript_blocks(cues: list[Cue], window_ms: int) -> list[TranscriptBlock]:
    if window_ms <= 0:
        raise ValueError("Окно таймкодов должно быть больше нуля")

    grouped: list[tuple[int, list[str]]] = []

    for start_ms, line in dedupe_cues(cues):
        if grouped and start_ms - grouped[-1][0] < window_ms:
            grouped[-1][1].append(line)
        else:
            grouped.append((start_ms, [line]))

    return [
        TranscriptBlock(start_ms, " ".join(lines))
        for start_ms, lines in grouped
    ]


def render_transcript(cues: list[Cue], window_ms: int) -> str:
    return "\n\n".join(
        block.render() for block in build_transcript_blocks(cues, window_ms)
    )


def chunk_transcript(
    blocks: list[TranscriptBlock], video_end_ms: int, max_chars: int
) -> list[TranscriptChunk]:
    if max_chars <= 0:
        raise ValueError("Лимит чанка должен быть больше нуля")
    if not blocks:
        raise ValueError("Очищенная расшифровка пуста")

    block_texts = [block.render() for block in blocks]
    for block_text in block_texts:
        if len(block_text) > max_chars:
            raise ValueError(
                "Один временной блок длиннее лимита чанка. "
                "Уменьшите --window или увеличьте --max-chars."
            )

    groups: list[tuple[int, list[str]]] = []
    current_start = blocks[0].start_ms
    current: list[str] = []
    current_length = 0

    for block, block_text in zip(blocks, block_texts):
        separator_length = 2 if current else 0
        if current and current_length + separator_length + len(block_text) > max_chars:
            groups.append((current_start, current))
            current_start = block.start_ms
            current = []
            current_length = 0
            separator_length = 0

        current.append(block_text)
        current_length += separator_length + len(block_text)

    groups.append((current_start, current))

    chunks: list[TranscriptChunk] = []
    for index, (content_start_ms, body_parts) in enumerate(groups):
        start_ms = 0 if index == 0 else content_start_ms
        end_ms = groups[index + 1][0] if index + 1 < len(groups) else video_end_ms
        chunks.append(
            TranscriptChunk(
                number=index + 1,
                start_ms=start_ms,
                end_ms=end_ms,
                body="\n\n".join(body_parts),
            )
        )

    return chunks


def materialize_chunks(
    video_dir: Path,
    max_chars: int = DEFAULT_CHUNK_CHARS,
    window_ms: int = DEFAULT_WINDOW_SECONDS * 1000,
) -> list[Path]:
    subtitles_path = find_subtitles(video_dir)
    cues = parse_srt(subtitles_path)
    blocks = build_transcript_blocks(cues, window_ms)
    video_end_ms = max(cue.end_ms for cue in cues)
    chunks = chunk_transcript(blocks, video_end_ms, max_chars)

    chunks_dir = video_dir / "chunks"
    chunks_dir.mkdir(exist_ok=True)
    for stale in chunks_dir.glob("*.md"):
        if stale.stem.isdigit():
            stale.unlink()

    width = max(2, len(str(len(chunks))))
    written: list[Path] = []
    rows: list[str] = []
    for chunk in chunks:
        filename = f"{chunk.number:0{width}d}.md"
        out = chunks_dir / filename
        content = (
            f"# Автоматический чанк {chunk.number}\n\n"
            f"Источник: [`../{subtitles_path.name}`](../{subtitles_path.name})  \n"
            f"Интервал: `{format_timecode(chunk.start_ms)} --> "
            f"{format_timecode(chunk.end_ms)}`  \n"
            f"Очищенный текст: `{len(chunk.body)}` символов\n\n"
            f"---\n\n{chunk.body}\n"
        )
        out.write_text(content, encoding="utf-8")
        written.append(out)
        rows.append(
            f"| {chunk.number} | "
            f"`{format_timecode(chunk.start_ms)} --> {format_timecode(chunk.end_ms)}` | "
            f"{len(chunk.body)} | [{filename}]({filename}) |"
        )

    index = chunks_dir / "README.md"
    index_content = (
        "# Автоматические чанки\n\n"
        f"Источник: [`../{subtitles_path.name}`](../{subtitles_path.name})  \n"
        f"Покрытие: `{format_timecode(chunks[0].start_ms)} --> "
        f"{format_timecode(chunks[-1].end_ms)}`  \n"
        f"Количество: **{len(chunks)}**  \n"
        f"Лимит очищенного текста в чанке: **{max_chars} символов**\n\n"
        "| # | Интервал | Символы | Файл |\n"
        "|---:|---|---:|---|\n"
        + "\n".join(rows)
        + "\n"
    )
    index.write_text(index_content, encoding="utf-8")
    return [index, *written]


def materialize(video_dir: Path, partial: bool = False) -> list[Path]:
    readme_path = video_dir / "README.md"
    if not readme_path.is_file():
        raise ValueError(f"Не найден README.md: {readme_path}")

    subtitles_path = find_subtitles(video_dir)
    readme = readme_path.read_text(encoding="utf-8")
    sections_yaml_path = video_dir / "sections.yaml"
    sections_from_yaml = sections_yaml_path.is_file()
    sections = (
        parse_sections_yaml(sections_yaml_path.read_text(encoding="utf-8"))
        if sections_from_yaml
        else parse_sections(readme)
    )
    cues = parse_srt(subtitles_path)

    video_end_ms = max(cue.end_ms for cue in cues)
    last = sections[-1]
    if partial and last.end_ms is None:
        raise ValueError(
            "В режиме --partial последний подтверждённый раздел должен "
            "заканчиваться явным таймкодом, не END."
        )
    effective_last_end = video_end_ms if last.end_ms is None else last.end_ms
    if not partial and effective_last_end < max(cue.start_ms for cue in cues):
        raise ValueError(
            "Последний раздел заканчивается раньше субтитров. "
            "Используйте END или запустите с --partial для подтверждённого префикса."
        )

    sections_dir = video_dir / "sections"
    sections_dir.mkdir(exist_ok=True)

    # sections/ is generated-only. Remove stale generated numeric files.
    for stale in sections_dir.glob("[0-9][0-9].md"):
        stale.unlink()

    source_name = (
        "transcript.cleaned.md"
        if (video_dir / "transcript.cleaned.md").is_file()
        else subtitles_path.name
    )

    written: list[Path] = []
    for section in sections:
        end_ms = video_end_ms if section.end_ms is None else section.end_ms
        body = section_text_cleaned(cues, section.start_ms, end_ms)
        if not body:
            raise ValueError(f"Раздел {section.number} не содержит субтитров")

        out = sections_dir / f"{section.number:02d}.md"
        enrichment = (
            f"{section.enrichment}\n\n---\n\n"
            if section.enrichment
            else ""
        )
        content = (
            f"# {section.number}. {section.title}\n\n"
            f"Источник: `../{source_name}`  \n"
            f"Интервал: `{format_timecode(section.start_ms)} --> "
            f"{format_timecode(end_ms)}`\n\n"
            f"{enrichment}"
            f"{body}\n"
        )
        out.write_text(content, encoding="utf-8")
        written.append(out)

    if sections_from_yaml:
        sync_readme_sections(readme_path, sections)

    return written


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Создать sections/*.md по sections.yaml (legacy: карта в README.md)."
    )
    parser.add_argument(
        "video_dir",
        type=Path,
        help="Папка ролика, содержащая README.md и subtitles.*.srt",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--transcript",
        action="store_true",
        help="Не создавать разделы, а выдать очищенную расшифровку для чтения",
    )
    mode.add_argument(
        "--chunks",
        action="store_true",
        help="Создать автоматические chunks/*.md из очищенной расшифровки",
    )
    parser.add_argument(
        "--partial",
        action="store_true",
        help="Материализовать подтверждённый префикс sections.yaml, не требуя покрытия всего ролика",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Файл для --transcript (по умолчанию stdout; в Windows-консоли "
        "кириллица в stdout может испортиться, лучше указывать файл)",
    )
    parser.add_argument(
        "--window",
        type=int,
        default=DEFAULT_WINDOW_SECONDS,
        help="Секунд текста под одной меткой времени (по умолчанию 30)",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=DEFAULT_CHUNK_CHARS,
        help="Максимум символов очищенного текста в одном чанке (по умолчанию 6000)",
    )
    args = parser.parse_args()

    video_dir = args.video_dir.resolve()

    if args.partial and (args.transcript or args.chunks):
        print("Ошибка: --partial нельзя сочетать с --transcript или --chunks", file=sys.stderr)
        return 1

    if args.transcript:
        try:
            cues = parse_srt(find_subtitles(video_dir))
            transcript = render_transcript(cues, args.window * 1000)
        except (OSError, ValueError) as exc:
            print(f"Ошибка: {exc}", file=sys.stderr)
            return 1

        if args.out:
            args.out.write_text(transcript + "\n", encoding="utf-8")
            print(f"Расшифровка: {args.out} ({len(transcript)} символов)")
        else:
            print(transcript)
        return 0

    if args.chunks:
        try:
            written = materialize_chunks(
                video_dir,
                max_chars=args.max_chars,
                window_ms=args.window * 1000,
            )
        except (OSError, ValueError) as exc:
            print(f"Ошибка: {exc}", file=sys.stderr)
            return 1

        print(f"Создан индекс и чанки: {len(written) - 1}")
        for path in written:
            print(path.relative_to(video_dir))
        return 0

    try:
        written = materialize(video_dir, partial=args.partial)
    except (OSError, ValueError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1

    prefix = "Создано подтверждённых разделов (частичная карта)" if args.partial else "Создано разделов"
    print(f"{prefix}: {len(written)}")
    for path in written:
        print(path.relative_to(video_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
