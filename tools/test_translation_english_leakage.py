"""Regression checks for reader-facing prose hidden in Markdown fences."""

import unittest
from pathlib import Path

from check_translation_english_leakage import (
    copied_english_prose_spans,
    copied_english_link_labels,
    copied_english_headings,
    copied_reader_fenced_examples,
    copied_reader_fenced_lines,
    prose_sentences_with_link_slots,
    reader_fenced_prose,
    visible_text,
)


class FencedProseTests(unittest.TestCase):
    def test_flags_copied_descriptive_headings_but_not_product_name_headings(self):
        source = (
            "## Be Wary of Public Wi-Fi\n\n"
            "## Safeguard Your Social Media Accounts\n\n"
            "## Visual Studio Code"
        )
        target = source

        self.assertEqual(
            copied_english_headings(source, target),
            [
                "be wary of public wi fi",
                "safeguard your social media accounts",
            ],
        )

    def test_ignores_heading_text_inside_code_fences(self):
        source = "```text\n## Be Wary of Public Wi-Fi\n```"
        target = "```text\n## Be Wary of Public Wi-Fi\n```"

        self.assertEqual(copied_english_headings(source, target), [])

    def test_flags_two_word_descriptive_link_labels_but_not_single_word_names(self):
        source = (
            "[VPN service](https://example.com/vpn) "
            "[FBI](https://example.com/fbi)"
        )
        target = (
            "[VPN service](https://example.com/vpn) "
            "[FBI](https://example.com/fbi)"
        )

        self.assertEqual(
            copied_english_link_labels(source, target),
            ["VPN service => https://example.com/vpn"],
        )

    def test_link_label_copy_requires_the_same_target(self):
        source = "[VPN service](https://example.com/vpn)"
        target = "[VPN service](https://example.com/other)"

        self.assertEqual(copied_english_link_labels(source, target), [])

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
        self.assertFalse(copied_reader_fenced_lines(evidence, evidence))

    def test_finds_short_copied_prose_lines_in_reader_fences(self):
        source = (
            "```text\n"
            "Source: docs/requirements.md, revision 1.\n"
            "Retain synthetic export files for 30 days.\n"
            "```"
        )
        target = source

        self.assertEqual(
            copied_reader_fenced_lines(source, target),
            {
                "source docs requirements md revision 1",
                "retain synthetic export files for 30 days",
            },
        )

    def test_ignores_identifier_and_path_mappings_in_reader_fences(self):
        mapping = "```text\nREQ-17 -> requirement.json\nRUN-04 → runbook.md\n```"

        self.assertFalse(copied_reader_fenced_lines(mapping, mapping))

    def test_finds_english_sentences_inside_translated_copy(self):
        source = "The reviewer should translate each sentence while preserving technical names and URLs."
        target = "本文は翻訳済みです。 The reviewer should translate each sentence while preserving technical names and URLs."

        self.assertTrue(copied_english_prose_spans(source, target))

    def test_finds_copied_english_sentence_around_retained_product_links(self):
        source = (
            "Opt for secure communication apps such as "
            "[Signal](https://signal.org) or [Wire](https://wire.com)."
        )
        target = (
            "Opt for secure communication apps such as "
            "[Signal](https://signal.org) or [Wire](https://wire.com)."
        )

        self.assertEqual(
            prose_sentences_with_link_slots(source),
            prose_sentences_with_link_slots(target),
        )
        self.assertTrue(prose_sentences_with_link_slots(source))

    def test_link_slots_do_not_flag_translated_surrounding_prose(self):
        source = "Opt for secure communication apps such as [Signal](https://signal.org) or [Wire](https://wire.com)."
        target = "Utilisez des applications de messagerie sécurisées comme [Signal](https://signal.org) ou [Wire](https://wire.com)."

        self.assertNotEqual(
            prose_sentences_with_link_slots(source),
            prose_sentences_with_link_slots(target),
        )

    def test_does_not_treat_unchanged_book_titles_as_copied_prose(self):
        source = "Read [All-in-One CompTIA A+ Certification Exam Guide by Mike Meyers](https://example.com/book)."
        target = "[All-in-One CompTIA A+ Certification Exam Guide by Mike Meyers](https://example.com/book) を参照してください。"

        self.assertFalse(copied_english_prose_spans(source, target))


if __name__ == "__main__":
    unittest.main()
