"""Regression checks for reader-facing prose hidden in Markdown fences."""

import unittest
from pathlib import Path

from check_translation_english_leakage import (
    copied_english_prose_spans,
    copied_english_link_labels,
    copied_english_headings,
    copied_english_taxonomy,
    copied_reader_fenced_examples,
    copied_reader_fenced_lines,
    markdown_structure,
    markdown_structure_differences,
    prose_sentences_with_link_slots,
    reader_fenced_prose,
    yaml_front_matter_lists,
    visible_text,
)


class FencedProseTests(unittest.TestCase):
    def test_markdown_structure_counts_reader_content(self):
        page = (
            "## Section\n\n"
            "- One\n- Two\n\n1. Three\n2. Four\n\n"
            "| A | B |\n| --- | --- |\n| X | Y |\n\n"
            "```text\nSample text\n```\n"
        )

        self.assertEqual(
            markdown_structure(page),
            {
                "heading_levels": [2],
                "table_shapes": [[2, 2, 2]],
                "ordered_items": 2,
                "unordered_items": 2,
                "section_items": [
                    {"ordered": 0, "unordered": 0},
                    {"ordered": 2, "unordered": 2},
                ],
                "fence_languages": ["text"],
                "link_targets": [],
                "shortcodes": [],
            },
        )

    def test_markdown_structure_flags_omitted_sections_and_table_rows(self):
        source = (
            "## First\n\n- One\n- Two\n\n"
            "## Second\n\n1. One\n2. Two\n\n"
            "| A | B |\n| --- | --- |\n| X | Y |\n| Z | W |\n"
            "```text\nReader sample\n```\n"
        )
        target = (
            "## First\n\n- One\n\n"
            "| A | B |\n| --- | --- |\n| X | Y |\n"
        )

        differences = markdown_structure_differences(source, target)
        self.assertEqual(differences["heading_levels"], ([2, 2], [2]))
        self.assertEqual(differences["ordered_items"], (2, 0))
        self.assertEqual(differences["unordered_items"], (2, 1))
        self.assertEqual(
            differences["section_items"],
            (
                [
                    {"ordered": 0, "unordered": 0},
                    {"ordered": 0, "unordered": 2},
                    {"ordered": 2, "unordered": 0},
                ],
                [
                    {"ordered": 0, "unordered": 0},
                    {"ordered": 0, "unordered": 1},
                ],
            ),
        )
        self.assertEqual(differences["fence_languages"], (["text"], []))
        self.assertEqual(differences["table_shapes"], ([[2, 2, 2, 2]], [[2, 2, 2]]))

    def test_markdown_structure_allows_translated_cell_text(self):
        source = "## Source\n\n| Name | Value |\n| --- | --- |\n| First | Second |\n"
        target = "## Quelle\n\n| Nom | Valeur |\n| --- | --- |\n| Premier | Deuxième |\n"

        self.assertEqual(markdown_structure_differences(source, target), {})

    def test_markdown_structure_recognizes_tables_without_outer_pipes(self):
        source = "Name | Value\n--- | ---\nFirst | Second\n"
        target = "Nom | Valeur\n--- | ---\nPremier | Deuxième\n"

        self.assertEqual(markdown_structure(source)["table_shapes"], [[2, 2, 2]])
        self.assertEqual(markdown_structure_differences(source, target), {})

    def test_markdown_structure_preserves_link_targets_and_shortcodes(self):
        source = "See [the guide](https://example.com/guide).\n\n{{< figure src=\"one.webp\" >}}"
        translated = "Consultez [le guide](https://example.com/guide).\n\n{{< figure src=\"one.webp\" >}}"
        altered = "Consultez [le guide](https://example.com/other)."

        self.assertEqual(markdown_structure_differences(source, translated), {})
        self.assertIn("link_targets", markdown_structure_differences(source, altered))
        self.assertIn("shortcodes", markdown_structure_differences(source, altered))

    def test_parses_inline_and_block_yaml_tag_lists(self):
        header = (
            'tags: ["Online Privacy", "Safe, trusted sites", \'reader\'\'s guide\']\n'
            'genre:\n  - "Digital Safety"\n  - "Online Security"\n'
        )

        self.assertEqual(
            yaml_front_matter_lists(header, "tags"),
            ["Online Privacy", "Safe, trusted sites", "reader's guide"],
        )
        self.assertEqual(
            yaml_front_matter_lists(header, "genre"),
            ["Digital Safety", "Online Security"],
        )

    def test_flags_identical_taxonomy_values_including_single_words(self):
        source = {"tags": ["Online Privacy", "Product X", "privacy tips"]}
        target = {"tags": ["Online Privacy", "Producto X", "consejos de privacidad"]}

        self.assertEqual(
            copied_english_taxonomy(source, target),
            {"tags": ["Online Privacy"]},
        )

        self.assertEqual(
            copied_english_taxonomy(
                {"tags": ["cybersecurity", "FISMA"]},
                {"tags": ["cybersecurity", "FISMA"]},
            ),
            {"tags": ["FISMA", "cybersecurity"]},
        )

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
            ["VPN service => VPN service => https://example.com/vpn"],
        )

    def test_flags_english_source_phrase_inside_longer_target_link_label(self):
        source = "[Cybersecurity framework](https://example.com/framework)"
        target = "[Consulte el Cybersecurity framework recomendado aquí](https://example.com/framework)"

        self.assertEqual(
            copied_english_link_labels(source, target),
            [
                "Cybersecurity framework => Consulte el Cybersecurity framework recomendado aquí => "
                "https://example.com/framework"
            ],
        )

    def test_flags_copied_source_link_phrase_with_attached_cjk_suffix(self):
        source = "[Cybersecurity framework](https://example.com/framework)"
        targets = [
            "[Cybersecurity frameworkのページ](https://example.com/framework)",
            "[Cybersecurity framework指南](https://example.com/framework)",
        ]

        for target in targets:
            with self.subTest(target=target):
                self.assertEqual(
                    copied_english_link_labels(source, target),
                    [
                        "Cybersecurity framework => "
                        f"{target.split('[', 1)[1].split(']', 1)[0]} => "
                        "https://example.com/framework"
                    ],
                )

    def test_does_not_flag_single_word_source_label_inside_longer_target_label(self):
        source = "[Framework](https://example.com/framework)"
        target = "[Consulte el framework recomendado](https://example.com/framework)"

        self.assertEqual(copied_english_link_labels(source, target), [])

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
        translated = (bundle / "index.de.md").read_text(encoding="utf-8")

        self.assertEqual(len(reader_fenced_prose(english)), 2)
        self.assertTrue(copied_reader_fenced_examples(english, english))
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

    def test_ignores_literal_validation_output_in_reader_fences(self):
        output = "```text\nPASS: consistency only, human approval remains required\n```"

        self.assertFalse(copied_reader_fenced_lines(output, output))

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
