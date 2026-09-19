import tempfile
import unittest
from pathlib import Path

from tools.materialize_sections import (
    Cue,
    build_transcript_blocks,
    chunk_transcript,
    materialize,
    materialize_chunks,
    parse_sections_yaml,
    parse_transcript_cleaned,
    render_transcript,
)


class AutomaticChunksTest(unittest.TestCase):
    def test_chunks_cover_cleaned_transcript_with_stable_contiguous_bounds(self):
        cues = [
            Cue(0, 1000, "А\nБ"),
            Cue(1000, 2000, "Б\nВ"),
            Cue(2000, 3000, "В\nГ"),
            Cue(3000, 4000, "Г\nД"),
        ]
        blocks = build_transcript_blocks(cues, window_ms=1)

        first = chunk_transcript(blocks, video_end_ms=4000, max_chars=24)
        second = chunk_transcript(blocks, video_end_ms=4000, max_chars=24)

        self.assertEqual(first, second)
        self.assertEqual(render_transcript(cues, 1), "\n\n".join(c.body for c in first))
        self.assertTrue(all(len(c.body) <= 24 for c in first))
        self.assertEqual(first[0].start_ms, 0)
        self.assertEqual(first[-1].end_ms, 4000)
        self.assertTrue(
            all(previous.end_ms == current.start_ms for previous, current in zip(first, first[1:]))
        )

    def test_materialization_preserves_source_readme_and_semantic_sections(self):
        with tempfile.TemporaryDirectory() as temp:
            video_dir = Path(temp)
            readme = "---\nreview:\n  state: open\n---\n\n<!-- sections:begin -->\n<!-- sections:end -->\n"
            subtitles = (
                "1\n00:00:00,000 --> 00:00:01,000\nПервая\nВторая\n\n"
                "2\n00:00:01,000 --> 00:00:02,000\nВторая\nТретья\n"
            )
            (video_dir / "README.md").write_text(readme, encoding="utf-8")
            (video_dir / "subtitles.uk.srt").write_text(subtitles, encoding="utf-8")
            sections_dir = video_dir / "sections"
            sections_dir.mkdir()
            (sections_dir / "01.md").write_text("semantic\n", encoding="utf-8")

            materialize_chunks(video_dir, max_chars=6000, window_ms=30_000)
            first_snapshot = {
                path.relative_to(video_dir): path.read_bytes()
                for path in sorted((video_dir / "chunks").glob("*.md"))
            }
            materialize_chunks(video_dir, max_chars=6000, window_ms=30_000)
            second_snapshot = {
                path.relative_to(video_dir): path.read_bytes()
                for path in sorted((video_dir / "chunks").glob("*.md"))
            }

            self.assertEqual(first_snapshot, second_snapshot)
            self.assertEqual((video_dir / "README.md").read_text(encoding="utf-8"), readme)
            self.assertEqual((video_dir / "subtitles.uk.srt").read_text(encoding="utf-8"), subtitles)
            self.assertEqual((sections_dir / "01.md").read_text(encoding="utf-8"), "semantic\n")
            self.assertIn("Количество: **1**", (video_dir / "chunks" / "README.md").read_text(encoding="utf-8"))


    def test_sections_yaml_parses_minimal_map(self):
        sections = parse_sections_yaml(
            'sections:\n'
            '  - title: "Введение"\n'
            '    start: "00:00:00"\n'
            '    end: "00:00:02"\n'
            '  - title: "Вывод"\n'
            '    start: "00:00:02"\n'
            '    end: END\n'
        )

        self.assertEqual([s.title for s in sections], ["Введение", "Вывод"])
        self.assertEqual(sections[0].start_ms, 0)
        self.assertEqual(sections[0].end_ms, 2000)
        self.assertIsNone(sections[1].end_ms)

    def test_yaml_materialization_uses_cleaned_text_and_syncs_readme(self):
        with tempfile.TemporaryDirectory() as temp:
            video_dir = Path(temp)
            readme = "---\nreview:\n  state: open\n---\n\n# Ролик\n"
            subtitles = (
                "1\n00:00:00,000 --> 00:00:01,000\nПервая\nВторая\n\n"
                "2\n00:00:01,000 --> 00:00:02,000\nВторая\nТретья\n\n"
                "3\n00:00:02,000 --> 00:00:03,000\nТретья\nЧетвертая\n\n"
                "4\n00:00:03,000 --> 00:00:04,000\nЧетвертая\nПятая\n"
            )
            sections_yaml = (
                'sections:\n'
                '  - title: "Первая мысль"\n'
                '    start: "00:00:00"\n'
                '    end: "00:00:02"\n'
                '  - title: "Вторая мысль"\n'
                '    start: "00:00:02"\n'
                '    end: END\n'
            )
            (video_dir / "README.md").write_text(readme, encoding="utf-8")
            (video_dir / "subtitles.ru.srt").write_text(subtitles, encoding="utf-8")
            (video_dir / "transcript.cleaned.md").write_text(
                "[00:00:00] Первая Вторая Третья\n\n"
                "[00:00:02] Четвертая Пятая\n",
                encoding="utf-8",
            )
            (video_dir / "sections.yaml").write_text(sections_yaml, encoding="utf-8")

            written = materialize(video_dir)

            self.assertEqual([path.name for path in written], ["01.md", "02.md"])
            first = (video_dir / "sections" / "01.md").read_text(encoding="utf-8")
            second = (video_dir / "sections" / "02.md").read_text(encoding="utf-8")
            updated_readme = (video_dir / "README.md").read_text(encoding="utf-8")

            self.assertEqual(first.count("Вторая"), 1)
            self.assertEqual(first.count("Третья"), 1)
            self.assertEqual(second.count("Четвертая"), 1)
            self.assertIn("Источник: `../transcript.cleaned.md`", first)
            self.assertIn("### 1. Первая мысль", updated_readme)
            self.assertIn("### 2. Вторая мысль", updated_readme)
            self.assertIn("review:\n  state: open", updated_readme)


    def test_materialize_sections_uses_cleaned_transcript_without_srt(self):
        with tempfile.TemporaryDirectory() as temp:
            video_dir = Path(temp)
            readme = "---\nreview:\n  state: open\n---\n\n# Ролик\n"
            (video_dir / "README.md").write_text(readme, encoding="utf-8")
            (video_dir / "transcript.cleaned.md").write_text(
                "[00:00:00] Первая строка\n\n"
                "[00:00:05] Вторая строка\n\n"
                "[00:00:10] Третья строка\n",
                encoding="utf-8",
            )
            sections_yaml = (
                'sections:\n'
                '  - title: "Начало"\n'
                '    start: "00:00:00"\n'
                '    end: "00:00:05"\n'
                '  - title: "Продолжение"\n'
                '    start: "00:00:05"\n'
                '    end: END\n'
            )
            (video_dir / "sections.yaml").write_text(sections_yaml, encoding="utf-8")

            # No subtitles.*.srt anywhere in video_dir: find_subtitles() would
            # raise if the script tried to fall back to it.
            written = materialize(video_dir)

            self.assertEqual([path.name for path in written], ["01.md", "02.md"])
            first = (video_dir / "sections" / "01.md").read_text(encoding="utf-8")
            second = (video_dir / "sections" / "02.md").read_text(encoding="utf-8")
            self.assertIn("[00:00:00] Первая строка", first)
            self.assertNotIn("Вторая строка", first)
            self.assertIn("[00:00:05] Вторая строка", second)
            self.assertIn("[00:00:10] Третья строка", second)
            self.assertIn("Источник: `../transcript.cleaned.md`", first)

    def test_materialize_chunks_uses_cleaned_transcript_without_srt(self):
        with tempfile.TemporaryDirectory() as temp:
            video_dir = Path(temp)
            (video_dir / "transcript.cleaned.md").write_text(
                "[00:00:00] Раз\n\n"
                "[00:00:01] Два\n\n"
                "[00:00:02] Три\n",
                encoding="utf-8",
            )

            materialize_chunks(video_dir, max_chars=6000, window_ms=30_000)

            content = (video_dir / "chunks" / "01.md").read_text(encoding="utf-8")
            self.assertIn("[00:00:00] Раз", content)
            self.assertIn("[00:00:01] Два", content)
            self.assertIn("[00:00:02] Три", content)
            self.assertIn("../transcript.cleaned.md", content)
            index = (video_dir / "chunks" / "README.md").read_text(encoding="utf-8")
            self.assertIn("../transcript.cleaned.md", index)

    def test_materialize_sections_falls_back_to_srt_without_cleaned_transcript(self):
        with tempfile.TemporaryDirectory() as temp:
            video_dir = Path(temp)
            readme = "---\nreview:\n  state: open\n---\n\n# Ролик\n"
            subtitles = (
                "1\n00:00:00,000 --> 00:00:01,000\nПервая\nВторая\n\n"
                "2\n00:00:01,000 --> 00:00:02,000\nВторая\nТретья\n\n"
                "3\n00:00:02,000 --> 00:00:03,000\nТретья\nЧетвертая\n\n"
                "4\n00:00:03,000 --> 00:00:04,000\nЧетвертая\nПятая\n"
            )
            sections_yaml = (
                'sections:\n'
                '  - title: "Первая мысль"\n'
                '    start: "00:00:00"\n'
                '    end: "00:00:02"\n'
                '  - title: "Вторая мысль"\n'
                '    start: "00:00:02"\n'
                '    end: END\n'
            )
            (video_dir / "README.md").write_text(readme, encoding="utf-8")
            (video_dir / "subtitles.ru.srt").write_text(subtitles, encoding="utf-8")
            (video_dir / "sections.yaml").write_text(sections_yaml, encoding="utf-8")

            # transcript.cleaned.md is intentionally absent: legacy videos
            # must still materialize from subtitles.*.srt.
            written = materialize(video_dir)

            self.assertEqual([path.name for path in written], ["01.md", "02.md"])
            first = (video_dir / "sections" / "01.md").read_text(encoding="utf-8")
            self.assertIn("Источник: `../subtitles.ru.srt`", first)
            self.assertEqual(first.count("Вторая"), 1)
            self.assertEqual(first.count("Третья"), 1)

    def test_materialize_prefers_cleaned_transcript_text_over_srt(self):
        with tempfile.TemporaryDirectory() as temp:
            video_dir = Path(temp)
            readme = "---\nreview:\n  state: open\n---\n\n# Ролик\n"
            (video_dir / "README.md").write_text(readme, encoding="utf-8")
            (video_dir / "subtitles.ru.srt").write_text(
                "1\n00:00:00,000 --> 00:00:01,000\nИз SRT\n", encoding="utf-8"
            )
            (video_dir / "transcript.cleaned.md").write_text(
                "[00:00:00] Из transcript.cleaned.md\n", encoding="utf-8"
            )
            sections_yaml = (
                'sections:\n'
                '  - title: "Всё"\n'
                '    start: "00:00:00"\n'
                '    end: END\n'
            )
            (video_dir / "sections.yaml").write_text(sections_yaml, encoding="utf-8")

            materialize(video_dir)

            body = (video_dir / "sections" / "01.md").read_text(encoding="utf-8")
            self.assertIn("Из transcript.cleaned.md", body)
            self.assertNotIn("Из SRT", body)

    def test_materialize_partial_uses_cleaned_transcript_without_srt(self):
        with tempfile.TemporaryDirectory() as temp:
            video_dir = Path(temp)
            readme = "---\nreview:\n  state: open\n---\n\n# Ролик\n"
            (video_dir / "README.md").write_text(readme, encoding="utf-8")
            (video_dir / "transcript.cleaned.md").write_text(
                "[00:00:00] Начало разговора\n\n"
                "[00:00:07] Продолжение, ещё не размечено\n",
                encoding="utf-8",
            )
            sections_yaml = (
                'sections:\n'
                '  - title: "Начало"\n'
                '    start: "00:00:00"\n'
                '    end: "00:00:07"\n'
            )
            (video_dir / "sections.yaml").write_text(sections_yaml, encoding="utf-8")

            written = materialize(video_dir, partial=True)

            self.assertEqual([path.name for path in written], ["01.md"])
            first = (video_dir / "sections" / "01.md").read_text(encoding="utf-8")
            self.assertIn("Начало разговора", first)
            self.assertNotIn("Продолжение", first)

    def test_parse_transcript_cleaned_rejects_malformed_line(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "transcript.cleaned.md"
            path.write_text("не таймкод и текст\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                parse_transcript_cleaned(path)


if __name__ == "__main__":
    unittest.main()
