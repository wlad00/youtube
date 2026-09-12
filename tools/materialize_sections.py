#!/usr/bin/env python3
"""Materialize semantic video sections declared in a video's README.md.

The agent defines semantic boundaries and enriched descriptions in README.md.
This script only slices the original subtitles into full-text section files.
It intentionally does not deduplicate, summarize, or rewrite subtitle text.

With --transcript it instead prints a reading copy of the subtitles: YouTube
rolling-caption repeats collapsed, timestamps kept, so semantic boundaries can
be chosen without loading the 4-5x larger raw SRT.
"""

from __future__ import annotations

import argparse
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


def render_transcript(cues: list[Cue], window_ms: int) -> str:
    chunks: list[tuple[int, list[str]]] = []

    for start_ms, line in dedupe_cues(cues):
        if chunks and start_ms - chunks[-1][0] < window_ms:
            chunks[-1][1].append(line)
        else:
            chunks.append((start_ms, [line]))

    return "\n\n".join(
        f"[{format_timecode(start_ms)}] {' '.join(lines)}" for start_ms, lines in chunks
    )


def materialize(video_dir: Path) -> list[Path]:
    readme_path = video_dir / "README.md"
    if not readme_path.is_file():
        raise ValueError(f"Не найден README.md: {readme_path}")

    subtitles_path = find_subtitles(video_dir)
    readme = readme_path.read_text(encoding="utf-8")
    sections = parse_sections(readme)
    cues = parse_srt(subtitles_path)

    video_end_ms = max(cue.end_ms for cue in cues)
    last = sections[-1]
    effective_last_end = video_end_ms if last.end_ms is None else last.end_ms
    if effective_last_end < max(cue.start_ms for cue in cues):
        raise ValueError(
            "Последний раздел заканчивается раньше субтитров. "
            "Используйте END или укажите конец ролика."
        )

    sections_dir = video_dir / "sections"
    sections_dir.mkdir(exist_ok=True)

    # sections/ is generated-only. Remove stale generated numeric files.
    for stale in sections_dir.glob("[0-9][0-9].md"):
        stale.unlink()

    written: list[Path] = []
    for section in sections:
        end_ms = video_end_ms if section.end_ms is None else section.end_ms
        body = section_text(cues, section.start_ms, end_ms)
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
            f"Источник: `../{subtitles_path.name}`  \n"
            f"Интервал: `{format_timecode(section.start_ms)} --> "
            f"{format_timecode(end_ms)}`\n\n"
            f"{enrichment}"
            f"{body}\n"
        )
        out.write_text(content, encoding="utf-8")
        written.append(out)

    return written


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Создать sections/*.md по смысловым границам из README.md."
    )
    parser.add_argument(
        "video_dir",
        type=Path,
        help="Папка ролика, содержащая README.md и subtitles.*.srt",
    )
    parser.add_argument(
        "--transcript",
        action="store_true",
        help="Не создавать разделы, а выдать очищенную расшифровку для чтения",
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
        default=30,
        help="Секунд текста под одной меткой времени в --transcript (по умолчанию 30)",
    )
    args = parser.parse_args()

    video_dir = args.video_dir.resolve()

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

    try:
        written = materialize(video_dir)
    except (OSError, ValueError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1

    print(f"Создано разделов: {len(written)}")
    for path in written:
        print(path.relative_to(video_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
