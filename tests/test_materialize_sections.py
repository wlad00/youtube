import tempfile
import unittest
from pathlib import Path

from tools.materialize_sections import (
    Cue,
    build_transcript_blocks,
    chunk_transcript,
    materialize_chunks,
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


if __name__ == "__main__":
    unittest.main()
