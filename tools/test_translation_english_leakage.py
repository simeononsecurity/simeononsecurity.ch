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
    copied_english_mixed_phrases,
    copied_english_generic_terms,
    copied_english_link_labels,
    copied_english_generic_link_labels,
    copied_english_shortcode_descriptions,
    copied_english_internal_link_labels,
    copied_english_link_connectors,
    copied_english_headings,
    copied_english_acronym_expansions,
    copied_english_inline_acronym_expansions,
    fixed_glossary_key,
    missing_acronym_keys,
    copied_english_opening,
    copied_english_prose_paragraphs,
    copied_english_taxonomy,
    copied_generic_english_taxonomy,
    copied_english_table_cells,
    taxonomy_count_differences,
    copied_reader_fenced_examples,
    copied_reader_fenced_lines,
    copied_english_fenced_formulas,
    copied_reader_code_prose,
    english_reader_code_prose_fallback,
    copied_unlabeled_fence_lines,
    english_dominant_paragraphs,
    high_confidence_english_paragraphs,
    copied_english_reader_verbs,
    english_dominant_body,
    english_dominant_title,
    english_dominant_title_review,
    main as checker_main,
    markdown_structure,
    markdown_structure_differences,
    hugo_github_heading_ids,
    normalize,
    fenced_blocks,
    prose_sentences_with_link_slots,
    reader_fenced_code_prose,
    reader_fenced_prose,
    script_ratio,
    split_word_emphasis,
    yaml_front_matter_lists,
    yaml_front_matter_scalar,
    visible_text,
)


class FencedProseTests(unittest.TestCase):
    def test_front_matter_scalar_reads_unquoted_and_folded_english_metadata(self):
        header = (
            "title: English title\n"
            "description: >-\n"
            "  This is an English description\n"
            "  that continues on another line.\n"
            "coverAlt: |\n"
            "  English cover text\n"
            "  with a second line.\n"
        )
        self.assertEqual(yaml_front_matter_scalar(header, "title"), "English title")
        self.assertEqual(
            yaml_front_matter_scalar(header, "description"),
            "This is an English description that continues on another line.",
        )
        self.assertEqual(
            yaml_front_matter_scalar(header, "coverAlt"),
            "English cover text\nwith a second line.",
        )

    def test_strict_gate_blocks_exact_english_description_in_yaml(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            source = (
                "---\ntitle: 'Access review'\n"
                "description: >-\n"
                "  Administrators review each access request before granting permission.\n"
                "---\n\nLocalized body text.\n"
            )
            target = source.replace(
                "title: 'Access review'", "title: 'Vérification des accès'"
            ).replace("Localized body text.", "Texte localisé.")
            (bundle / "index.en.md").write_text(source, encoding="utf-8")
            (bundle / "index.fr.md").write_text(target, encoding="utf-8")
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", str(bundle)],
                ),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("copied_english_reader_metadata", stdout.getvalue())

    def test_quoted_yaml_scalar_with_comment_does_not_consume_following_metadata(self):
        header = (
            'description: "The \\\"Access Guide\\\"" # copied source text\n'
            'coverAlt: "Localized illustration"\n'
        )
        self.assertEqual(
            yaml_front_matter_scalar(header, "description"),
            'The "Access Guide"',
        )
        self.assertEqual(
            yaml_front_matter_scalar(header, "coverAlt"),
            "Localized illustration",
        )

    def test_empty_block_scalar_does_not_consume_next_top_level_field(self):
        header = 'description: |\ncoverAlt: "Localized illustration"\n'
        self.assertEqual(yaml_front_matter_scalar(header, "description"), "")
        self.assertEqual(
            yaml_front_matter_scalar(header, "coverAlt"),
            "Localized illustration",
        )

    def test_strict_gate_blocks_short_copied_description_and_image_metadata(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            source = (
                "---\ntitle: 'Access review'\n"
                "description: Overview\n"
                "coverAlt: Access review\n"
                "coverCaption: |\n"
                "  Request workflow\n"
                "---\n\nEnglish text describes the review process in detail.\n"
            )
            target = (
                "---\ntitle: 'Revisión de acceso'\n"
                "description: Overview\n"
                "coverAlt: Access review\n"
                "coverCaption: |\n"
                "  Request workflow\n"
                "---\n\nEl texto describe el proceso de revisión con detalle.\n"
            )
            (bundle / "index.en.md").write_text(source, encoding="utf-8")
            (bundle / "index.es.md").write_text(target, encoding="utf-8")
            stdout = io.StringIO()
            report = Path(temporary_directory) / "metadata.csv"
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["es"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", "--csv", str(report), str(bundle)],
                ),
                redirect_stdout(stdout),
            ):
                result = checker_main()
            with report.open(encoding="utf-8", newline="") as handle:
                findings = list(csv.DictReader(handle))

        self.assertEqual(result, 1)
        self.assertIn("copied_english_reader_metadata", findings[0]["reasons"])
        self.assertEqual(
            findings[0]["copied_english_metadata"],
            "description: Overview | coverAlt: Access review | coverCaption: Request workflow",
        )

    def test_non_strict_summary_excludes_drafts_from_published_count(self):
        with TemporaryDirectory() as temporary_directory:
            articles = Path(temporary_directory) / "content" / "articles"
            published = articles / "published"
            draft = articles / "draft"
            published.mkdir(parents=True)
            draft.mkdir(parents=True)
            source = "---\ntitle: 'Example article'\ndraft: false\n---\n\nSource prose.\n"
            translation = "---\ntitle: 'Article exemple'\ndraft: false\n---\n\nTexte source.\n"
            (published / "index.en.md").write_text(source, encoding="utf-8")
            (published / "index.fr.md").write_text(translation, encoding="utf-8")
            (draft / "index.en.md").write_text(
                source.replace("draft: false", "draft: true"), encoding="utf-8"
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.ARTICLES", articles),
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(sys, "argv", ["checker", "--all"]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertIn(result, (0, 1))
        self.assertIn("published bundles scanned: 1;", stdout.getvalue())

    def test_all_report_counts_only_published_bundles(self):
        with TemporaryDirectory() as temporary_directory:
            articles = Path(temporary_directory) / "content" / "articles"
            published = articles / "published"
            draft = articles / "draft"
            published.mkdir(parents=True)
            draft.mkdir(parents=True)
            source = "---\ntitle: 'Example article'\ndraft: false\n---\n\nSource prose.\n"
            translation = "---\ntitle: 'Article exemple'\ndraft: false\n---\n\nTexte source.\n"
            (published / "index.en.md").write_text(source, encoding="utf-8")
            (published / "index.fr.md").write_text(translation, encoding="utf-8")
            (draft / "index.en.md").write_text(
                source.replace("draft: false", "draft: true"), encoding="utf-8"
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.ARTICLES", articles),
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(sys, "argv", ["checker", "--all", "--fail-on-english-fallback"]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 0)
        self.assertIn("published bundles scanned: 1;", stdout.getvalue())
        self.assertIn("strict blockers: 0", stdout.getvalue())

    def test_strict_gate_blocks_missing_locale_files(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Example article'\n---\n\nSource prose.\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["es"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("strict blockers: 1", stdout.getvalue())
        self.assertIn("translation_missing", stdout.getvalue())

    def test_strict_gate_blocks_localized_file_with_english_body(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            body = (
                "## Overview\n\n"
                "Administrators review each access request before granting permission to protected records. "
                "The system records the decision and alerts the responsible owner.\n"
            )
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Access review'\n---\n" + body,
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Vérification des accès'\n---\n" + body,
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", str(bundle)],
                ),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("copied_english_body", stdout.getvalue())

    def test_english_title_screen_catches_low_stopword_descriptive_titles(self):
        self.assertTrue(
            english_dominant_title("Protect Your Data Now", "fr")
        )
        self.assertTrue(english_dominant_title("Security Incident", "de"))
        self.assertTrue(english_dominant_title("Security Showdown", "pl"))
        self.assertTrue(english_dominant_title("Secure Browsers", "pl"))
        self.assertTrue(english_dominant_title("Network Breach", "de"))
        self.assertTrue(english_dominant_title("RFID Skimming Attacks", "fr"))
        self.assertTrue(
            english_dominant_title(
                "Zero Trust Security Benefits and Challenges", "fr"
            )
        )
        self.assertFalse(
            english_dominant_title("The Legend of Zelda: A Link to the Past", "fr")
        )
        self.assertTrue(
            english_dominant_title_review("The Legend of Zelda: A Link to the Past", "fr")
        )
        self.assertTrue(
            english_dominant_title(
                "Protecting Your Personal Information: How to Keep Your Credit Cards Safe "
                "from RFID Skimming and other Physical Attacks",
                "fr",
            )
        )
        self.assertTrue(
            english_dominant_title(
                "Aktualizacja do Windows Server 2019 lub przejście na Azure: Which Option "
                "is Right for Your Business?",
                "pl",
            )
        )
        self.assertTrue(
            english_dominant_title(
                "OPSEC-proces: belangrijkste onderdelen en best practices", "nl"
            )
        )
        self.assertFalse(english_dominant_title("Zero Trust model: beveiliging", "nl"))
        self.assertFalse(english_dominant_title("Zero-Trust model: beveiliging", "nl"))
        self.assertTrue(
            english_dominant_title(
                "Comparaison des plateformes serveur modernes pour les petites entreprises: "
                "Which Option is Right for Your Business?",
                "fr",
            )
        )
        self.assertFalse(english_dominant_title("Azure DevOps vs GitHub", "fr"))
        self.assertFalse(english_dominant_title("Flipper Zero: la guía completa para hackers y makers", "es"))
        self.assertFalse(english_dominant_title("Privacy beschermen: de CCPA en uw rechten begrijpen", "nl"))
        self.assertFalse(english_dominant_title("Virtualisatie ontsluiten: meer IT-efficiëntie en schaalbaarheid", "nl"))
        self.assertFalse(english_dominant_title("Ubiquiti Unifi et TP-Link Omada : quel système réseau choisir ?", "fr"))
        self.assertTrue(english_dominant_title("Best Practices für sichere Codierung", "de"))
        self.assertTrue(english_dominant_title("Top Secure Browsers for Privacy Protection", "pl"))
        self.assertTrue(english_dominant_title("Cloud Security Showdown", "pl"))
        self.assertTrue(english_dominant_title("A Comprehensive Guide", "pl"))
        self.assertTrue(
            english_dominant_title("TOP SECURE BROWSERS FOR PRIVACY PROTECTION", "pl")
        )
        self.assertTrue(english_dominant_title_review("10 plugins, compétences et outils MCP pour Claude Code : guide pratique", "fr"))
        self.assertFalse(
            english_dominant_title(
                "Kreditkarten schützen: RFID-Skimming abwehren", "de"
            )
        )
        self.assertFalse(english_dominant_title("RFID Skimming", "de"))
        self.assertFalse(english_dominant_title("Skimming Attacks abwehren", "de"))
        self.assertTrue(english_dominant_title_review("Skimming Attacks abwehren", "de"))
        self.assertFalse(
            english_dominant_title(
                "Comment protéger votre carte contre le vol", "fr"
            )
        )

    def test_flags_unchanged_parenthetical_acronym_expansions_in_prose(self):
        source = (
            "The company uses HTTPS (hypertext transfer protocol secure) "
            "for customer connections.\n"
        )
        target = (
            "L’entreprise utilise HTTPS (hypertext transfer protocol secure) "
            "pour les connexions client.\n"
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "fr"),
            (["https: hypertext transfer protocol secure"], []),
        )

    def test_inline_acronym_screen_ignores_glossary_and_translated_expansions(self):
        entry = "- **HTTPS**: Hypertext Transfer Protocol Secure\n"
        self.assertEqual(
            copied_english_inline_acronym_expansions(entry, entry, "fr"),
            ([], []),
        )
        source = "HTTPS (hypertext transfer protocol secure) protects the connection."
        localized = "HTTPS (protocole de transfert hypertexte sécurisé) protège la connexion."
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, localized, "fr"),
            ([], []),
        )

    def test_inline_acronym_screen_allows_bilingual_expansion(self):
        source = "HTTPS (Hypertext Transfer Protocol Secure) protects the connection."
        target = (
            "HTTPS (Hypertext Transfer Protocol Secure, protocole de transfert "
            "hypertexte sécurisé) protège la connexion."
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "fr"),
            ([], ["https: hypertext transfer protocol secure"]),
        )

    def test_inline_acronym_screen_requires_localized_german_or_dutch_wording(self):
        source = "HTTPS (Hypertext Transfer Protocol Secure) protects the connection."
        cases = (
            (
                "de",
                "HTTPS (hypertext transfer protocol secure, encrypted connection "
                "protocol) schützt die Verbindung.",
                ["https: hypertext transfer protocol secure"],
                [],
            ),
            (
                "de",
                "HTTPS (hypertext transfer protocol secure, verschlüsselte "
                "Verbindung) schützt die Verbindung.",
                [],
                ["https: hypertext transfer protocol secure"],
            ),
            (
                "nl",
                "HTTPS (hypertext transfer protocol secure, encrypted connection "
                "protocol) beschermt de verbinding.",
                ["https: hypertext transfer protocol secure"],
                [],
            ),
            (
                "nl",
                "HTTPS (hypertext transfer protocol secure, versleutelde "
                "verbinding) beschermt de verbinding.",
                [],
                ["https: hypertext transfer protocol secure"],
            ),
        )
        for locale, target, expected_blockers, expected_reviews in cases:
            with self.subTest(locale=locale, target=target):
                self.assertEqual(
                    copied_english_inline_acronym_expansions(source, target, locale),
                    (expected_blockers, expected_reviews),
                )

    def test_inline_acronym_screen_recognizes_reviewed_polish_glosses(self):
        cases = (
            (
                "AES (Advanced Encryption Standard) protects data.",
                "AES (zaawansowany standard szyfrowania, Advanced Encryption Standard) chroni dane.",
                "aes: advanced encryption standard",
            ),
            (
                "OWASP (Open Web Application Security Project) publishes guidance.",
                "OWASP (Otwarty projekt bezpieczeństwa aplikacji internetowych, Open Web Application Security Project) publikuje zalecenia.",
                "owasp: open web application security project",
            ),
            (
                "TLS (Transport Layer Security) protects connections.",
                "TLS (bezpieczeństwo warstwy transportowej, Transport Layer Security) chroni połączenia.",
                "tls: transport layer security",
            ),
        )
        for source, target, expected_review in cases:
            with self.subTest(expected_review=expected_review):
                self.assertEqual(
                    copied_english_inline_acronym_expansions(source, target, "pl"),
                    ([], [expected_review]),
                )

    def test_inline_acronym_screen_accepts_localized_compounds_for_manual_review(self):
        cases = (
            (
                "de",
                "HTTPS (hypertext transfer protocol secure) protects data.",
                "HTTPS (hypertext transfer protocol secure, sicheres "
                "Datenübertragungsprotokoll) schützt die Verbindung.",
                "https: hypertext transfer protocol secure",
            ),
            (
                "nl",
                "NFC (near field communication) supports payments.",
                "NFC (near field communication, contactloze communicatie) "
                "is beschikbaar.",
                "nfc: near field communication",
            ),
            (
                "de",
                "VPN (virtual private network) protects traffic.",
                "VPN (virtual private network, virtuelles privates Netzwerk) "
                "schützt den Datenverkehr.",
                "vpn: virtual private network",
            ),
            (
                "nl",
                "VPN (virtual private network) protects traffic.",
                "VPN (virtual private network, virtueel privénetwerk) "
                "beschermt het verkeer.",
                "vpn: virtual private network",
            ),
            (
                "pt",
                "VPN (virtual private network) protects traffic.",
                "VPN (virtual private network, rede privada virtual) protege "
                "a conexão.",
                "vpn: virtual private network",
            ),
        )
        for locale, source, target, expected_review in cases:
            with self.subTest(locale=locale, target=target):
                self.assertEqual(
                    copied_english_inline_acronym_expansions(source, target, locale),
                    ([], [expected_review]),
                )

    def test_inline_acronym_screen_matches_hyphenated_german_compounds(self):
        source = "NFC (Near Field Communication) payments are convenient."
        target = "NFC-Zahlungen (Near Field Communication) sind bequem."
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "de"),
            ([], ["nfc: near field communication"]),
        )

    def test_inline_acronym_screen_uses_unicode_tokens_for_romanian(self):
        source = "NFC (Near Field Communication) payments are convenient."
        target = (
            "Plățile NFC (Near Field Communication, comunicare în câmp apropiat) "
            "sunt comode."
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "ro"),
            ([], ["nfc: near field communication"]),
        )

    def test_inline_acronym_screen_queues_transliterated_acronym_for_review(self):
        source = "NFC (Near Field Communication) payments are convenient."
        target = (
            "एनएफसी (नियर फील्ड कम्युनिकेशन) "
            "भुगतान सुविधाजनक हैं।"
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "hi"),
            (
                [],
                [
                    "nfc: possible noncanonical target key एनएफसी; map this occurrence "
                    "and verify expansion meaning"
                ],
            ),
        )

    def test_inline_acronym_screen_does_not_flag_unrelated_parenthetical(self):
        source = (
            "NFC (Near Field Communication) enables payment.\n\n"
            "More information appears in a separate section."
        )
        target = (
            "NFC (संपर्क रहित भुगतान तकनीक) "
            "भुगतान सक्षम करता है।\n\n"
            "अन्य जानकारी "
            "(यहां स्पष्टीकरण है)।"
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "hi"),
            ([], []),
        )

    def test_inline_acronym_screen_reviews_transliterated_repeat_in_same_paragraph(self):
        source = (
            "NFC (Near Field Communication) is useful, and NFC "
            "(Near Field Communication) is common."
        )
        target = (
            "NFC (नियर फील्ड कम्युनिकेशन) "
            "उपयोगी है, "
            "और एनएफसी "
            "(नियर फील्ड कम्युनिकेशन) आम है।"
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "hi"),
            (
                [],
                [
                    "nfc: possible noncanonical target key एनएफसी; map this occurrence "
                    "and verify expansion meaning"
                ],
            ),
        )

    def test_inline_acronym_screen_reviews_each_key_occurrence(self):
        source = (
            "NFC (Near Field Communication) payments work.\n\n"
            "NFC (Near Field Communication) payments are common."
        )
        target = (
            "NFC (नियर फील्ड कम्युनिकेशन) "
            "भुगतान काम करते हैं।\n\n"
            "एनएफसी (नियर फील्ड कम्युनिकेशन) "
            "भुगतान आम हैं।"
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "hi"),
            (
                [],
                [
                    "nfc: possible noncanonical target key एनएफसी; map this occurrence "
                    "and verify expansion meaning"
                ],
            ),
        )

    def test_inline_acronym_screen_checks_reader_lists_and_quotes(self):
        source = (
            "- Secure connections use HTTPS "
            "(hypertext transfer protocol secure).\n"
            "> HTTPS (hypertext transfer protocol secure) protects data.\n"
        )
        target = (
            "- Les connexions utilisent HTTPS "
            "(hypertext transfer protocol secure).\n"
            "> HTTPS (hypertext transfer protocol secure) protège les données.\n"
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "fr"),
            (["https: hypertext transfer protocol secure"], []),
        )

    def test_title_case_official_expansion_queues_review_instead_of_blocking(self):
        source = "NIST (National Institute of Standards and Technology) publishes guidance."
        target = "NIST (National Institute of Standards and Technology) publie des conseils."
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "fr"),
            ([], ["nist: national institute of standards and technology"]),
        )

    def test_bengali_transliteration_does_not_clear_expansion_review(self):
        source = "NFC (Near Field Communication) payments are convenient."
        target = (
            "NFC (Near Field Communication, "
            "নিয়ার ফিল্ড কমিউনিকেশন) "
            "পেমেন্ট সুবিধাজনক।"
        )
        self.assertEqual(
            copied_english_inline_acronym_expansions(source, target, "bn"),
            ([], ["nfc: near field communication"]),
        )

    def test_strict_gate_blocks_an_unchanged_inline_acronym_expansion(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "network-security"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Network Security'\n---\n"
                "HTTPS (hypertext transfer protocol secure) protects data.\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Sécurité réseau'\n---\n"
                "HTTPS (hypertext transfer protocol secure) protège les données.\n",
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
        self.assertIn("copied_english_acronym_expansion", stdout.getvalue())

    def test_english_dominant_title_blocks_only_when_different_from_source(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "payment-cards"
            bundle.mkdir()
            csv_path = Path(temporary_directory) / "findings.csv"
            cases = (
                (
                    "Protecting Payment Cards",
                    "Protect Your Data Now",
                    1,
                    "high_confidence_english_title",
                ),
                (
                    "Choosing a Server Platform",
                    "Comparaison des plateformes serveur modernes pour les petites entreprises: "
                    "Which Option is Right for Your Business?",
                    1,
                    "high_confidence_english_title",
                ),
                (
                    "The Legend of Zelda: A Link to the Past",
                    "The Legend of Zelda: A Link to the Past",
                    0,
                    "english_dominant_title_review",
                ),
            )
            for source_title, target_title, expected_result, expected_reason in cases:
                with self.subTest(target_title=target_title):
                    (bundle / "index.en.md").write_text(
                        f"---\ntitle: '{source_title}'\n---\n"
                        "The source explains practical ways to protect payment card data.\n",
                        encoding="utf-8",
                    )
                    (bundle / "index.fr.md").write_text(
                        f"---\ntitle: '{target_title}'\n---\n"
                        "Ce guide présente des moyens pratiques de protéger les données.\n",
                        encoding="utf-8",
                    )
                    stdout = io.StringIO()
                    with (
                        patch(
                            "check_translation_english_leakage.configured_locales",
                            return_value=["fr"],
                        ),
                        patch.object(
                            sys,
                            "argv",
                            [
                                "checker",
                                "--fail-on-english-fallback",
                                "--csv",
                                str(csv_path),
                                str(bundle),
                            ],
                        ),
                        redirect_stdout(stdout),
                    ):
                        result = checker_main()
                    self.assertEqual(result, expected_result)
                    with csv_path.open(newline="", encoding="utf-8") as report:
                        rows = list(csv.DictReader(report))
                    row = next(row for row in rows if row["locale"] == "fr")
                    self.assertIn(expected_reason, row["reasons"])
                    field = (
                        "english_dominant_title_review"
                        if expected_reason == "english_dominant_title_review"
                        else "english_dominant_title"
                    )
                    self.assertEqual(row[field], target_title)

    def test_queues_retained_english_vs_comparator_for_title_review(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "networking"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Ubiquiti Unifi vs TP-Link Omada'\n---\n"
                "The source compares two networking systems and their features.\n",
                encoding="utf-8",
            )
            (bundle / "index.pt.md").write_text(
                "---\ntitle: 'Ubiquiti Unifi vs TP-Link Omada: qual sistema escolher?'\n---\n"
                "Este artigo compara dois sistemas de rede e seus recursos.\n",
                encoding="utf-8",
            )
            csv_path = Path(temporary_directory) / "findings.csv"
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["pt"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", "--csv", str(csv_path), str(bundle)]),
                redirect_stdout(io.StringIO()),
            ):
                result = checker_main()
            self.assertEqual(result, 0)
            with csv_path.open(newline="", encoding="utf-8") as report:
                row = next(csv.DictReader(report))
            self.assertIn("copied_english_title_comparator", row["reasons"])

    def test_does_not_treat_vs_code_product_name_as_a_comparator(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "vscode-extensions"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Best VS Code Extensions for C++ Development'\n---\n"
                "The source describes useful extensions for C++ developers.\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Meilleures extensions VS Code pour le développement C++'\n---\n"
                "Cet article présente des extensions utiles pour les développeurs C++.\n",
                encoding="utf-8",
            )
            csv_path = Path(temporary_directory) / "findings.csv"
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", "--csv", str(csv_path), str(bundle)]),
                redirect_stdout(io.StringIO()),
            ):
                result = checker_main()
            self.assertEqual(result, 0)
            with csv_path.open(newline="", encoding="utf-8") as report:
                rows = list(csv.DictReader(report))
            self.assertEqual(rows, [])

    def test_blocks_one_copied_english_prose_paragraph_inside_a_translation(self):
        source = (
            "Une phrase française explique le contexte localisé et le traitement initial.\n\n"
            "Administrators review each access request before granting permission to protected records. "
            "The system records the decision and alerts the responsible owner.\n"
        )
        target = (
            "Une phrase française explique le contexte localisé et le traitement initial.\n\n"
            "Administrators review each access request before granting permission to protected records. "
            "The system records the decision and alerts the responsible owner.\n"
        )

        findings = copied_english_prose_paragraphs(source, target)

        self.assertEqual(len(findings), 1)
        self.assertIn("administrators review each access request", findings[0])

    def test_checks_list_items_and_linked_prose_but_ignores_name_only_references(self):
        example = (
            "```text\n"
            "Administrators review each access request before granting permission to protected records and notify the assigned owner.\n"
            "```\n\n"
            "- Administrators review each access request before granting permission to protected records and notify the assigned owner.\n"
        )
        citation = "1. [A comprehensive guide to cybersecurity careers](https://example.com) published by Example Org."
        linked_instruction = "- Administrators review [each access request](https://example.com) before granting permission to protected records and notify the assigned owner."
        official_title = "- NIST SP 1270: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence"

        self.assertEqual(len(copied_english_prose_paragraphs(example, example)), 1)
        self.assertEqual(copied_english_prose_paragraphs(citation, citation), [])
        self.assertEqual(len(copied_english_prose_paragraphs(linked_instruction, linked_instruction)), 1)
        self.assertEqual(copied_english_prose_paragraphs(official_title, official_title), [])

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

    def test_flags_known_untranslated_generic_table_labels(self):
        for label in (
            "Model A",
            "Model B",
            "Model C",
            "Total certifications",
            "with fallback",
            "Plug-and-play",
            "Infrastructure as Code",
        ):
            with self.subTest(label=label):
                table = f"| {label} |\n| --- |\n"
                self.assertEqual(
                    copied_english_table_cells(table, table, "fr"),
                    [f"table 1, row 1, cell 1: {normalize(label)}"],
                )

    def test_ignores_localized_versions_of_generic_table_labels(self):
        source = (
            "| Model A | Total certifications | with fallback |\n"
            "| --- | --- | --- |\n"
        )
        for target in (
            "| Modelo A | Nombre total de certifications | Claude Opus 5.5, max（フォールバックあり） |\n"
            "| --- | --- | --- |\n",
        ):
            with self.subTest(target=target):
                self.assertEqual(copied_english_table_cells(source, target, "fr"), [])

    def test_flags_short_project_and_responsive_assistant_table_labels(self):
        self.assertEqual(
            copied_english_table_cells("| Short project |\n| --- |\n", "| Short project |\n| --- |\n"),
            ["table 1, row 1, cell 1: short project"],
        )
        self.assertEqual(
            copied_english_table_cells("| Responsive assistant |\n| --- |\n", "| Responsive assistant |\n| --- |\n"),
            ["table 1, row 1, cell 1: responsive assistant"],
        )

    def test_accepts_cost_as_a_shared_catalan_and_romanian_table_word(self):
        table = "| Cost |\n| --- |\n"
        self.assertEqual(copied_english_table_cells(table, table, "ca"), [])
        self.assertEqual(copied_english_table_cells(table, table, "ro"), [])
        self.assertEqual(
            copied_english_table_cells(
                "| Cost per user |\n| --- |\n",
                "| Cost per user |\n| --- |\n",
                "ca",
            ),
            ["table 1, row 1, cell 1: cost per user"],
        )

    def test_accepts_exact_fixed_product_names_in_table_cells(self):
        for name in (
            "Server 2019",
            "Azure",
            "Defender for Cloud",
            "PCI DSS Level 1",
            "SQL Database, Database for MySQL/PostgreSQL",
            "Cache for Redis",
            "Speech-to-Text, Text-to-Speech",
            "Database for PostgreSQL",
            "Migrate for Compute Engine",
            "N/A",
            "N/A (BigQuery, Dataplex)",
        ):
            with self.subTest(name=name):
                table = f"| {name} |\n| --- |\n"
                self.assertEqual(copied_english_table_cells(table, table, "de"), [])
        performance = "| Performance |\n| --- |\n"
        self.assertEqual(copied_english_table_cells(performance, performance, "fr"), [])

    def test_flags_a_as_a_generic_table_cell(self):
        endpoint = "| A |\n| --- |\n"
        self.assertEqual(
            copied_english_table_cells(endpoint, endpoint, "bn"),
            ["table 1, row 1, cell 1: a"],
        )

    def test_accepts_openrouter_endpoint_ids_only_in_their_table_context(self):
        source = (
            "| Illustrative endpoint | Input price | Output price |\n"
            "| --- | ---: | ---: |\n"
            "| **A** | $0.03 | $16.00 |\n"
            "| **B** | $0.42 | $1.32 |\n"
        )
        translated = (
            "| Punto final ilustrativo | Precio de entrada | Precio de salida |\n"
            "| --- | ---: | ---: |\n"
            "| **A** | $0.03 | $16.00 |\n"
            "| **B** | $0.42 | $1.32 |\n"
        )

        self.assertEqual(copied_english_table_cells(source, translated, "es"), [])

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

    def test_high_confidence_gate_flags_a_single_english_reader_paragraph(self):
        english = (
            "Administrators review each access request before granting permission to protected records. "
            "The system records every decision and alerts the responsible owner."
        )
        self.assertEqual(high_confidence_english_paragraphs(english, "fr"), [normalize(english)])

    def test_high_confidence_gate_ignores_target_script_with_technical_names(self):
        chinese = (
            "管理員會檢查每個 access request，再授予受保護資料的權限。"
            "系統會記錄決策並通知負責人。"
        )
        self.assertEqual(high_confidence_english_paragraphs(chinese, "zh"), [])

    def test_high_confidence_gate_ignores_title_cased_reference_entries(self):
        citation = (
            "- National Institute of Standards and Technology (NIST). (2017). "
            "NIST Special Publication 800-37: Risk Management Framework for "
            "Information Systems and Organizations: A System Life Cycle Approach."
        )
        self.assertEqual(high_confidence_english_paragraphs(citation, "fr"), [])

    def test_high_confidence_gate_skips_localized_reference_sections(self):
        references = (
            "## Références\n\n"
            "- [What Is Machine Learning?](https://example.com/ml)\n"
            "- National Institute of Standards and Technology (NIST). (2017). "
            "NIST Special Publication 800-37: Risk Management Framework for "
            "Information Systems and Organizations."
        )
        self.assertEqual(high_confidence_english_paragraphs(references, "fr"), [])

    def test_high_confidence_gate_skips_more_localized_reference_sections(self):
        for heading in (
            "参考資料",
            "Referințe",
            "Referències",
            "Bibliografía",
            "Referências Bibliográficas",
            "Fontes bibliográficas",
        ):
            with self.subTest(heading=heading):
                references = (
                    f"## {heading}\n"
                    "- National Institute of Standards and Technology (NIST). (2017). "
                    "NIST Special Publication 800-37: Risk Management Framework for "
                    "Information Systems and Organizations. Retrieved from https://example.com"
                )
                self.assertEqual(high_confidence_english_paragraphs(references, "fr"), [])

    def test_reference_architecture_is_not_mistaken_for_a_bibliography(self):
        text = (
            "## Reference Architecture\n\n"
            "Administrators review each access request before granting permission "
            "to protected records. The system records the decision and alerts the owner."
        )
        self.assertEqual(len(high_confidence_english_paragraphs(text, "fr")), 1)

    def test_bibliography_heading_does_not_hide_preceding_english_prose(self):
        text = (
            "Administrators review each access request before granting permission "
            "to protected records. The system records the decision and alerts the owner.\n"
            "## Referințe\n"
            "- National Institute of Standards and Technology (NIST). (2017). "
            "NIST Special Publication 800-37: Risk Management Framework."
        )
        self.assertEqual(len(high_confidence_english_paragraphs(text, "ro")), 1)

    def test_high_confidence_gate_ignores_table_rows(self):
        table = (
            "| Method | Average throughput at 6 GHz 1,485 Mbps at 15 feet | Average throughput at 5 GHz 780 Mbps |\n"
            "| --- | --- | --- |\n"
            "| Test result | Average latency at 15 ms | Network performance remains stable |"
        )
        self.assertEqual(high_confidence_english_paragraphs(table, "it"), [])

    def test_high_confidence_gate_counts_accented_latin_words(self):
        romanian = (
            "Aplicația a validat lista, a extras datele, a procesat cererile, "
            "a păstrat rezultatele, a salvat raportul pentru administrator."
        )
        self.assertEqual(high_confidence_english_paragraphs(romanian, "ro"), [])

    def test_high_confidence_gate_strips_link_labels_but_keeps_english_sentence(self):
        mixed = (
            "- Elija [**StartMail**](https://example.com/) if you seek a user-friendly interface, "
            "custom domain integration, and support for PFS encryption."
        )
        found = high_confidence_english_paragraphs(mixed, "es")
        self.assertEqual(len(found), 1)
        self.assertIn("if you seek a user friendly interface", found[0])

    def test_flags_a_copied_english_reader_verb_inside_localized_prose(self):
        source = (
            "StartMail offers PFS protection, which means each email session uses a unique key."
        )
        target = (
            "[StartMail](https://example.com/) offers **PFS (Perfect Forward Secrecy)**, "
            "lo que significa que cada sesión utiliza una clave única."
        )
        self.assertEqual(len(copied_english_reader_verbs(source, target)), 1)
        self.assertIn("offers:", copied_english_reader_verbs(source, target)[0])

    def test_does_not_flag_spanish_subjunctive_uses_as_an_english_reader_verb(self):
        source = "The camera uses a visible status light during recording."
        target = "Para proteger la privacidad de todos, no lo uses cerca de otras personas."
        self.assertEqual(copied_english_reader_verbs(source, target, "es"), [])

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

    def test_strict_gate_blocks_copied_product_comparison_opening(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            opening = "**Azure DevOps vs GitHub vs GitLab vs Bitbucket**"
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Azure DevOps vs GitHub vs GitLab vs Bitbucket'\n---\n"
                f"{opening}\n\nThis is the English source paragraph for the comparison.\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Azure DevOps vs GitHub vs GitLab vs Bitbucket'\n---\n"
                f"{opening}\n\nCette analyse compare les plateformes selon vos besoins.\n",
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
        self.assertIn("copied_english_opening", stdout.getvalue())
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

    def test_strict_gate_blocks_a_single_copied_english_prose_paragraph(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            translated = "Le système examine chaque demande avant de modifier les accès."
            english = (
                "Administrators review each access request before granting permission to protected records. "
                "The system records the decision and alerts the responsible owner."
            )
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Access review'\n---\n" + translated + "\n\n" + english + "\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Vérification des accès'\n---\n" + translated + "\n\n" + english + "\n",
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
        self.assertIn("copied_english_prose_paragraph", stdout.getvalue())

    def test_strict_gate_blocks_missing_source_headings(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Access review'\n---\n## Introduction\n\n"
                "The source explains a complete access review process.\n\n"
                "## Corrective action\n\nThe source describes how to correct the record.\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Vérification des accès'\n---\n## Introduction\n\n"
                "Le texte présente le processus complet de vérification des accès.\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", str(bundle)],
                ),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("markdown_heading_levels_mismatch", stdout.getvalue())

    def test_strict_gate_blocks_one_paraphrased_english_paragraph_in_a_translation(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Review access'\n---\n"
                "The original English source describes a different access process with separate controls.\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Vérifier les accès'\n---\n"
                "Le système examine chaque demande avant d'accorder un accès limité aux dossiers.\n\n"
                "Administrators check every access request before they grant permission to sensitive records. "
                "The platform logs each decision and alerts the designated owner.\n",
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
        self.assertIn("high_confidence_english_paragraph", stdout.getvalue())
        self.assertIn(str(bundle / "index.fr.md"), stdout.getvalue())

    def test_strict_gate_blocks_one_english_verb_inside_localized_paragraph(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Secure email'\n---\n"
                "StartMail offers PFS protection, which means each email session uses a unique key.\n",
                encoding="utf-8",
            )
            (bundle / "index.es.md").write_text(
                "---\ntitle: 'Correo seguro'\n---\n"
                "StartMail offers **PFS (Perfect Forward Secrecy)**, lo que significa que cada sesión "
                "utiliza una clave única.\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["es"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("copied_english_reader_verb", stdout.getvalue())

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

    def test_markdown_structure_accepts_localized_fragments_for_aligned_headings(self):
        source = (
            "## Step-by-Step Setup Instructions\n\n"
            "See the [setup section](#step-by-step-setup-instructions).\n"
        )
        translated = (
            "## Instrucciones de configuración paso a paso\n\n"
            "Consulta la [sección de configuración](#instrucciones-de-configuración-paso-a-paso).\n"
        )
        broken = translated.replace(
            "#instrucciones-de-configuración-paso-a-paso", "#other-section"
        )

        self.assertEqual(markdown_structure_differences(source, translated), {})
        self.assertIn("link_targets", markdown_structure_differences(source, broken))

    def test_localized_fragment_match_rejects_changed_path_query_and_wrong_heading(self):
        source = (
            "## Step-by-Step Setup Instructions\n\n"
            "## Troubleshooting\n\n"
            "See [setup](guide.md?view=full#step-by-step-setup-instructions).\n"
        )
        translated = (
            "## Instrucciones de configuración paso a paso\n\n"
            "## Solución de problemas\n\n"
            "Consulta [la configuración](guide.md?view=full#instrucciones-de-configuración-paso-a-paso).\n"
        )
        changed_path = translated.replace("guide.md?view=full", "other.md?view=full")
        changed_query = translated.replace("view=full", "view=compact")
        wrong_existing_heading = translated.replace(
            "#instrucciones-de-configuración-paso-a-paso", "#solución-de-problemas"
        )

        for altered in (changed_path, changed_query, wrong_existing_heading):
            with self.subTest(target=altered.splitlines()[-1]):
                self.assertIn("link_targets", markdown_structure_differences(source, altered))

    def test_localized_fragment_match_rejects_cross_page_relative_links(self):
        source = "## Setup\n\nSee [the guide](guide.md#setup).\n"
        translated = "## Configuración\n\nConsulta [la guía](guide.md#configuración).\n"

        self.assertIn("link_targets", markdown_structure_differences(source, translated))

    def test_hugo_github_heading_ids_drop_combining_script_marks(self):
        source = "## Step-by-Step Setup Instructions"
        translated = "## ধাপে ধাপে সেটআপ নির্দেশাবলী"

        self.assertEqual(hugo_github_heading_ids(source), [("step-by-step-setup-instructions", False)])
        self.assertEqual(hugo_github_heading_ids(translated), [("ধপ-ধপ-সটআপ-নরদশবল", False)])

    def test_hugo_github_heading_ids_suffix_duplicate_headings(self):
        self.assertEqual(
            hugo_github_heading_ids("## Overview\n\n## Overview"),
            [("overview", False), ("overview-1", False)],
        )

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

    def test_identifies_unchanged_generic_english_taxonomy_labels(self):
        source = {
            "genre": ["Data Privacy", "Cloud Computing", "Python Security"],
            "tags": ["ad-blocking", "cross-platform", "Python interpreter", "internet privacy", "open-source", "FISMA"],
        }
        target = {
            "genre": ["Data Privacy", "Cloud Computing", "Sicherheit für Python"],
            "tags": ["ad-blocking", "cross-platform", "Python interpreter", "internet privacy", "open-source", "FISMA"],
        }

        self.assertEqual(
            copied_generic_english_taxonomy(source, target),
            {
                "genre": ["Cloud Computing", "Data Privacy"],
                "tags": ["Python interpreter", "ad-blocking", "cross-platform", "internet privacy", "open-source"],
            },
        )
        self.assertEqual(
            copied_generic_english_taxonomy(source, target, "de"),
            {
                "genre": ["Data Privacy"],
                "tags": ["ad-blocking", "cross-platform", "internet privacy", "open-source"],
            },
        )
        self.assertEqual(
            copied_generic_english_taxonomy(source, target, "nl"),
            {
                "genre": ["Cloud Computing", "Data Privacy"],
                "tags": ["ad-blocking", "cross-platform", "internet privacy", "open-source"],
            },
        )
        self.assertEqual(
            copied_generic_english_taxonomy(source, target, "fr"),
            {
                "genre": ["Cloud Computing", "Data Privacy"],
                "tags": [
                    "Python interpreter",
                    "ad-blocking",
                    "cross-platform",
                    "internet privacy",
                    "open-source",
                ],
            },
        )

    def test_cloud_computing_is_an_accepted_taxonomy_loanword_in_de_it_ro(self):
        self.assertEqual(
            copied_generic_english_taxonomy(
                {"genre": ["Cloud Computing"]},
                {"genre": ["Cloud-Computing"]},
                "de",
            ),
            {},
        )
        for locale in ("it", "ro"):
            self.assertEqual(
                copied_generic_english_taxonomy(
                    {"tags": ["cloud computing"]},
                    {"tags": ["cloud computing"]},
                    locale,
                ),
                {},
            )

    def test_strict_gate_blocks_unchanged_generic_english_taxonomy(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "browser-guide"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                '---\ntitle: "Browser privacy guide"\ntags: ["ad-blocking", "open-source"]\n---\n'
                "This article explains how browser extensions block advertising and protect privacy.\n",
                encoding="utf-8",
            )
            (bundle / "index.nl.md").write_text(
                '---\ntitle: "Gids voor browserprivacy"\ntags: ["ad-blocking", "open-source"]\n---\n'
                "Dit artikel legt uit hoe browserextensies advertenties blokkeren en privacy beschermen.\n",
                encoding="utf-8",
            )
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["nl"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", str(bundle)],
                ),
                redirect_stdout(io.StringIO()),
            ):
                result = checker_main()

        self.assertEqual(result, 1)

    def test_strict_gate_accepts_localized_python_interpreter_loanword(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "python-guide"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                '---\ntitle: "Python security guide"\ntags: ["python interpreter"]\n---\n'
                "This article explains how to secure Python applications and their data.\n",
                encoding="utf-8",
            )
            (bundle / "index.de.md").write_text(
                '---\ntitle: "Leitfaden zur Python-Sicherheit"\ntags: ["Python-Interpreter"]\n---\n'
                "Dieser Artikel erklärt, wie Sie Python-Anwendungen und ihre Daten schützen.\n",
                encoding="utf-8",
            )
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["de"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", str(bundle)],
                ),
                redirect_stdout(io.StringIO()),
            ):
                result = checker_main()

        self.assertEqual(result, 0)

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

    def test_blocks_an_unchanged_english_acronym_expansion(self):
        source = "- **BaaS**: Backend as a Service\n"
        unchanged = "- **BaaS**: Backend as a Service\n"
        localized = "- **BaaS**: バックエンド・アズ・ア・サービス\n"
        bilingual = "- **BaaS**: Backend as a Service (バックエンド・アズ・ア・サービス)\n"

        self.assertEqual(
            copied_english_acronym_expansions(source, unchanged),
            ["BaaS: backend as a service"],
        )
        self.assertEqual(copied_english_acronym_expansions(source, localized), [])
        self.assertEqual(copied_english_acronym_expansions(source, bilingual, "ja"), [])

    def test_blocks_unchanged_acronym_expansions_without_english_stopwords(self):
        for expansion in ("Application Programming Interface", "Transport Layer Security"):
            with self.subTest(expansion=expansion):
                entry = f"- **API**: {expansion}\n"
                self.assertEqual(
                    copied_english_acronym_expansions(entry, entry),
                    [f"API: {normalize(expansion)}"],
                )

    def test_does_not_block_a_single_word_shared_technical_term(self):
        source = "- **AV**: Antivirus\n"
        self.assertEqual(copied_english_acronym_expansions(source, source), [])

    def test_acronym_checks_accept_fullwidth_colon_in_translations(self):
        source = "- **API**: Application Programming Interface\n"
        unchanged_english = "- **API**：Application Programming Interface\n"
        localized = "- **API**：应用程序编程接口\n"
        self.assertEqual(
            copied_english_acronym_expansions(source, unchanged_english),
            ["API: application programming interface"],
        )
        self.assertEqual(copied_english_acronym_expansions(source, localized), [])
        self.assertEqual(missing_acronym_keys(source, localized), [])

    def test_checks_duplicate_acronym_keys_independently(self):
        source = (
            "- **DOS**: Disk Operating System\n"
            "- **DOS**: Denial of Service\n"
        )
        target = (
            "- **DOS**: Sistema Operativo de Disco\n"
            "- **DOS**: Denial of Service\n"
        )
        self.assertEqual(
            copied_english_acronym_expansions(source, target),
            ["DOS: denial of service"],
        )

    def test_does_not_treat_title_case_glossary_labels_as_acronym_keys(self):
        for key in (
            "Annual Plan",
            "Enhanced Search",
            "Cold Turkey",
            "Calendar Integration",
            "Professional Appearance",
        ):
            with self.subTest(key=key):
                self.assertFalse(fixed_glossary_key(key))

    def test_recognizes_common_mixed_case_acronym_keys(self):
        for key in ("DDoS", "BaaS", "ProtonMail", "IPv6"):
            with self.subTest(key=key):
                self.assertTrue(fixed_glossary_key(key))

    def test_recognizes_spaced_and_lowercase_fixed_glossary_keys(self):
        for key in ("AWS CLI", "iOS", "eSIM"):
            with self.subTest(key=key):
                self.assertTrue(fixed_glossary_key(key))

    def test_detects_nonstandard_acronym_and_technical_term_keys(self):
        for key, expansion in (
            ("CI/CD", "Continuous Integration and Continuous Delivery"),
            ("DDoS", "Distributed Denial of Service"),
            ("QR Code", "Quick Response Code"),
            ("Qubit", "Quantum Bit"),
        ):
            with self.subTest(key=key):
                entry = f"- **{key}**: {expansion}\n"
                self.assertEqual(
                    copied_english_acronym_expansions(entry, entry),
                    [f"{key}: {normalize(expansion)}"],
                )

    def test_flags_a_partially_untranslated_multiword_expansion(self):
        source = "- **OTP**: One-Time Password or One-Time Pad\n"
        partial = "- **OTP**: Contraseña de un solo uso o One-Time Pad\n"
        bilingual = (
            "- **OTP**: Contraseña de un solo uso o cifrado de un solo uso "
            "(One-Time Password or One-Time Pad)\n"
        )
        self.assertEqual(
            copied_english_acronym_expansions(source, partial),
            ["OTP: copied phrase one time pad"],
        )
        self.assertEqual(copied_english_acronym_expansions(source, bilingual), [])

    def test_flags_full_english_expansion_with_only_one_localized_word(self):
        source = "- **BaaS**: Backend as a Service\n"
        for locale, partial in (
            ("zh", "- **BaaS**: Backend as a Service 服务\n"),
            ("es", "- **BaaS**: Backend as a Service prestación\n"),
            ("pl", "- **BaaS**: Backend as a Service zażółć\n"),
        ):
            with self.subTest(locale=locale, partial=partial):
                self.assertEqual(
                    copied_english_acronym_expansions(source, partial, locale),
                    ["BaaS: copied phrase backend as a service"],
                )

    def test_cjk_bilingual_expansion_needs_a_substantial_target_script_phrase(self):
        source = "- **BaaS**: Backend as a Service\n"
        short = "- **BaaS**: Backend as a Service サービス\n"
        translated = "- **BaaS**: Backend as a Service バックエンド・アズ・ア・サービス\n"
        short_bilingual = "- **BaaS**: サービス（Backend as a Service）\n"
        translated_bilingual = (
            "- **BaaS**: バックエンド・アズ・ア・サービス（Backend as a Service）\n"
        )
        self.assertEqual(
            copied_english_acronym_expansions(source, short, "ja"),
            ["BaaS: copied phrase backend as a service"],
        )
        self.assertEqual(
            copied_english_acronym_expansions(source, translated, "ja"),
            [],
        )
        self.assertEqual(
            copied_english_acronym_expansions(source, short_bilingual, "ja"),
            ["BaaS: copied phrase backend as a service"],
        )
        self.assertEqual(
            copied_english_acronym_expansions(source, translated_bilingual, "ja"),
            [],
        )

    def test_latin_bilingual_expansion_needs_two_localized_words(self):
        source = "- **BaaS**: Backend as a Service\n"
        short = "- **BaaS**: servicio (Backend as a Service)\n"
        translated = "- **BaaS**: servicio de alojamiento (Backend as a Service)\n"
        self.assertEqual(
            copied_english_acronym_expansions(source, short, "es"),
            ["BaaS: copied phrase backend as a service"],
        )
        self.assertEqual(
            copied_english_acronym_expansions(source, translated, "es"),
            [],
        )

    def test_repeating_a_multiword_acronym_key_does_not_count_as_translation(self):
        fixtures = (
            (
                "- **AWS CLI**: Command Line Interface\n",
                "- **AWS CLI**: AWS CLI (Amazon Web Services Command Line Interface)\n",
                "AWS CLI: copied phrase command line interface",
            ),
            (
                "- **CI/CD**: Continuous Integration and Continuous Deployment\n",
                "- **CI/CD**: CI/CD (Continuous Integration and Continuous Deployment)\n",
                "CI/CD: copied phrase continuous integration and continuous deployment",
            ),
        )
        for source, target, expected in fixtures:
            with self.subTest(key=source.split("**")[1]):
                self.assertEqual(
                    copied_english_acronym_expansions(source, target, "es"),
                    [expected],
                )

    def test_flags_partial_content_phrases_without_stopwords(self):
        ssl_source = "- **SSL**: Secure Sockets Layer\n"
        ssl_target = "- **SSL**: Capa de Secure Sockets\n"
        cicd_source = "- **CI/CD**: Continuous Integration and Continuous Deployment\n"
        cicd_target = "- **CI/CD**: Integración continua/continuous integration\n"
        api_source = "- **API**: Application Programming Interface\n"
        api_target = "- **API**: Interfaz de Application Programming\n"
        tls_source = "- **TLS**: Transport Layer Security\n"
        tls_target = "- **TLS**: Seguridad de Transport Layer\n"
        access_source = "- **ACL**: Access Control List\n"
        access_target = "- **ACL**: Control de Access\n"
        self.assertEqual(
            copied_english_acronym_expansions(ssl_source, ssl_target),
            ["SSL: copied phrase secure sockets"],
        )
        self.assertEqual(
            copied_english_acronym_expansions(cicd_source, cicd_target),
            ["CI/CD: copied phrase continuous integration"],
        )
        self.assertEqual(
            copied_english_acronym_expansions(api_source, api_target),
            ["API: copied phrase application programming"],
        )
        self.assertEqual(
            copied_english_acronym_expansions(tls_source, tls_target),
            ["TLS: copied phrase transport layer"],
        )
        self.assertEqual(
            copied_english_acronym_expansions(access_source, access_target),
            ["ACL: copied phrase access control"],
        )

    def test_non_latin_characters_do_not_excuse_an_english_expansion(self):
        source = "- **BaaS**: Backend as a Service\n"
        mostly_english = "- **BaaS**: Backend as a Service 服务\n"
        localized = "- **BaaS**: Backend as a Service 服务平台扩展内容\n"
        self.assertEqual(
            copied_english_acronym_expansions(source, mostly_english, "zh"),
            ["BaaS: copied phrase backend as a service"],
        )
        self.assertEqual(copied_english_acronym_expansions(source, localized, "zh"), [])

    def test_partial_expansion_screen_ignores_brand_names_and_version_labels(self):
        aws_source = "- **AWS CLI**: Amazon Web Services Command Line Interface\n"
        aws_target = "- **AWS CLI**: Interfaz de línea de comandos de Amazon Web Services\n"
        html_source = "- **HTML5**: HyperText Markup Language, version 5\n"
        html_target = "- **HTML5**: Langue de balisage hypertexte, version 5\n"
        bps_source = "- **BPS**: Bits Per Second\n"
        bps_target = "- **BPS**: bits per seconde\n"
        kbe_source = "- **KbE**: Kilobits Per Second\n"
        kbe_target = "- **KbE**: kilobits per seconde\n"
        self.assertEqual(copied_english_acronym_expansions(aws_source, aws_target), [])
        self.assertEqual(copied_english_acronym_expansions(html_source, html_target), [])
        self.assertEqual(
            copied_english_acronym_expansions(bps_source, bps_target, "nl"), []
        )
        self.assertEqual(
            copied_english_acronym_expansions(kbe_source, kbe_target, "nl"), []
        )

    def test_does_not_flag_an_unchanged_brand_name_as_a_glossary_expansion(self):
        entry = "- **Android**: Tor Browser for Android\n"
        self.assertEqual(copied_english_acronym_expansions(entry, entry), [])

    def test_scans_glossary_entries_with_fullwidth_colons(self):
        source = "- **API**: Application Programming Interface\n"
        target = "- **API**：Application Programming Interface\n"
        self.assertEqual(
            copied_english_acronym_expansions(source, target),
            ["API: application programming interface"],
        )
        self.assertEqual(missing_acronym_keys(source, target), [])

    def test_blocks_translating_or_omitting_a_fixed_acronym_key(self):
        source = "- **GIS**: Geographic Information System\n" + "".join(
            f"- **AA{index}**: Definition {index}\n" for index in range(19)
        )
        target = "- **SIG**: Système d'information géographique\n" + "".join(
            f"- **AA{index}**: Définition localisée {index}\n" for index in range(19)
        )
        self.assertEqual(missing_acronym_keys(source, target), ["GIS"])

    def test_fixed_key_check_covers_short_glossaries(self):
        self.assertEqual(
            missing_acronym_keys(
                "- **GIS**: Geographic Information System\n",
                "- **SIG**: Système d’information géographique\n",
            ),
            ["GIS"],
        )

    def test_blocks_translating_a_fixed_qr_code_glossary_key(self):
        source = "- **QR Code**: Quick Response Code\n" + "".join(
            f"- **AA{index}**: Definition {index}\n" for index in range(19)
        )
        target = "- **QR ਕੋਡ**: ਤੁਰੰਤ ਜਵਾਬ ਕੋਡ\n" + "".join(
            f"- **AA{index}**: ਸਥਾਨਕ ਪਰਿਭਾਸ਼ਾ {index}\n" for index in range(19)
        )
        self.assertEqual(missing_acronym_keys(source, target), ["QR Code"])

    def test_short_article_bullet_lists_are_not_acronym_glossaries(self):
        source = "- **MFA**: Multi-Factor Authentication\n"
        target = "- **MFA**: ਮਲਟੀ-ਫੈਕਟਰ ਪ੍ਰਮਾਣਿਕਤਾ\n"
        self.assertEqual(missing_acronym_keys(source, target), [])

    def test_non_glossary_product_list_does_not_require_fixed_glossary_keys(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "secure-email-products"
            bundle.mkdir()
            keys = ["ProtonMail", "StartMail"] + [f"Tool{index}Name" for index in range(18)]
            source = "---\ntitle: 'Secure Email Services'\n---\n" + "".join(
                f"- **{key}**: Email service\n" for key in keys
            )
            target = "---\ntitle: 'E-Mail-Dienste'\n---\n" + "".join(
                f"- **{key}**: E-Mail-Dienst\n" for key in keys[2:]
            )
            source_path = bundle / "index.en.md"
            source_path.write_text(source, encoding="utf-8")
            (bundle / "index.de.md").write_text(target, encoding="utf-8")

            findings = audit_bundle(source_path, ["de"])

        self.assertFalse(
            any("missing_acronym_key" in row["reasons"] for row in findings)
        )

    def test_non_glossary_ci_cd_tool_list_is_not_checked_as_an_acronym_expansion(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "configuration-tools"
            bundle.mkdir()
            source_path = bundle / "index.en.md"
            source_path.write_text(
                "---\ntitle: 'Compare CI/CD Tools'\n---\n"
                "- **CI/CD**: Easily integrated with Jenkins, GitLab CI, and GitHub Actions.\n",
                encoding="utf-8",
            )
            (bundle / "index.es.md").write_text(
                "---\ntitle: 'Comparar herramientas de CI/CD'\n---\n"
                "- **CI/CD**: Se integra fácilmente con Jenkins, GitLab CI y GitHub Actions.\n",
                encoding="utf-8",
            )

            findings = audit_bundle(source_path, ["es"])

        self.assertFalse(
            any("copied_english_acronym_expansion" in row["reasons"] for row in findings)
        )

    def test_recognizes_fullwidth_colon_in_localized_glossary_entries(self):
        source = "- **ACL**: Access Control List\n"
        target = "- **ACL**：Access Control List\n"
        self.assertEqual(missing_acronym_keys(source, target), [])
        self.assertEqual(
            copied_english_acronym_expansions(source, target),
            ["ACL: access control list"],
        )

    def test_flags_unchanged_english_table_cells_after_row_or_column_reordering(self):
        source = (
            "| Método | Latency at 15 ms | Precio |\n"
            "| --- | --- | --- |\n"
            "| Modelo A | 20 ms | $99 |\n"
            "| Modelo B | 25 ms | $129 |\n"
        )
        target = (
            "| Precio | Método | Latency at 15 ms |\n"
            "| --- | --- | --- |\n"
            "| $129 | Modelo B | 25 ms |\n"
            "| $99 | Modelo A | 20 ms |\n"
        )
        findings = copied_english_table_cells(source, target)
        self.assertTrue(any("latency at 15 ms" in finding for finding in findings))

    def test_does_not_treat_a_platform_name_as_an_acronym(self):
        text = "- **Android**: Tor Browser for Android\n"
        self.assertEqual(copied_english_acronym_expansions(text, text), [])

    def test_strict_gate_blocks_an_unchanged_english_acronym_expansion(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Acronyms'\n---\n- **BaaS**: Backend as a Service\n",
                encoding="utf-8",
            )
            (bundle / "index.ja.md").write_text(
                "---\ntitle: '略語'\n---\n- **BaaS**: Backend as a Service\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["ja"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("copied_english_acronym_expansion", stdout.getvalue())

    def test_strict_gate_blocks_a_changed_fixed_acronym_key(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            source_glossary = "- **GIS**: Geographic Information System\n" + "".join(
                f"- **AA{index}**: Definition {index}\n" for index in range(19)
            )
            target_glossary = "- **SIG**: Système d’information géographique\n" + "".join(
                f"- **AA{index}**: Définition localisée {index}\n" for index in range(19)
            )
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Geographic information systems glossary'\n---\n"
                + source_glossary,
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Systèmes d’information géographique'\n---\n"
                + target_glossary,
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
        self.assertIn("missing_acronym_key", stdout.getvalue())

    def test_strict_gate_blocks_an_unchanged_english_table_cell(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            table = "| Method | Average latency per request |\n| --- | --- |\n"
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Compare methods'\n---\n" + table,
                encoding="utf-8",
            )
            (bundle / "index.de.md").write_text(
                "---\ntitle: 'Methoden vergleichen'\n---\n" + table,
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["de"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("English_reader_table_cell_copy", stdout.getvalue())

    def test_strict_gate_blocks_an_unchanged_shortcode_description(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            shortcode = (
                '{{< youtube id="abc" title="Official Video Title" '
                'description="Local and hosted models, memory requirements, and agent verification." >}}'
                '\n{{< figure caption="A descriptive network diagram" alt="Secure network icon" >}}'
            )
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Local models guide'\n---\n" + shortcode,
                encoding="utf-8",
            )
            (bundle / "index.de.md").write_text(
                "---\ntitle: 'Leitfaden für lokale Modelle'\n---\n" + shortcode,
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["de"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("copied_english_shortcode_description", stdout.getvalue())

    def test_strict_gate_blocks_missing_taxonomy_values(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'A guide to network security'\n"
                "tags: [network security, privacy tools, secure networks]\n---\n"
                "A useful guide for protecting your network and its data.\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Guide de sécurité réseau'\ntags: [sécurité réseau]\n---\n"
                "Un guide utile pour protéger votre réseau et ses données.\n",
                encoding="utf-8",
            )
            report = Path(temporary_directory) / "leakage.csv"
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", "--csv", str(report), str(bundle)],
                ),
                redirect_stdout(stdout),
            ):
                result = checker_main()
            report_text = report.read_text(encoding="utf-8")

        self.assertEqual(result, 1)
        self.assertIn("taxonomy_count_mismatch", report_text)
        self.assertIn("taxonomy_count_mismatch", stdout.getvalue())

    def test_strict_gate_blocks_missing_shortcode_structure(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Network guide'\n---\n"
                "## Setup\n\nA useful setup guide for your network.\n\n"
                '{{< figure src="network.webp" alt="A secure network diagram" >}}\n',
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Guide réseau'\n---\n"
                "## Configuration\n\nUn guide utile pour configurer votre réseau.\n",
                encoding="utf-8",
            )
            report = Path(temporary_directory) / "leakage.csv"
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["fr"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", "--csv", str(report), str(bundle)],
                ),
                redirect_stdout(stdout),
            ):
                result = checker_main()
            report_text = report.read_text(encoding="utf-8")

        self.assertEqual(result, 1)
        self.assertIn("markdown_shortcodes_mismatch", report_text)
        self.assertIn("markdown_shortcodes_mismatch", stdout.getvalue())

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

    def test_strict_gate_blocks_unchanged_generic_bibliography_link_label(self):
        source = "[Link](https://example.com/documentation)"
        target = "[Link](https://example.com/documentation)"
        self.assertEqual(
            copied_english_generic_link_labels(source, target, "fr"),
            ["Link => Link => https://example.com/documentation"],
        )
        self.assertEqual(
            copied_english_generic_link_labels(
                "[TLS RFC](https://tools.ietf.org/html/rfc5246)",
                "[TLS RFC](https://tools.ietf.org/html/rfc5246)",
                "ru",
            ),
            ["TLS RFC => TLS RFC => https://tools.ietf.org/html/rfc5246"],
        )
        self.assertEqual(
            copied_english_generic_link_labels(
                "[NIST - Role-Based Access Control](https://example.com/rbac)",
                "[NIST - Role-Based Access Control](https://example.com/rbac)",
                "de",
            ),
            [
                "NIST - Role-Based Access Control => NIST - Role-Based Access Control => "
                "https://example.com/rbac"
            ],
        )
        self.assertEqual(
            copied_english_generic_link_labels(
                "[OWASP RBAC Cheat Sheet](https://example.com/owasp)",
                "[OWASP RBAC Cheat Sheet](https://example.com/owasp)",
                "ja",
            ),
            [
                "OWASP RBAC Cheat Sheet => OWASP RBAC Cheat Sheet => "
                "https://example.com/owasp"
            ],
        )
        self.assertEqual(
            copied_english_generic_link_labels(
                "[Python website](https://www.python.org/downloads/)",
                "[Python-Website](https://www.python.org/downloads/)",
                "de",
            ),
            [],
        )
        copied_cloud_provider_labels = (
            "[Amazon Web Services (AWS) - Security](https://aws.example/security)\n"
            "[Microsoft Azure - Security and Compliance](https://azure.example/security)\n"
            "[Google Cloud Platform - Security](https://google.example/security)"
        )
        self.assertEqual(
            copied_english_generic_link_labels(
                copied_cloud_provider_labels,
                copied_cloud_provider_labels,
                "fr",
            ),
            [
                "Amazon Web Services (AWS) - Security => Amazon Web Services (AWS) - Security => "
                "https://aws.example/security",
                "Microsoft Azure - Security and Compliance => Microsoft Azure - Security and Compliance => "
                "https://azure.example/security",
                "Google Cloud Platform - Security => Google Cloud Platform - Security => "
                "https://google.example/security",
            ],
        )
        copied_chocolatey_labels = (
            "[Chocolatey documentation on Puppet integration](https://example.com/puppet)\n"
            "[Chocolatey module documentation for Ansible](https://example.com/ansible)\n"
            "[Chocolatey documentation on package creation](https://example.com/packages)\n"
            "[Chocolatey Official Website](https://chocolatey.org/)\n"
            "[Chocolatey Documentation](https://docs.chocolatey.org/)\n"
            "[NuGet Package Manager](https://www.nuget.org/)"
        )
        self.assertEqual(
            copied_english_generic_link_labels(
                copied_chocolatey_labels,
                copied_chocolatey_labels,
                "fr",
            ),
            [
                "Chocolatey documentation on Puppet integration => Chocolatey documentation on Puppet integration => "
                "https://example.com/puppet",
                "Chocolatey module documentation for Ansible => Chocolatey module documentation for Ansible => "
                "https://example.com/ansible",
                "Chocolatey documentation on package creation => Chocolatey documentation on package creation => "
                "https://example.com/packages",
                "Chocolatey Official Website => Chocolatey Official Website => https://chocolatey.org/",
                "Chocolatey Documentation => Chocolatey Documentation => https://docs.chocolatey.org/",
                "NuGet Package Manager => NuGet Package Manager => https://www.nuget.org/",
            ],
        )
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Security guide'\n---\n"
                "This article explains how to secure your software and protect data.\n\n"
                "[Link](https://example.com/documentation)\n"
                "[TLS RFC](https://tools.ietf.org/html/rfc5246)\n"
                "[Amazon Web Services (AWS) - Security](https://aws.example/security)\n"
                "[Microsoft Azure - Security and Compliance](https://azure.example/security)\n"
                "[Google Cloud Platform - Security](https://google.example/security)\n"
                + copied_chocolatey_labels
                + "\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Guide de sécurité'\n---\n"
                "Cet article explique comment sécuriser les logiciels et protéger les données.\n\n"
                "[Link](https://example.com/documentation)\n"
                "[TLS RFC](https://tools.ietf.org/html/rfc5246)\n"
                "[Amazon Web Services (AWS) - Security](https://aws.example/security)\n"
                "[Microsoft Azure - Security and Compliance](https://azure.example/security)\n"
                "[Google Cloud Platform - Security](https://google.example/security)\n"
                + copied_chocolatey_labels
                + "\n",
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
        self.assertIn("copied_english_generic_link_label", stdout.getvalue())

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

    def test_flags_unchanged_shortcode_descriptions_but_ignores_official_titles(self):
        source = (
            '{{< youtube id="abc" title="Official Video: Source Name" '
            'description="Local and hosted models, memory requirements, and agent verification." >}}'
        )
        unchanged = source
        localized = (
            '{{< youtube id="abc" title="Título oficial: Nombre" '
            'description="Modelos locais e hospedados, requisitos de memória e verificação de agentes." >}}'
        )

        self.assertEqual(
            copied_english_shortcode_descriptions(source, unchanged),
            ["youtube.description: Local and hosted models, memory requirements, and agent verification."],
        )
        self.assertEqual(copied_english_shortcode_descriptions(source, localized), [])

    def test_shortcode_reader_text_matches_attributes_independently_and_ignores_data_alt(self):
        source = (
            '{{< figure alt="Secure network icon" caption="A sample network diagram" >}}\n'
            '{{< figure alt="Another network illustration" >}}'
        )
        target = (
            '{{< figure caption="A sample network diagram" data-alt="Secure network icon" '
            'alt="Icono de red segura" >}}\n'
            '{{< figure alt="Another network illustration" >}}'
        )

        self.assertEqual(
            copied_english_shortcode_descriptions(source, target),
            [
                "figure.caption: A sample network diagram",
                "figure.alt: Another network illustration",
            ],
        )
        short_alt = '{{< figure alt="Secure network icon" >}}'
        self.assertEqual(
            copied_english_shortcode_descriptions(short_alt, short_alt),
            ["figure.alt: Secure network icon"],
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

    def test_internal_article_link_copy_blocks_when_sibling_title_is_localized(self):
        with TemporaryDirectory() as temporary_directory:
            articles = Path(temporary_directory) / "articles"
            sibling = articles / "compromised-email"
            sibling.mkdir(parents=True)
            (sibling / "index.de.md").write_text(
                "---\ntitle: 'Was tun bei kompromittierter E-Mail?'\n---\n", encoding="utf-8"
            )
            source = (
                "Read [the guide](https://simeononsecurity.com/articles/other-guide/) and "
                "[Enable two-factor authentication (2FA)]"
                "(https://simeononsecurity.com/articles/compromised-email/)."
            )
            target = (
                "Aktivieren Sie [Enable two-factor authentication]"
                "(https://simeononsecurity.com/articles/compromised-email/) und lesen Sie "
                "[die Anleitung](https://simeononsecurity.com/articles/other-guide/)."
            )

            with patch("check_translation_english_leakage.ARTICLES", articles):
                findings = copied_english_internal_link_labels(source, target, "de")

        self.assertEqual(len(findings), 1)
        self.assertIn("Enable two-factor authentication", findings[0])

    def test_strict_gate_blocks_copied_internal_link_label(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory).resolve()
            articles = root / "articles"
            sibling = articles / "compromised-email"
            sibling.mkdir(parents=True)
            (sibling / "index.de.md").write_text(
                "---\ntitle: 'Was tun bei kompromittierter E-Mail?'\n---\n", encoding="utf-8"
            )
            bundle = articles / "current-article"
            bundle.mkdir()
            url = "https://simeononsecurity.com/articles/compromised-email/"
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Email security'\n---\nSee [What to Do If You Think Your Email Is Compromised]"
                f"({url}).\n",
                encoding="utf-8",
            )
            (bundle / "index.de.md").write_text(
                "---\ntitle: 'E-Mail-Sicherheit'\n---\nLesen Sie "
                f"[What to Do If You Think Your Email Is Compromised]({url}).\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.ROOT", root),
                patch("check_translation_english_leakage.ARTICLES", articles),
                patch("check_translation_english_leakage.configured_locales", return_value=["de"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("copied_english_internal_link_label", stdout.getvalue())

    def test_internal_link_gate_does_not_attach_last_source_url_to_other_links(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            articles = root / "articles"
            sibling = articles / "strong-passwords"
            sibling.mkdir(parents=True)
            (sibling / "index.de.md").write_text(
                "---\ntitle: 'Starke Passwörter erstellen'\n---\n", encoding="utf-8"
            )
            source = (
                "[Norton Family](https://example.com/norton) and "
                "[Kaspersky Safe Kids](https://example.com/kaspersky). "
                "Read [strong passwords](https://simeononsecurity.com/articles/strong-passwords/)."
            )
            target = (
                "[Norton Family](https://example.com/norton) und "
                "[Kaspersky Safe Kids](https://example.com/kaspersky). "
                "Lesen Sie [starke Passwörter](https://simeononsecurity.com/articles/strong-passwords/)."
            )

            with patch("check_translation_english_leakage.ARTICLES", articles):
                findings = copied_english_internal_link_labels(source, target, "de")

        self.assertEqual(findings, [])

    def test_internal_link_gate_ignores_shared_brand_words_in_localized_label(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            articles = root / "articles"
            sibling = articles / "flock-finder"
            sibling.mkdir(parents=True)
            (sibling / "index.fr.md").write_text(
                "---\ntitle: 'Cartographier les caméras Flock Safety'\n---\n",
                encoding="utf-8",
            )
            source = (
                "Read [Flock Finder: Map Flock Safety ALPR Cameras]"
                "(https://simeononsecurity.com/articles/flock-finder/)."
            )
            target = (
                "Lisez [Flock Finder: Cartographier les caméras Flock Safety]"
                "(https://simeononsecurity.com/articles/flock-finder/)."
            )

            with patch("check_translation_english_leakage.ARTICLES", articles):
                findings = copied_english_internal_link_labels(source, target, "fr")

        self.assertEqual(findings, [])

    def test_flags_english_and_connector_between_linked_list_items(self):
        text = (
            "Algunos servicios incluyen [A](https://example.com/a), "
            "[B](https://example.com/b), and [C](https://example.com/c)."
        )

        self.assertEqual(
            copied_english_link_connectors(text),
            ["line 1: and before C"],
        )

    def test_flags_english_or_connector_between_linked_list_items(self):
        text = (
            "Choisissez [A](https://example.com/a), "
            "[B](https://example.com/b), or [C](https://example.com/c)."
        )

        self.assertEqual(
            copied_english_link_connectors(text),
            ["line 1: or before C"],
        )

    def test_ignores_english_and_connector_inside_code_or_single_link(self):
        text = (
            "[Session](https://example.com/session) and [Threema](https://example.com/threema).\n"
            "```text\n[A](https://example.com/a), [B](https://example.com/b), and "
            "[C](https://example.com/c)\n```\n"
            "[A](https://example.com/a), and [B](https://example.com/b)\n"
            "Sample syntax: `[A](https://example.com/a), [B](https://example.com/b), and "
            "[C](https://example.com/c)`.\n"
            "Multiline example: `preview\n[A](https://example.com/a), "
            "[B](https://example.com/b), and [C](https://example.com/c)\nend preview`."
        )

        self.assertEqual(copied_english_link_connectors(text), [])

    def test_strict_gate_blocks_english_link_list_connector(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Messaging services'\n---\n"
                "## Options\n\nCompare [A](https://example.com/a), "
                "[B](https://example.com/b), and [C](https://example.com/c).\n",
                encoding="utf-8",
            )
            (bundle / "index.es.md").write_text(
                "---\ntitle: 'Servicios de mensajería'\n---\n"
                "## Opciones\n\nCompara [A](https://example.com/a), "
                "[B](https://example.com/b), and [C](https://example.com/c).\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["es"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("strict blockers: 1", stdout.getvalue())
        self.assertIn("copied_english_link_connector", stdout.getvalue())
        self.assertNotIn("English_dominant_reader_body", stdout.getvalue())

    def test_strict_gate_blocks_copied_reader_code_comments(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Create a virtual network'\n---\n"
                "## Steps\n\nFollow the commands below to create a network.\n\n"
                "```azurecli\n# Create a virtual network and subnet\n"
                "az network vnet create --name MyVNet\n```\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Créer un réseau virtuel'\n---\n"
                "## Étapes\n\nSuivez les commandes ci-dessous pour créer un réseau.\n\n"
                "```azurecli\n# Create a virtual network and subnet\n"
                "az network vnet create --name MyVNet\n```\n",
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
        self.assertIn("English_reader_code_prose_fallback", stdout.getvalue())

    def test_strict_gate_blocks_copied_short_greeting_in_code_output(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Safe output encoding'\n---\n"
                "## Example\n\nEncode output before rendering it.\n\n"
                "```python\ndef greet():\n    return 'Hello, '\n```\n",
                encoding="utf-8",
            )
            (bundle / "index.es.md").write_text(
                "---\ntitle: 'Codificación de salida segura'\n---\n"
                "## Ejemplo\n\nCodifique la salida antes de mostrarla.\n\n"
                "```python\ndef greet():\n    return 'Hello, '\n```\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["es"]),
                patch.object(sys, "argv", ["checker", "--fail-on-english-fallback", str(bundle)]),
                redirect_stdout(stdout),
            ):
                result = checker_main()

        self.assertEqual(result, 1)
        self.assertIn("English_reader_code_prose_fallback", stdout.getvalue())

    def test_short_hi_output_stays_in_manual_review_queue(self):
        example = '```python\nprint("Hi")\n```\n'

        self.assertIn("hi", copied_reader_code_prose(example, example))
        self.assertNotIn("hi", english_reader_code_prose_fallback(example, example))

    def test_strict_gate_blocks_unchanged_reader_facing_formula_lines(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'KV cache estimate'\n---\n"
                "## Estimate\n\nThe calculation gives the bytes needed per token.\n\n"
                "```text\nFull-attention KV bytes per token:\n"
                "16 layers × 4 KV heads × 256 dimensions × 2 (K and V) × 2 bytes\n"
                "```\n",
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Estimation du cache KV'\n---\n"
                "## Estimation\n\nLe calcul donne les octets requis par jeton.\n\n"
                "```text\nOctets KV en attention complète par jeton :\n"
                "16 layers × 4 KV heads × 256 dimensions × 2 (K and V) × 2 bytes\n"
                "```\n",
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
            self.assertIn("copied_english_fenced_formula", stdout.getvalue())
            self.assertIn(
                "16 layers 4 kv heads 256 dimensions 2 k and v 2 bytes",
                copied_english_fenced_formulas(
                    (bundle / "index.en.md").read_text(encoding="utf-8"),
                    (bundle / "index.fr.md").read_text(encoding="utf-8"),
                ),
            )
            status_output = (
                "```text\nStatus: 200 records in 4 files, 16 events, and 2 errors.\n```"
            )
            self.assertEqual(copied_english_fenced_formulas(status_output, status_output), [])

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

    def test_screens_azurecli_comments_and_powershell_label_descriptions(self):
        source = (
            "```azurecli\n"
            "# Create a virtual network and subnet\n"
            "az network vnet create --name MyVNet\n"
            "```\n"
            "```powershell\n"
            '$LabelDescription = "This label applies encryption and an access policy for internal use only."\n'
            "```\n"
        )

        self.assertEqual(
            reader_fenced_code_prose(source),
            {
                "create a virtual network and subnet",
                "this label applies encryption and an access policy for internal use only",
            },
        )
        self.assertEqual(copied_reader_code_prose(source, source), reader_fenced_code_prose(source))
        self.assertEqual(
            english_reader_code_prose_fallback(source, source),
            [
                "create a virtual network and subnet",
                "this label applies encryption and an access policy for internal use only",
            ],
        )

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

    def test_screens_unchanged_english_yaml_sample_values(self):
        source = (
            "```yaml\n"
            "user_input: \"Hello! This is a string with non-alphanumeric characters.\"\n"
            "sanitized_input: \"{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}\"\n"
            "```"
        )
        localized = (
            "```yaml\n"
            "user_input: \"¡Hola! Esta es una cadena con caracteres no alfanuméricos.\"\n"
            "sanitized_input: \"{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}\"\n"
            "```"
        )
        expected = {"hello this is a string with non alphanumeric characters"}
        self.assertEqual(reader_fenced_code_prose(source), expected)
        self.assertEqual(copied_reader_code_prose(source, source), expected)
        self.assertEqual(copied_reader_code_prose(source, localized), set())
        self.assertEqual(english_reader_code_prose_fallback(source, source), sorted(expected))

    def test_strict_gate_blocks_unchanged_english_yaml_sample_value(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            en_body = (
                "## Example\n\nUse this sample input in the filter.\n\n"
                "```yaml\n"
                "user_input: \"Hello! This is a string with non-alphanumeric characters.\"\n"
                "sanitized_input: \"{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}\"\n"
                "```\n"
            )
            fr_body = (
                "## Exemple\n\nUtilisez cette entrée dans le filtre.\n\n"
                "```yaml\n"
                "user_input: \"Hello! This is a string with non-alphanumeric characters.\"\n"
                "sanitized_input: \"{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}\"\n"
                "```\n"
            )
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Input sanitization'\n---\n" + en_body,
                encoding="utf-8",
            )
            (bundle / "index.fr.md").write_text(
                "---\ntitle: 'Nettoyage des entrées'\n---\n" + fr_body,
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
        self.assertIn("English_reader_code_prose_fallback", stdout.getvalue())

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

    def test_finds_source_matched_english_phrases_in_bengali_prose(self):
        source = (
            "Required memory = resident weights + context cache + runtime allowance\n"
            "| Relevant context | Edits an unrelated file |"
        )
        target = (
            "প্রয়োজনীয় মেমরি = resident weights + context cache + runtime allowance\n"
            "| Relevant context | অসংশ্লিষ্ট ফাইল সম্পাদনা করে |"
        )

        findings = copied_english_mixed_phrases(source, target, "bn")
        self.assertIn("resident weights", findings)
        self.assertIn("context cache", findings)
        self.assertIn("runtime allowance", findings)
        self.assertIn("Relevant context", findings)
        self.assertEqual(copied_english_mixed_phrases(source, target, "fr"), [])

    def test_strict_gate_blocks_generic_technical_descriptors(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Network switch guide'\n---\n"
                "Required memory = resident weights + context cache + runtime allowance\n\n"
                "Omada ER7206 (Multi-Gigabit): $199\n\n"
                "Snyk - Open Source Security Platform\n",
                encoding="utf-8",
            )
            (bundle / "index.bn.md").write_text(
                "---\ntitle: 'নেটওয়ার্ক সুইচ নির্দেশিকা'\n---\n"
                "প্রয়োজনীয় মেমরি = resident weights + context cache + runtime allowance\n\n"
                "Omada ER7206 (Multi-Gigabit): $199\n\n"
                "Snyk - Open Source Security Platform\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            report = bundle.parent / "leakage.csv"
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["bn"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", "--csv", str(report), str(bundle)],
                ),
                redirect_stdout(stdout),
            ):
                result = checker_main()
            with report.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                report_fields = reader.fieldnames
                report_rows = list(reader)

        self.assertEqual(result, 1)
        self.assertIn("copied_english_generic_term", stdout.getvalue())
        self.assertIn("source-matched mixed-script phrase reviews:", stdout.getvalue())
        self.assertIn("copied_english_mixed_phrases", report_fields)
        self.assertIn("copied_english_generic_terms", report_fields)
        self.assertTrue(any("resident weights" in row["copied_english_mixed_phrases"] for row in report_rows))
        self.assertTrue(any("multi-gigabit" in row["copied_english_generic_terms"] for row in report_rows))
        self.assertTrue(
            any("open source security platform" in row["copied_english_generic_terms"] for row in report_rows)
        )

    def test_strict_gate_blocks_high_density_mixed_english_in_bengali(self):
        with TemporaryDirectory() as temporary_directory:
            bundle = Path(temporary_directory).resolve() / "candidate"
            bundle.mkdir()
            source_lines = [f"required item{index:03d}" for index in range(20)]
            source_lines.append(source_lines[0])
            source_body = "\n\n".join(source_lines)
            target_body = "\n\n".join(source_lines)
            self.assertEqual(
                len(copied_english_mixed_phrases(source_body, target_body, "bn")),
                20,
            )
            (bundle / "index.en.md").write_text(
                "---\ntitle: 'Memory planning guide'\n---\n" + source_body + "\n",
                encoding="utf-8",
            )
            (bundle / "index.bn.md").write_text(
                "---\ntitle: 'মেমরি পরিকল্পনা নির্দেশিকা'\n---\n"
                + "প্রয়োজনীয় স্মৃতি পরিকল্পনা করুন।\n\n"
                + target_body + "\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()
            report = Path(temporary_directory) / "leakage.csv"
            with (
                patch("check_translation_english_leakage.configured_locales", return_value=["bn"]),
                patch.object(
                    sys,
                    "argv",
                    ["checker", "--fail-on-english-fallback", "--csv", str(report), str(bundle)],
                ),
                redirect_stdout(stdout),
            ):
                result = checker_main()
            with report.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))

        self.assertEqual(result, 1)
        self.assertIn("high_density_copied_english_mixed_phrases", stdout.getvalue())
        self.assertTrue(
            any("high_density_copied_english_mixed_phrases" in row["reasons"] for row in rows)
        )

    def test_generic_descriptor_screen_catches_hardware_controller(self):
        self.assertEqual(
            copied_english_generic_terms(
                "Flask dashboard support for GPS wardriving",
                "دعم لوحة Flask لـ GPS wardriving",
                "ar",
            ),
            ["gps wardriving"],
        )
        self.assertEqual(
            copied_english_generic_terms(
                "Omada OC200 Hardware Controller: $89",
                "Omada OC200 Hardware Controller: $89",
                "de",
            ),
            ["hardware controller"],
        )
        self.assertEqual(
            copied_english_generic_terms(
                "- **Use Prepared Statements**: explanatory localized text",
                "- **Use Prepared Statements**: 解释性本地化文本",
                "zh",
            ),
            ["use prepared statements"],
        )
        self.assertEqual(
            copied_english_generic_terms(
                "Snyk - Open Source Security Platform",
                "Snyk - Open Source Security Platform",
                "fr",
            ),
            ["open source security platform"],
        )
        self.assertEqual(
            copied_english_generic_terms(
                "Snyk - Open Source Security Platform",
                "Snyk - plate-forme de sécurité open source",
                "fr",
            ),
            [],
        )
        self.assertEqual(
            copied_english_generic_terms(
                "Multi-Gigabit capability", "Multi-Gigabit-fähig", "de"
            ),
            [],
        )
        self.assertEqual(copied_english_mixed_phrases("Astra max", "Astra max", "bn"), [])


if __name__ == "__main__":
    unittest.main()
