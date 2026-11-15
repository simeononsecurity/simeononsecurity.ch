"""Regression checks for reader-facing prose hidden in Markdown fences."""

import csv
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from check_translation_english_leakage import (
    CSV_FIELDS,
    audit_bundle,
    copied_english_prose_spans,
    copied_english_link_labels,
    copied_english_headings,
    copied_english_opening,
    copied_english_taxonomy,
    copied_english_table_cells,
    taxonomy_count_differences,
    copied_reader_fenced_examples,
    copied_reader_fenced_lines,
    copied_reader_code_prose,
    copied_unlabeled_fence_lines,
    english_dominant_paragraphs,
    english_dominant_body,
    main as checker_main,
    markdown_structure,
    markdown_structure_differences,
    normalize,
    fenced_blocks,
    prose_sentences_with_link_slots,
    reader_fenced_code_prose,
    reader_fenced_prose,
    script_ratio,
    split_word_emphasis,
    yaml_front_matter_lists,
    visible_text,
)


class FencedProseTests(unittest.TestCase):
    def test_flags_unchanged_english_article_opening(self):
        source = "**Passing CompTIA's A+ Exams 220-1101 & 220-1102**\n\nA Polish paragraph follows."
        target = "**Passing CompTIA's A+ Exams 220-1101 & 220-1102**\n\nPolski akapit następuje."

        self.assertEqual(
            copied_english_opening(source, target),
            "passing comptia s a exams 220 1101 220 1102",
        )

    def test_flags_short_unchanged_descriptive_openings(self):
        for opening in ("Cybersecurity 101", "Data privacy laws"):
            with self.subTest(opening=opening):
                self.assertEqual(copied_english_opening(opening, opening), normalize(opening))

    def test_queues_opening_that_only_names_products_for_manual_review(self):
        product_list = "**Azure DevOps vs GitHub vs GitLab vs Bitbucket**"

        self.assertEqual(
            copied_english_opening(product_list, product_list),
            normalize(product_list),
        )

    def test_flags_copied_comparison_opening_with_descriptive_prose(self):
        opening = "Azure vs AWS is the wrong way to frame this decision."

        self.assertEqual(copied_english_opening(opening, opening), normalize(opening))

    def test_flags_comparison_opening_with_descriptive_suffix(self):
        opening = "Azure vs AWS network security"

        self.assertEqual(copied_english_opening(opening, opening), normalize(opening))

    def test_csv_report_keeps_reader_fence_findings_in_separate_columns(self):
        self.assertIn("exact_english_sentences", CSV_FIELDS)
        self.assertIn("copied_reader_fenced_lines", CSV_FIELDS)
        self.assertIn("copied_reader_code_prose", CSV_FIELDS)
        self.assertIn("copied_unlabeled_fence_lines", CSV_FIELDS)
        self.assertLess(
            CSV_FIELDS.index("exact_english_sentences"),
            CSV_FIELDS.index("copied_reader_fenced_lines"),
        )
        output = io.StringIO(newline="")
        finding = {field: "" for field in CSV_FIELDS}
        finding["copied_unlabeled_fence_lines"] = "primary network adapters"
        writer = csv.DictWriter(output, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerow(finding)
        output.seek(0)
        self.assertEqual(
            next(csv.DictReader(output))["copied_unlabeled_fence_lines"],
            "primary network adapters",
        )

    def test_flags_unchanged_descriptive_table_cell(self):
        source = (
            "| Méthode | Mean prefix reuse per trial |\n"
            "| --- | --- |\n"
            "| Résumé | 47.8 |\n"
        )
        target = (
            "| Méthode | Mean prefix reuse per trial |\n"
            "| --- | --- |\n"
            "| Resumen | 47.8 |\n"
        )
        self.assertEqual(
            copied_english_table_cells(source, target),
            ["table 1, row 1, cell 2: mean prefix reuse per trial"],
        )

    def test_flags_descriptive_table_cells_without_stopwords(self):
        table = "| Average latency |\n| --- |\n| 42 ms |\n"
        self.assertEqual(
            copied_english_table_cells(table, table),
            ["table 1, row 1, cell 1: average latency"],
        )

    def test_flags_generic_table_labels_missed_by_stopword_screen(self):
        table = (
            "| Component | Privacy question |\n"
            "| --- | --- |\n"
            "| Local model server | Evidence to collect |\n"
            "| Situation | Better first choice |\n"
            "| Reason | Other |\n"
        )
        self.assertEqual(
            copied_english_table_cells(table, table),
            [
                "table 1, row 1, cell 1: component",
                "table 1, row 1, cell 2: privacy question",
                "table 1, row 2, cell 1: local model server",
                "table 1, row 2, cell 2: evidence to collect",
                "table 1, row 3, cell 1: situation",
                "table 1, row 3, cell 2: better first choice",
                "table 1, row 4, cell 1: reason",
                "table 1, row 4, cell 2: other",
            ],
        )

    def test_flags_short_project_and_responsive_assistant_table_labels(self):
        self.assertEqual(
            copied_english_table_cells("| Short project |\n| --- |\n", "| Short project |\n| --- |\n"),
            ["table 1, row 1, cell 1: short project"],
        )
        self.assertEqual(
            copied_english_table_cells("| Responsive assistant |\n| --- |\n", "| Responsive assistant |\n| --- |\n"),
            ["table 1, row 1, cell 1: responsive assistant"],
        )

    def test_ignores_table_like_content_inside_code_fence(self):
        source = "```bash\n| Method | Mean prefix reuse per trial |\n| --- | --- |\n```"
        target = source
        self.assertEqual(copied_english_table_cells(source, target), [])

    def test_flags_english_paragraph_inside_otherwise_translated_article(self):
        english = (
            "The system gives users access to protected data and helps teams "
            "review each request before they approve changes. The process also "
            "records the result and sends a notice to the owner."
        )
        self.assertEqual(english_dominant_paragraphs(english, "fr"), [normalize(english)])

    def test_flags_short_paraphrased_english_paragraph(self):
        english = (
            "The team checks each request before granting access. "
            "It logs the result and alerts its owner."
        )

        self.assertLess(len(english.split()), 30)
        self.assertEqual(english_dominant_paragraphs(english, "fr"), [normalize(english)])

    def test_flags_several_short_english_paragraphs(self):
        text = (
            "The tool is in the box for users.\n\n"
            "It is not safe for users to proceed.\n\n"
            "Use the tool only if it is safe."
        )
        self.assertEqual(
            english_dominant_paragraphs(text, "fr"),
            [
                "the tool is in the box for users",
                "it is not safe for users to proceed",
                "use the tool only if it is safe",
            ],
        )

    def test_audit_flags_short_wholly_english_locale_file(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            bundle = root / "article"
            bundle.mkdir()
            source = bundle / "index.en.md"
            source.write_text(
                "---\ntitle: 'Review access'\n---\n"
                "## Scope\n\n"
                "Administrators examine each credential request before granting access "
                "to protected records. The platform retains an audit trail and alerts "
                "the responsible owner.\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Vérifier l’accès'\n---\n"
                "## Portée\n\n"
                "The team checks each request before granting access. It logs the result "
                "and alerts its owner.\n",
                encoding="utf-8",
            )

            with patch("check_translation_english_leakage.ROOT", root):
                findings = audit_bundle(source, ["fr"])

        self.assertEqual(len(findings), 1)
        self.assertIn("English_dominant_reader_paragraph", findings[0]["reasons"])

    def test_strict_gate_blocks_short_paraphrased_english_candidate_outside_repo(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Review access'\n---\n"
                "## Scope\n\nThe original English source describes a different process.\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Vérifier les accès'\n---\n"
                "## Portée\n\n"
                "The team checks each request before granting access. It logs the result "
                "and alerts its owner.\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("English_dominant_reader_body", stdout.getvalue())
        self.assertIn(str(bundle / "index.fr.md"), stdout.getvalue())

    def test_strict_gate_does_not_treat_one_english_paragraph_as_whole_body_fallback(self):
        body = (
            "Le système examine chaque demande d’accès avant d’approuver les changements. "
            "Il conserve une trace et avertit le responsable.\n\n"
            "Administrators examine each credential request before granting access "
            "to protected records. The platform retains an audit trail and alerts "
            "the responsible owner.\n"
        )

        self.assertFalse(english_dominant_body(body, "fr"))

    def test_audit_flags_short_exact_english_body_with_different_front_matter(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            bundle = root / "article"
            bundle.mkdir()
            body = "## Overview\n\nThe system records each approval.\n"
            self.assertLess(len(body.split()), 20)
            source = bundle / "index.en.md"
            source.write_text("---\ntitle: 'Review access'\n---\n" + body, encoding="utf-8")
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Vérifier l’accès'\nlastmod: 2026-11-14\n---\n" + body,
                encoding="utf-8",
            )

            with patch("check_translation_english_leakage.ROOT", root):
                findings = audit_bundle(source, ["fr"])

        self.assertEqual(len(findings), 1)
        self.assertIn("copied_english_body", findings[0]["reasons"])

    def test_audit_reports_unlabeled_fence_copy_reason_and_csv_value(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            bundle = root / "article"
            bundle.mkdir()
            source = bundle / "index.en.md"
            source.write_text(
                "---\ntitle: 'Network adapters'\n---\n"
                "## Overview\n\nThe adapter reports network details for review.\n\n"
                "```\nPrimary network adapters:\n```\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Adaptateurs réseau'\n---\n"
                "## Présentation\n\nL’adaptateur indique les informations réseau à vérifier.\n\n"
                "```\nPrimary network adapters:\n```\n",
                encoding="utf-8",
            )

            with patch("check_translation_english_leakage.ROOT", root):
                findings = audit_bundle(source, ["fr"])

        self.assertEqual(len(findings), 1)
        self.assertIn("copied_unlabeled_fence_line", findings[0]["reasons"])
        self.assertEqual(
            findings[0]["copied_unlabeled_fence_lines"],
            "primary network adapters",
        )

    def test_does_not_flag_product_names_as_short_english_paragraph(self):
        product_names = (
            "Microsoft Entra ID, Microsoft Defender, Azure Sentinel, "
            "and GitHub Actions."
        )

        self.assertEqual(english_dominant_paragraphs(product_names, "fr"), [])

    def test_does_not_flag_french_paragraph_or_short_product_name(self):
        french = (
            "Le système permet aux équipes de vérifier chaque demande avant "
            "d'approuver les changements et de prévenir le propriétaire."
        )
        self.assertEqual(english_dominant_paragraphs(french, "fr"), [])
        self.assertEqual(english_dominant_paragraphs("Microsoft Entra ID", "fr"), [])

    def test_ignores_english_product_names_inside_translated_indic_text(self):
        bengali = (
            "এখানে বাংলা ব্যাখ্যা রয়েছে এবং দলগুলো নিরাপত্তা অনুশীলন সম্পর্কে আলোচনা করে। "
            "Microsoft Entra ID এবং PowerShell নাম দুটি অপরিবর্তিত রাখা হয়েছে।"
        )
        self.assertEqual(english_dominant_paragraphs(bengali, "bn"), [])

    def test_ignores_many_product_names_inside_chinese_prose(self):
        chinese = (
            "方案支持 Microsoft Entra ID、Microsoft Defender、Azure Sentinel、GitHub Actions、"
            "PowerShell、Windows Server、Active Directory、Kubernetes、Docker、Prometheus、"
            "Grafana、StartMail、ProtonMail、Tutanota 和 OpenAI 等产品。"
        )
        self.assertEqual(english_dominant_paragraphs(chinese, "zh"), [])

    def test_flags_english_clause_even_when_chinese_script_dilutes_ratio(self):
        mixed = (
            "在易用性方面，StartMail、ProtonMail 和 Tutanota 都是安全电子邮件服务，用户可以比较它们的界面设计、导航方式、邮件整理工具和整体使用体验。"
            "StartMail stands out with its easy-to-use interface, ProtonMail offers a visually appealing layout with efficient email "
            "organization tools, and Tutanota 设计简洁明快。"
        )
        self.assertGreater(script_ratio(normalize(mixed), "zh"), 0.20)
        self.assertEqual(english_dominant_paragraphs(mixed, "zh"), [normalize(mixed)])

    def test_screens_reader_facing_markdown_fences(self):
        source = (
            "```markdown\n## Review the changes\n\nKeep the paths unchanged and "
            "verify every expected result before approval.\n```"
        )
        target = source

        self.assertEqual(len(reader_fenced_prose(target)), 1)
        self.assertTrue(copied_reader_fenced_examples(source, target))

    def test_flags_missing_translated_taxonomy_values_by_count(self):
        source = {"genre": ["Article"], "tags": [f"Tag {n}" for n in range(51)]}
        target = {"genre": ["Artikel"], "tags": [f"Marke {n}" for n in range(20)]}

        self.assertEqual(
            taxonomy_count_differences(source, target),
            {"tags": (51, 20)},
        )

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
                "strong_emphasis_markers": 0,
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

    def test_markdown_structure_flags_unbalanced_strong_emphasis(self):
        source = "A **bold phrase** remains in this sentence."
        balanced = "Une **phrase en gras** reste dans cette phrase."
        unbalanced = "Une **phrase en gras reste dans cette phrase."

        self.assertEqual(markdown_structure_differences(source, balanced), {})
        self.assertIn(
            "strong_emphasis_markers",
            markdown_structure_differences(source, unbalanced),
        )

    def test_markdown_structure_does_not_count_underscore_rules_as_emphasis(self):
        page = "Text with __emphasis__.\n\n______\n"

        self.assertEqual(markdown_structure(page)["strong_emphasis_markers"], 2)

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

    def test_flags_unchanged_headings_for_context_review(self):
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
                "visual studio code",
            ],
        )

    def test_flags_short_generic_heading_copies(self):
        self.assertEqual(copied_english_headings("## Switches", "## Switches"), ["switches"])

    def test_flags_english_fragments_in_mixed_language_headings(self):
        source = "## Gateways and All-in-One"
        target = "## Gateways / Todo en uno"
        target_with_phrase = "## Gateways / All-in-One"

        self.assertIn("gateways in gateways todo en uno", copied_english_headings(source, target))
        self.assertIn("all in gateways all in one", copied_english_headings(source, target_with_phrase))

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

    def test_flags_generic_single_word_link_labels(self):
        source = "[here](https://example.com/help)"
        target = "[here](https://example.com/help)"

        self.assertEqual(
            copied_english_link_labels(source, target),
            ["here => here => https://example.com/help"],
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

    def test_screens_comments_and_natural_language_strings_in_code_fences(self):
        source = (
            "```bash\n"
            "# If you created CLAUDE.md, run: git add CLAUDE.md\n"
            'git commit -m "Add lab guidance"\n'
            "git status --short\n"
            "```"
        )
        translated = (
            "```bash\n"
            "# Si creaste CLAUDE.md, ejecuta: git add CLAUDE.md\n"
            'git commit -m "Añadir guía del laboratorio"\n'
            "git status --short\n"
            "```"
        )

        self.assertEqual(
            reader_fenced_code_prose(source),
            {"if you created claude md run git add claude md", "add lab guidance"},
        )
        self.assertEqual(copied_reader_code_prose(source, source), reader_fenced_code_prose(source))
        self.assertFalse(copied_reader_code_prose(source, translated))

    def test_screens_python_function_and_class_docstrings(self):
        source = (
            "```python\n"
            "class Analyzer:\n"
            '    """Coordinate the analysis workflow."""\n'
            "    def render(self):\n"
            '        """Generate research visualizations."""\n'
            "        pass\n"
            "```"
        )
        translated = (
            "```python\n"
            "class Analyzer:\n"
            '    """Coordonner le flux d’analyse."""\n'
            "    def render(self):\n"
            '        """Générer des visualisations de recherche."""\n'
            "        pass\n"
            "```"
        )

        self.assertEqual(
            reader_fenced_code_prose(source),
            {"coordinate the analysis workflow", "generate research visualizations"},
        )
        self.assertFalse(copied_reader_code_prose(source, translated))

    def test_screens_powershell_comments_in_powershell_fences(self):
        source = (
            "```powershell\n"
            "# Analyze component store\n"
            "Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore\n"
            "````\n"
        )
        translated = (
            "```powershell\n"
            "# Analizar el almacén de componentes\n"
            "Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore\n"
            "````\n"
        )

        self.assertEqual(reader_fenced_code_prose(source), {"analyze component store"})
        self.assertFalse(copied_reader_code_prose(source, translated))

    def test_screens_comments_without_space_and_markup_language_comments(self):
        sample = (
            "```swift\n"
            "//Translate this instruction for readers.\n"
            "```\n"
            "```html\n"
            "<!-- Keep this explanatory label localized. -->\n"
            "````\n"
            "```c\n"
            "printf(\"Choose a file\");\n"
            "````\n"
            "```haskell\n-- Translate this Haskell comment\n````\n"
            "```erlang\n% Localize this Erlang comment\nio:format(\"ok\").% Explain this result\n````\n"
            "```clojure\n; Explain this Clojure comment\n````\n"
            "```css\n.icon { background: url(//cdn.example.com/icon.svg); }\n````\n"
            "```hcl\nresource \"thing\" {} // Explain this Terraform resource\n````\n"
        )

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {
                "translate this instruction for readers",
                "keep this explanatory label localized",
                "choose a file",
                "translate this haskell comment",
                "localize this erlang comment",
                "explain this result",
                "explain this clojure comment",
                "explain this terraform resource",
            },
        )

    def test_screens_inline_sql_and_ini_comments(self):
        sample = (
            "```sql\nSELECT 1; -- Translate this reader instruction\nSELECT 1;-- No-space SQL comment\n```\n"
            "```ini\nkey=value ; Localize this setting description\n```\n"
            "```python\nvalue=1# Translate this Python comment\nprint(\"Continue\")\n```\n"
            "```clojure\n(run); Explain this example\n```\n"
            "```javascript\ncall();// Translate this UI note\nconst url = \"https://example.com/path\";\n"
            "console.log(`Verify ${project} before continuing`);\n```\n"
            "```lua\nprint('start')-- Explain this output\n```\n"
        )

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {
                "translate this reader instruction",
                "no space sql comment",
                "localize this setting description",
                "translate this python comment",
                "continue",
                "explain this example",
                "translate this ui note",
                "verify project before continuing",
                "explain this output",
                "start",
            },
        )

    def test_ignores_structured_jsonc_fences(self):
        sample = '```jsonc\n{"print": "Reader-facing label"}\n```'
        self.assertEqual(reader_fenced_code_prose(sample), set())

    def test_screens_ansible_and_workflow_yaml_labels_and_messages(self):
        sample = (
            '```yaml\n- name: Configure web servers\n  hosts: webservers\n'
            '  tasks:\n    - name: Install Nginx\n      apt:\n        name: nginx\n'
            '    - name: Report status\n      debug:\n        msg: "Restart the service now"\n```'
        )

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {
                "configure web servers",
                "install nginx",
                "report status",
                "nginx",
                "restart the service now",
            },
        )

    def test_screens_multiline_yaml_block_scalar_labels_and_messages(self):
        sample = (
            "```yaml\n- name: |\n    Configure secure web servers before deployment\n"
            "  hosts: webservers\n  tasks:\n    - name: Report status\n"
            "      debug:\n        msg: >-\n          Restart the service now\n"
            "          and verify the health check before continuing.\n```"
            "\n```yml\n- name: Verify backups\n  debug:\n    msg: |\n"
            "      Verify the backup before deployment.\n```"
        )

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {
                "configure secure web servers before deployment",
                "report status",
                "restart the service now and verify the health check before continuing",
                "verify backups",
                "verify the backup before deployment",
            },
        )

    def test_screens_top_level_and_mapping_yaml_name_labels(self):
        sample = (
            "```yaml\nname: Build and test the application\n"
            "jobs:\n  build:\n    name: Compile and package the release\n"
            "  deploy:\n    name: |\n      Publish the verified release\n"
            "      after approval\n```"
        )

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {
                "build and test the application",
                "compile and package the release",
                "publish the verified release after approval",
            },
        )

    def test_yaml_ignores_identifier_only_and_fixed_status_messages(self):
        sample = (
            '```yml\n- name: "{{ result.stdout }}"\n'
            '  debug:\n    msg: "{{ result.stdout }}"\n'
            '- name: Report state\n  debug:\n    msg: "Ready"\n'
            '- name: Start\n```'
        )

        self.assertEqual(reader_fenced_code_prose(sample), {"report state", "ready", "start"})

    def test_ignores_fixed_status_output(self):
        sample = '```python\nprint("OK")\nprint("PASS: validated")\n```'
        self.assertEqual(reader_fenced_code_prose(sample), set())

    def test_screens_comments_in_perl_lua_and_scala_fences(self):
        sample = (
            "```perl\n# Translate this note for readers.\n```\n"
            "```lua\n-- Localize this instruction.\n```\n"
            "```scala\n// Explain this example.\n```"
        )

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {
                "translate this note for readers",
                "localize this instruction",
                "explain this example",
            },
        )

    def test_flags_generic_status_words_and_preserves_fixed_runtime_output(self):
        output = (
            '```python\nprint("PASS: all checks passed")\n'
            'print("Permission denied")\n'
            'print("Operation timed out")\n'
            'print("No changes detected")\n'
            'print("start")\n'
            'print("Done")\n'
            'print("Ready")\n'
            'print("CODE_NOT_FOUND")\n'
            'print("status_code")\n'
            '```javascript\nconsole.log("statusCode")\n```'
        )

        self.assertEqual(reader_fenced_code_prose(output), {"start", "done", "ready"})

    def test_detects_javascript_reader_facing_output_strings(self):
        output = '```javascript\nconsole.log("Configure your account before continuing")\n```'

        self.assertEqual(
            reader_fenced_code_prose(output),
            {"configure your account before continuing"},
        )

    def test_detects_cpp_stream_output_strings(self):
        output = '```cpp\nstd::cout << "Configure your account now";\n```'

        self.assertEqual(
            reader_fenced_code_prose(output),
            {"configure your account now"},
        )

    def test_detects_single_word_html_labels_and_accessibility_text(self):
        sample = (
            '```html\n<button>Submit</button>\n'
            '<span>Continue</span><div>Waiting</div>\n'
            '<input aria-label="Search" placeholder="Email">\n```'
        )

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {"submit", "continue", "waiting", "search", "email"},
        )

    def test_does_not_treat_hyphenated_ui_copy_as_an_identifier(self):
        sample = '```java\nSystem.out.println("Click-to-continue");\n```'

        self.assertEqual(reader_fenced_code_prose(sample), {"click to continue"})

    def test_extracts_output_strings_with_other_quote_characters(self):
        sample = '''```python
print("Don't skip setup")
print('She said "Continue before saving"')
```'''

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {"don t skip setup", "she said continue before saving"},
        )

    def test_extracts_two_character_reader_facing_output_labels(self):
        sample = '```python\nprint("Go")\n```'

        self.assertEqual(reader_fenced_code_prose(sample), {"go"})

    def test_queues_uppercase_ui_labels_for_manual_review(self):
        sample = '```javascript\nconsole.log("SAVE");\n```'

        self.assertEqual(reader_fenced_code_prose(sample), {"save"})

    def test_detects_reader_facing_output_strings_across_languages(self):
        sample = (
            '```java\nSystem.out.println("Configure your account now");\n```\n'
            '```go\nfmt.Println("Continue setup before running");\n```\n'
            '```csharp\nConsole.WriteLine("Save your changes now");\n```\n'
            '```rust\nprintln!("Restart the service when prompted");\n```\n'
            '```swift\nprint("Review the generated report");\n```\n'
            '```kotlin\nprintln("Choose your language below");\n```\n'
            '```php\necho "Select the preferred option";\n```\n'
            '```javascript\nconsole.log(`Configure your account before continuing`);\n```\n'
            '```html\n<button aria-label="Continue with setup">Continue to the next step</button>\n```'
        )

        self.assertEqual(
            reader_fenced_code_prose(sample),
            {
                "configure your account now",
                "continue setup before running",
                "save your changes now",
                "restart the service when prompted",
                "review the generated report",
                "choose your language below",
                "select the preferred option",
                "configure your account before continuing",
                "continue with setup",
                "continue to the next step",
            },
        )

    def test_longer_fence_closer_ends_the_correct_block(self):
        sample = "```bash\n# Translate this instruction for readers.\n````\nAfter the example."

        self.assertEqual(len(fenced_blocks(sample)), 1)
        self.assertIn("After the example.", visible_text(sample))
        self.assertNotIn("Translate this instruction", visible_text(sample))

    def test_detects_emphasis_markers_that_split_words(self):
        prose = (
            "**Lies** die Hinweise. Codex unterstützt AGENTS.md. "
            "Lie**s** die [Anweisungen](https://example.com). "
            "Nutze `Con**sulta**` als unveränderten Codewert."
        )

        findings = split_word_emphasis(prose)

        self.assertEqual(len(findings), 1)
        self.assertIn("Lie**s**", findings[0])

    def test_ignores_intraword_underscores_but_flags_asterisk_emphasis(self):
        self.assertEqual(split_word_emphasis("Keep some_config_value unchanged."), [])
        findings = split_word_emphasis("Translate trans*la*tion carefully.")
        self.assertEqual(len(findings), 1)

    def test_ignores_literal_emphasis_syntax_in_fenced_examples(self):
        sample = "```markdown\nUse Con**sulta** as a markup example.\n```"

        self.assertEqual(split_word_emphasis(sample), [])

    def test_does_not_flag_emphasis_adjacent_to_japanese_or_chinese_words(self):
        japanese = "**未分類情報**とは、政府機関で使われる用語です。"
        chinese = "**非机密信息**是政府机构常用的术语。"

        self.assertEqual(split_word_emphasis(japanese, "ja"), [])
        self.assertEqual(split_word_emphasis(chinese, "zh"), [])

    def test_flags_a_japanese_particle_bolded_by_itself(self):
        self.assertEqual(len(split_word_emphasis("内容**は**次の通りです。", "ja")), 1)

    def test_effective_ai_delegation_examples_detect_an_english_copy(self):
        bundle = Path(__file__).resolve().parents[1] / "content/articles/effective-ai-agent-delegation"
        english_path = bundle / "index.en.md"
        translated_path = bundle / "index.de.md"
        if not english_path.is_file() or not translated_path.is_file():
            self.skipTest("article bundle is outside this sparse checkout")
        english = english_path.read_text(encoding="utf-8")
        translated = translated_path.read_text(encoding="utf-8")

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

    def test_flags_unchanged_descriptive_lines_in_unlabeled_fences(self):
        source = (
            "```\n"
            "Primary Espressif OUIs (ESP32-based modules):\n"
            "[...] 21 additional manufacturer OUIs ...]\n"
            "```"
        )

        self.assertEqual(
            copied_unlabeled_fence_lines(source, source),
            {
                "primary espressif ouis esp32 based modules",
                "21 additional manufacturer ouis",
            },
        )

    def test_ignores_oui_records_in_unlabeled_fences(self):
        data = "```\nD4:AD:FC - Espressif Inc. (Common ESP32-S3)\n```"

        self.assertFalse(copied_unlabeled_fence_lines(data, data))

    def test_flags_short_labels_in_unlabeled_fences(self):
        labels = "```\nDevice name\nVendor\n```"

        self.assertEqual(
            copied_unlabeled_fence_lines(labels, labels),
            {"device name", "vendor"},
        )

    def test_flags_colon_sentences_in_unlabeled_fences(self):
        sentence = "```\nDo not continue: check the logs.\n```"

        self.assertEqual(
            copied_unlabeled_fence_lines(sentence, sentence),
            {"do not continue check the logs"},
        )

    def test_queues_single_word_status_labels_in_unlabeled_fences(self):
        labels = "```\nstart\nstop\nready\ndone\n```"

        self.assertEqual(
            copied_unlabeled_fence_lines(labels, labels),
            {"start", "stop", "ready", "done"},
        )

    def test_ignores_numeric_network_data_in_unlabeled_fences(self):
        data = "```\n192.168.1.1 255.255.255.0\n```"

        self.assertFalse(copied_unlabeled_fence_lines(data, data))

    def test_flags_numeric_reader_facing_lines_in_unlabeled_fences(self):
        source = "```\n90% complete\n3 devices\n```"

        self.assertEqual(
            copied_unlabeled_fence_lines(source, source),
            {"90 complete", "3 devices"},
        )

    def test_flags_one_word_numeric_labels_and_bare_phase_headings(self):
        source = "```\nCost: $2,500\nSavings: 25%\nPhase 1\n```"

        self.assertEqual(
            copied_unlabeled_fence_lines(source, source),
            {"cost 2 500", "savings 25", "phase 1"},
        )

    def test_flags_brace_placeholders_and_arrow_prose_in_unlabeled_fences(self):
        source = (
            "```\n"
            "Device address: {address}\n"
            "Read the profile -> check status\n"
            "Need maximum anonymity → Tor Browser\n"
            "```"
        )

        self.assertEqual(
            copied_unlabeled_fence_lines(source, source),
            {
                "device address address",
                "read the profile check status",
                "need maximum anonymity tor browser",
            },
        )

    def test_ignores_identifier_mappings_in_unlabeled_fences(self):
        mapping = "```\nREQ-17 -> requirement.json\nRUN-04 → runbook.md\n```"

        self.assertFalse(copied_unlabeled_fence_lines(mapping, mapping))

    def test_flags_word_only_arrow_mapping_in_unlabeled_fence(self):
        prose = "```\nOpen -> Save\n```"

        self.assertEqual(
            copied_unlabeled_fence_lines(prose, prose),
            {"open save"},
        )

    def test_flags_numbered_phase_flow_in_unlabeled_fence(self):
        for line in ("Phase 1 -> Phase 2", "Step 1 -> Step 2", "Phase-1 -> Phase-2"):
            with self.subTest(line=line):
                prose = f"```\n{line}\n```"
                self.assertEqual(
                    copied_unlabeled_fence_lines(prose, prose),
                    {"phase 1 phase 2" if line.startswith("Phase") else "step 1 step 2"},
                )

    def test_flags_numbered_phase_headings_in_unlabeled_fences(self):
        source = "```\nPhase 1: Pilot (Months 1-2)\n```"

        self.assertIn(
            normalize("Phase 1: Pilot (Months 1-2)"),
            copied_unlabeled_fence_lines(source, source),
        )

    def test_flags_cost_prose_with_currency_and_arithmetic(self):
        line = "Cost savings: $2,500 device replaces $2,000 firewall + $3,000 SD-WAN appliance"
        source = f"```\n{line}\n```"

        self.assertIn(normalize(line), copied_unlabeled_fence_lines(source, source))

    def test_finds_english_sentences_inside_translated_copy(self):
        source = "The reviewer should translate each sentence while preserving technical names and URLs."
        target = "本文は翻訳済みです。 The reviewer should translate each sentence while preserving technical names and URLs."

        self.assertTrue(copied_english_prose_spans(source, target))

    def test_finds_short_copied_english_clause_inside_translated_prose(self):
        source = "Privacy rules protect people because personal data is collected online."
        target = "Datenschutzregeln schützen Menschen, weil personal data is collected online."

        self.assertIn(
            "personal data is collected online",
            copied_english_prose_spans(source, target),
        )

    def test_finds_short_english_connector_before_a_preserved_law_name(self):
        source = (
            "Privacy rules include the European Union's General Data Protection Regulation "
            "[GDPR](https://example.com/gdpr) and California's Consumer Privacy Act (CCPA)."
        )
        target = (
            "Datenschutzregeln umfassen die DSGVO [GDPR](https://example.com/gdpr) "
            "and California's Consumer Privacy Act (CCPA)."
        )

        findings = copied_english_prose_spans(source, target)
        self.assertIn("and", findings)
        self.assertFalse(any("california" in finding for finding in findings))

    def test_finds_four_word_copied_clause_inside_translated_paragraph(self):
        source = "Privacy rules help everyone. They matter to you."
        target = "Datenschutzregeln helfen allen. They matter to you."

        self.assertIn("they matter to you", copied_english_prose_spans(source, target))

    def test_ignores_formal_organization_name_in_translated_prose(self):
        source = (
            "The National Institute of Standards and Technology (NIST) publishes this guide."
        )
        target = (
            "Das National Institute of Standards and Technology (NIST) veröffentlicht diesen Leitfaden."
        )

        self.assertEqual(copied_english_prose_spans(source, target), set())

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
