"""Regression checks for reader-facing prose hidden in Markdown fences."""

import unittest
from pathlib import Path

from check_translation_english_leakage import (
    copied_english_prose_spans,
    copied_reader_fenced_examples,
    reader_fenced_prose,
    visible_text,
)


class FencedProseTests(unittest.TestCase):
    def test_keeps_text_fences_and_excludes_executable_fences(self):
        sample = (
            "```text\nTranslate this prompt for the reader.\n```\n"
            "```python\nprint('English code string')\n```\n"
            "~~~plaintext\nThis form is reader facing.\n~~~"
        )

        visible = visible_text(sample)

        self.assertIn("Translate this prompt for the reader.", visible)
        self.assertIn("This form is reader facing.", visible)
        self.assertNotIn("English code string", visible)
        self.assertEqual(len(reader_fenced_prose(sample)), 2)

    def test_effective_ai_delegation_examples_detect_an_english_copy(self):
        bundle = Path(__file__).resolve().parents[1] / "content/articles/effective-ai-agent-delegation"
        english = (bundle / "index.en.md").read_text(encoding="utf-8")
        misplaced_english = (bundle / "locale/index.fr.md").read_text(encoding="utf-8")
        translated = (bundle / "index.de.md").read_text(encoding="utf-8")

        self.assertEqual(len(reader_fenced_prose(english)), 2)
        self.assertTrue(copied_reader_fenced_examples(english, misplaced_english))
        self.assertFalse(copied_reader_fenced_examples(english, translated))

    def test_identical_structured_evidence_is_not_english_prose(self):
        evidence = "```text\n2,12,127,221:506f9a16030103,45,191,221:0050f208000000\n```"

        self.assertFalse(copied_reader_fenced_examples(evidence, evidence))

    def test_finds_english_sentences_inside_translated_copy(self):
        source = "The reviewer should translate each sentence while preserving technical names and URLs."
        target = "本文は翻訳済みです。 The reviewer should translate each sentence while preserving technical names and URLs."

        self.assertTrue(copied_english_prose_spans(source, target))

    def test_does_not_treat_unchanged_book_titles_as_copied_prose(self):
        source = "Read [All-in-One CompTIA A+ Certification Exam Guide by Mike Meyers](https://example.com/book)."
        target = "[All-in-One CompTIA A+ Certification Exam Guide by Mike Meyers](https://example.com/book) を参照してください。"

        self.assertFalse(copied_english_prose_spans(source, target))


if __name__ == "__main__":
    unittest.main()
