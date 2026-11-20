#!/usr/bin/env python3
"""Screen article translations for copied or English-dominant reader-facing prose.

The blocking mode also detects copied English list conjunctions and English-heavy
reader-facing comments or natural-language values in executable code fences.

Run on one or more article bundles, or scan all published article bundles:

    python3 tools/check_translation_english_leakage.py content/articles/<slug>
    python3 tools/check_translation_english_leakage.py --all --csv /tmp/leakage.csv

Findings require human review. A clean screen does not prove translation quality.
"""

from __future__ import annotations

import argparse
import ast
import csv
import datetime as dt
import json
import re
import sys
import tomllib
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit



ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config/_default/config.toml"
ARTICLES = ROOT / "content/articles"
ENGLISH_STOPWORDS = set(
    "the and of to in a is that for on with as by are be this or from at an not "
    "which can will have has it its was were if than these those they we you our "
    "should also when how what where after before use more into about through "
    "your yourself yourselves "
    "each one other any only all do does then their them there such using used "
    "may might could would must been being"
    .split()
)
ENGLISH_TITLE_TERMS = set(
    "attacks benefits best business cards challenge challenges cloud compare "
    "comparison components complete comprehensive credit data guide how introduction keep "
    "key legend link model network now option overview past personal practices "
    "privacy protect protecting protection review right risk safe secure security "
    "top browser browsers "
    "showdown skimming steps trust zero future incident breach"
    .split()
)
LOCALE_TITLE_LOANWORDS = {"de": {"skimming"}}
LOCALE_TITLE_LOANWORD_PHRASES = {
    "de": {"skimming abwehren"},
}
ENGLISH_READER_VERBS = {
    "allows", "enables", "ensures", "follows", "helps", "includes", "means",
    "offers", "provides", "remains", "requires", "supports", "uses", "works",
}
LOCALE_READER_VERB_HOMOGRAPHS = {"es": {"uses"}}
TABLE_ENGLISH_REVIEW_WORDS = ENGLISH_STOPWORDS | set(
    "average mean final score latency memory bandwidth method trial throughput "
    "value category result benchmark stage test cost price output input time "
    "performance description rate duration total size count level status per "
    "component privacy question local model server situation better choice "
    "reason evidence collect action recommendation finding concern response "
    "what check example setting location boundary control short project responsive assistant a"
    .split()
)
TABLE_UNTRANSLATED_GENERIC_LABELS = {
    "model a",
    "model b",
    "model c",
    "total certifications",
    "with fallback",
    "plug and play",
}
GENERIC_ENGLISH_TAXONOMY_LABELS = {
    "ad blocking",
    "cloud computing",
    "cross platform",
    "data privacy",
    "internet privacy",
    "open source",
    "python interpreter",
    "python security documentation",
}
GENERIC_ENGLISH_TECHNICAL_TERMS = {
    "gps wardriving", "hardware controller", "multi-gigabit", "open source security platform",
    "use prepared statements",
}
MIXED_PHRASE_FIXED_VALUES = {"astra max", "glm-5 max", "opus max"}
MIXED_PHRASE_STRICT_BLOCKER_THRESHOLD = 20
LOCALE_ACCEPTED_TAXONOMY_LOANWORDS = {
    "de": {"cloud computing", "python interpreter"},
    "it": {"cloud computing"},
    "nl": {"python interpreter"},
    "ro": {"cloud computing"},
}
GENERIC_ENGLISH_LINK_LABELS = {
    "here",
    "click",
    "read",
    "learn",
    "more",
    "continue",
    "download",
    "visit",
    "website",
    "source",
    "documentation",
    "link",
    "python website",
    "python downloads page",
    "python security documentation",
    "python website downloads",
    "aes wikipedia page",
    "wikipedia page",
    "downloads page",
    "security documentation",
    "tls rfc",
    "nist role based access control",
    "owasp rbac cheat sheet",
    "amazon web services aws security",
    "microsoft azure security and compliance",
    "google cloud platform security",
    "chocolatey documentation on puppet integration",
    "chocolatey module documentation for ansible",
    "chocolatey documentation on package creation",
    "chocolatey official website",
    "chocolatey documentation",
    "nuget package manager",
}
ACCEPTED_GENERIC_LINK_LABELS = {
    "de": {
        ("python website", "python-website"),
        ("python website - downloads", "python-website – downloads"),
    },
}
ACCEPTED_GENERIC_TECHNICAL_COMPOUNDS = {
    "de": {"multi-gigabit-fähig"},
}
ENGLISH_INTERNAL_LINK_DESCRIPTIVE_WORDS = {
    "enable", "two", "factor", "authentication", "compromised", "email",
    "flash", "download", "setup", "guide", "create", "strong", "password",
    "protect", "privacy", "security", "what", "think", "your", "how", "read",
}
LOCALIZED_TECHNICAL_LOANWORDS = {
    # Italian uses "password" in standard phrases such as "gestore di password".
    # Exact copied labels still fail the equality check below.
    "it": {"password"},
}
UNLABELED_FENCE_SINGLE_WORD_LABELS = {
    "additional", "category", "common", "description", "device", "done",
    "example", "input", "location", "manufacturer", "model", "name", "notes",
    "output", "primary", "product", "ready", "source", "start", "status", "stop",
    "type", "value", "vendor",
}
LOCALE_STOPWORDS = {
    "ca": set("el la els les un una i o de que en per amb és són es del dels al als sobre com no també si quan".split()),
    "de": set("der die das den dem des ein eine einer und oder zu im vom mit auf für ist sind wird werden nicht aus an bei nach über als dass weil sich von am zum zur auch".split()),
    "es": set("el la los las un una y o de que en para por con es son está están del al como no se también si cuando".split()),
    "fr": set("le la les un une des du et ou de que en pour par avec est sont pas dans sur au aux cette ces comme ne se aussi".split()),
    "it": set("il lo la gli le un una e o di che in per con è sono non del della dei al alla come si anche questo".split()),
    "nl": set("de het een en of van voor met is zijn in op aan niet dat als zich ook naar door deze dit".split()),
    "pl": set("i w z na do jest są nie się oraz albo że dla przez od co jak tego tej także".split()),
    "pt": set("o a os as um uma e ou de que em para por com é são não do da dos das como se também".split()),
    "ro": set("a și de în la este sunt cu pentru din nu pe un o că ca aceasta acești".split()),
}
LOCALE_ACRONYM_LOCALIZATION_MARKERS = {
    "de": set(
        "datenübertrag geschütz sicher sicherheit verschlüssel verbindung "
        "übertrag nahfeldkommunik privat privates privater virtuell virtuelle "
        "virtuelles netzwerk"
        .split()
    ),
    "nl": set(
        "beveilig contactloz gegevens bescherming versleutel veilig veiligheid verbinding "
        "overdracht belangrijkste onderdeel privé privénetwerk virtueel virtuele "
        "netwerk"
        .split()
    ),
    "pl": set(
        "zaawansowan standard szyfrow bezpiecze warstw transportow otwarty projekt "
        "aplikac internet"
        .split()
    ),
    "pt": set(
        "dados rede privad segurança segur conexã protocol proteg virtual transfer"
        .split()
    ),
}
CSV_FIELDS = [
    "path", "locale", "reasons", "tokens", "english_stopword_ratio",
    "locale_stopword_ratio", "exact_english_paragraphs",
    "exact_english_sentences", "copied_reader_fenced_lines",
    "copied_english_fenced_formulas",
    "copied_reader_code_prose", "copied_unlabeled_fence_lines", "copied_english_spans",
    "split_word_emphasis", "english_dominant_paragraphs",
    "copied_english_table_cells", "copied_english_headings",
    "copied_english_metadata", "taxonomy_count_differences",
    "expected_script_ratio", "copied_english_opening", "copied_link_labels",
    "english_dominant_title", "english_dominant_title_review",
    "copied_english_link_connectors",
    "copied_english_generic_link_labels",
    "copied_english_internal_link_labels",
    "copied_english_shortcode_descriptions",
    "copied_english_mixed_phrases",
    "copied_english_generic_terms",
    "copied_english_reader_verbs",
    "copied_english_acronym_expansions",
    "copied_english_inline_acronym_expansion_review",
    "missing_acronym_keys",
    "english_reader_code_prose_fallback",
    "high_confidence_english_paragraphs",
    "copied_english_body",
    "copied_english_prose_paragraphs",
    "markdown_structure_differences", "note",
]
SCRIPT_RANGES = {
    "ar": ((0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF)),
    "bn": ((0x0980, 0x09FF),),
    "hi": ((0x0900, 0x097F),),
    "pa": ((0x0A00, 0x0A7F),),
    "ru": ((0x0400, 0x052F),),
    "ja": ((0x3040, 0x30FF), (0x3400, 0x9FFF)),
    "zh": ((0x3400, 0x9FFF),),
}
REFERENCE_HEADINGS = {
    "reference", "references", "reference list", "references and resources", "sources", "source list",
    "bibliography", "bibliographies", "further reading", "referencia", "referencias", "referencias y recursos",
    "referencia bibliografica", "referencias bibliograficas", "referencies", "referències", "referències i recursos",
    "referencia", "referencias", "bibliografia", "bibliografie", "riferimenti", "fontes", "referências",
    "referências e recursos", "fontes bibliográficas", "références", "referenties", "bronnen", "referencje", "źródła", "spis źródeł", "literatura", "список литературы",
    "библиография", "источники", "المراجع", "المصادر", "संदर्भ", "स्रोत", "তথ্যসূত্র", "ਹਵਾਲੇ",
    "referències", "riferimenti bibliografici", "références", "referințe", "referințe bibliografice",
    "参考文献", "参考资料", "参考資料", "參考文獻",
}


def is_reference_heading(value: str) -> bool:
    """Match localized bibliography labels, accents, and qualified variants."""
    def fold(text: str) -> str:
        normalized = unicodedata.normalize("NFKD", normalize(text))
        return "".join(char for char in normalized if not unicodedata.combining(char))

    heading = fold(value)
    return heading in {fold(item) for item in REFERENCE_HEADINGS}


def configured_locales() -> list[str]:
    data = tomllib.loads(CONFIG.read_text(encoding="utf-8"))
    languages = data.get("languages", {})
    if not isinstance(languages, dict):
        raise ValueError("config/_default/config.toml has no [languages.<code>] tables")
    return sorted(code for code, value in languages.items() if code.lower() != "en" and isinstance(value, dict))


def yaml_sequence_values(raw: str) -> list[str]:
    """Parse simple quoted or plain YAML sequence values."""
    values = []
    current = []
    quote = None
    index = 0
    while index < len(raw):
        char = raw[index]
        following = raw[index + 1] if index + 1 < len(raw) else ""
        if quote == "'" and char == "'" and following == "'":
            current.extend((char, following))
            index += 2
            continue
        if quote == '"' and char == "\\" and following:
            current.extend((char, following))
            index += 2
            continue
        if quote and char == quote:
            current.append(char)
            quote = None
        elif quote:
            current.append(char)
        elif char in {"'", '"'}:
            quote = char
            current.append(char)
        elif char == ",":
            values.append("".join(current).strip())
            current = []
        elif char not in "[]":
            current.append(char)
        index += 1
    if current:
        values.append("".join(current).strip())

    parsed = []
    for value in values:
        if not value:
            continue
        if value.startswith('"') and value.endswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                value = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        else:
            value = re.sub(r"\s+#.*$", "", value).strip()
        parsed.append(value)
    return parsed


def yaml_unquoted_comment(value: str) -> str:
    """Remove a YAML comment from an unquoted scalar value."""
    quote = None
    for index, char in enumerate(value):
        if quote == "'" and char == "'" and index + 1 < len(value) and value[index + 1] == "'":
            continue
        if quote == '"' and char == "\\":
            continue
        if quote and char == quote:
            quote = None
        elif not quote and char in {"'", '"'}:
            quote = char
        elif not quote and char == "#" and (index == 0 or value[index - 1].isspace()):
            return value[:index].rstrip()
    return value.strip()


def yaml_quoted_scalar_end(value: str, quote: str) -> int | None:
    """Return the closing quote position when a YAML quoted scalar is complete."""
    index = 1
    while index < len(value):
        char = value[index]
        if quote == "'" and char == "'" and index + 1 < len(value) and value[index + 1] == "'":
            index += 2
            continue
        if quote == '"' and char == "\\":
            index += 2
            continue
        if char == quote:
            remainder = value[index + 1:].lstrip()
            if not remainder or remainder.startswith("#"):
                return index
        index += 1
    return None


def yaml_scalar_value(lines: list[str], index: int, raw_value: str) -> tuple[str, int]:
    """Read a quoted, plain, or block scalar and return its next line index."""
    value = raw_value.strip()
    block = re.fullmatch(r"[>|](?:[+-][1-9]?|[1-9][+-]?)?", value)
    if block:
        style = value[0]
        content: list[str] = []
        content_indent: int | None = None
        parent_indent = len(lines[index]) - len(lines[index].lstrip())
        next_index = index + 1
        while next_index < len(lines):
            line = lines[next_index]
            if line.strip():
                indent = len(line) - len(line.lstrip())
                if indent <= parent_indent:
                    break
                if content_indent is None:
                    content_indent = indent
                elif indent < content_indent:
                    break
            content.append(line.strip())
            next_index += 1
        separator = "\n" if style == "|" else " "
        return separator.join(content).strip(), next_index

    if value.startswith(('"', "'")):
        quote = value[0]
        scalar_parts = [value]
        next_index = index + 1
        while yaml_quoted_scalar_end(scalar_parts[-1], quote) is None and next_index < len(lines):
            scalar_parts.append(lines[next_index].strip())
            next_index += 1
        scalar = " ".join(scalar_parts).strip()
        end = yaml_quoted_scalar_end(scalar, quote)
        if end is not None:
            scalar = scalar[:end + 1]
        if len(scalar) > 1 and scalar[0] == scalar[-1] == '"':
            try:
                scalar = json.loads(scalar)
            except json.JSONDecodeError:
                scalar = scalar[1:-1].replace('\\"', '"')
        elif len(scalar) > 1 and scalar[0] == scalar[-1] == "'":
            scalar = scalar[1:-1].replace("''", "'")
        return str(scalar), next_index

    return yaml_unquoted_comment(value), index + 1


def yaml_front_matter_scalar(header: str, key: str) -> str | None:
    """Read a YAML front-matter scalar, including folded and unquoted values."""
    lines = header.splitlines()
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}\s*:\s*(.*)$", line)
        if match:
            value, _ = yaml_scalar_value(lines, index, match.group(1))
            return value
    return None


def yaml_front_matter_lists(header: str, key: str) -> list[str]:
    """Read an inline or block-style YAML list from article front matter."""
    lines = header.splitlines()
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}\s*:\s*(.*)$", line)
        if not match:
            continue
        value = match.group(1).strip()
        if value.startswith("["):
            return yaml_sequence_values(value)
        if value:
            return []
        items = []
        for child in lines[index + 1:]:
            item = re.match(r"^\s*-\s+(.*?)\s*$", child)
            if item:
                items.extend(yaml_sequence_values(item.group(1)))
            elif child.strip():
                break
        return items
    return []


def read_page(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", text, re.S)
    if not match:
        return {}, text
    header = match.group(1)
    metadata: dict[str, object] = {}
    draft = re.search(r"(?m)^draft\s*:\s*(true|false)\s*(?:#.*)?$", header, re.I)
    if draft:
        metadata["draft"] = draft.group(1).lower() == "true"
    date = re.search(r"(?m)^date\s*:\s*[\"']?(\d{4}-\d{2}-\d{2})", header)
    if date:
        try:
            metadata["date"] = dt.date.fromisoformat(date.group(1))
        except ValueError:
            pass
    for key in ("title", "description", "coverAlt", "coverCaption"):
        value = yaml_front_matter_scalar(header, key)
        if value is not None:
            metadata[key] = value
    for key in ("genre", "tags"):
        values = yaml_front_matter_lists(header, key)
        if values:
            metadata[key] = values
    return metadata, match.group(2)


def copied_english_taxonomy(source: dict, target: dict) -> dict[str, list[str]]:
    """Find unchanged genre or tag values for manual review."""
    copied: dict[str, list[str]] = {}
    for key in ("genre", "tags"):
        source_values = source.get(key, [])
        target_values = target.get(key, [])
        if not isinstance(source_values, list) or not isinstance(target_values, list):
            continue
        target_normalized = {normalize(value) for value in target_values if isinstance(value, str)}
        values = [
            value for value in source_values
            if isinstance(value, str)
            and normalize(value)
            and normalize(value) in target_normalized
        ]
        if values:
            copied[key] = sorted(set(values))
    return copied


def copied_generic_english_taxonomy(
    source: dict, target: dict, locale: str = ""
) -> dict[str, list[str]]:
    """Find unchanged generic English genre/tag values that must be localized."""
    copied = copied_english_taxonomy(source, target)
    accepted_loanwords = LOCALE_ACCEPTED_TAXONOMY_LOANWORDS.get(locale, set())
    return {
        key: [
            value for value in values
            if normalize(value) in GENERIC_ENGLISH_TAXONOMY_LABELS
            and normalize(value) not in accepted_loanwords
        ]
        for key, values in copied.items()
        if any(
            normalize(value) in GENERIC_ENGLISH_TAXONOMY_LABELS
            and normalize(value) not in accepted_loanwords
            for value in values
        )
    }


def english_dominant_title(title: str, locale: str) -> bool:
    """Flag high-confidence English title segments, including mixed titles."""
    high_confidence, _needs_review = english_title_signals(title, locale)
    return high_confidence


def english_dominant_title_review(title: str, locale: str) -> bool:
    """Queue ambiguous English-looking titles for a human source comparison."""
    _high_confidence, needs_review = english_title_signals(title, locale)
    return needs_review


def english_title_signals(title: str, locale: str) -> tuple[bool, bool]:
    """Separate clear English titles from titles that only need manual review."""
    title_without_fixed_term = re.sub(
        r"\bzero[\s-]+trust\b", " ", title, flags=re.I
    )
    title_without_fixed_term = re.sub(
        r"\bflipper[\s-]+zero\b", "Flipper", title_without_fixed_term, flags=re.I
    )
    english_terms = ENGLISH_STOPWORDS | ENGLISH_TITLE_TERMS
    locale_words = LOCALE_STOPWORDS.get(locale, set())
    for raw_segment in re.split(r"[:;|.!?–—]", title_without_fixed_term):
        segment = normalize(raw_segment).lower()
        raw_words = re.findall(r"[^\W_]+(?:['’][^\W_]+)?", raw_segment, re.UNICODE)
        words = [word.lower() for word in raw_words]
        if len(words) < 2:
            continue
        has_localized_loanword_phrase = segment in LOCALE_TITLE_LOANWORD_PHRASES.get(
            locale, set()
        )
        segment_english_terms = (
            english_terms - LOCALE_TITLE_LOANWORDS.get(locale, set())
            if has_localized_loanword_phrase
            else english_terms
        )
        english_matches = sum(
            word in segment_english_terms
            and word not in locale_words
            and (not raw_word.isupper() or word in ENGLISH_TITLE_TERMS)
            for word, raw_word in zip(words, raw_words)
        )
        english_ratio = english_matches / len(words)
        locale_ratio = sum(word in locale_words for word in words) / len(words)
        if english_ratio < 0.40 or locale_ratio >= 0.25:
            continue
        script_ratio_value = script_ratio(segment, locale)
        if script_ratio_value is not None and script_ratio_value >= 0.25:
            continue
        content_matches = sum(
            word in ENGLISH_TITLE_TERMS
            and word not in LOCALE_TITLE_LOANWORDS.get(locale, set())
            and word not in locale_words
            for word, raw_word in zip(words, raw_words)
        )
        if content_matches >= 2:
            return True, False
        if content_matches >= 1:
            return False, True
    return False, False


def copied_english_inline_acronym_expansions(
    source: str, target: str, locale: str
) -> tuple[list[str], list[str]]:
    """Find copied acronym expansions in prose and queue likely proper names."""
    pattern = re.compile(
        r"\b(?P<key>(?:[A-Z][a-z]+(?:[A-Z][A-Za-z0-9]*)+|[A-Z][A-Z0-9/&.-]{1,}[a-z]?))\s*"
        r"(?:[-‐‑][^\W_]+)*\s*"
        r"\(\s*(?P<expansion>[^()\n]{4,240})\s*\)"
    )
    target_parenthetical = re.compile(
        r"(?P<key>[^\s()]+)\s*\(\s*(?P<expansion>[^()\n]{4,240})\s*\)",
        re.UNICODE,
    )
    glossary_entry = re.compile(r"^[-*+]\s+\*\*[A-Z][A-Za-z0-9/&.-]*\*\*\s*:")

    def prose_pairs(text: str) -> set[tuple[str, str]]:
        pairs: set[tuple[str, str]] = set()
        prose = strip_fenced_blocks(text)
        for paragraph in re.split(r"\n\s*\n", prose):
            lines = [line.strip() for line in paragraph.splitlines() if line.strip()]
            if not lines or all(line.startswith(("#", "|", "{{<", "{{%")) for line in lines):
                continue
            if all(glossary_entry.match(line) for line in lines):
                continue
            visible = visible_text(paragraph, include_link_labels=False)
            for match in pattern.finditer(visible):
                expansion = normalize(match.group("expansion"))
                if len(expansion.split()) >= 2:
                    pairs.add((normalize(match.group("key")), expansion))
        return pairs

    def has_localized_explanation(extra: str) -> bool:
        if locale in SCRIPT_RANGES:
            ranges = SCRIPT_RANGES[locale]
            letters = [char for char in extra if char.isalpha()]
            localized_letters = sum(
                any(start <= ord(char) <= end for start, end in ranges)
                for char in letters
            )
            return localized_letters >= 6

        words = re.findall(r"[^\W_]+(?:['’][^\W_]+)?", extra.lower(), re.UNICODE)
        content_words = [word for word in words if word not in ENGLISH_STOPWORDS]
        if locale in {"de", "nl"}:
            has_local_word = any(
                word.startswith(marker)
                for word in content_words
                for marker in LOCALE_ACRONYM_LOCALIZATION_MARKERS[locale]
            )
            has_local_connector = any(
                word in LOCALE_STOPWORDS.get(locale, set()) for word in words
            )
            return has_local_word or has_local_connector
        if locale in LOCALE_ACRONYM_LOCALIZATION_MARKERS:
            if any(
                word.startswith(marker)
                for word in content_words
                for marker in LOCALE_ACRONYM_LOCALIZATION_MARKERS[locale]
            ):
                return True
        has_local_connector = any(
            word in LOCALE_STOPWORDS.get(locale, set()) for word in words
        )
        return len(content_words) >= 2 and has_local_connector

    source_pairs = prose_pairs(source)
    target_pairs = prose_pairs(target)
    blocking: set[str] = set()
    review: set[str] = set()
    target_by_key: dict[str, set[str]] = {}
    for key, expansion in target_pairs:
        target_by_key.setdefault(key, set()).add(expansion)

    for key, source_expansion in source_pairs:
        for target_expansion in target_by_key.get(key, set()):
            if source_expansion not in target_expansion:
                continue
            extra = target_expansion.replace(source_expansion, " ", 1).strip()
            finding = f"{key}: {source_expansion}"
            localized_explanation = bool(extra and has_localized_explanation(extra))
            if extra and localized_explanation:
                # A script check cannot distinguish a translation from a
                # phonetic transliteration. Keep bilingual expansions in the
                # manual-review queue so a reviewer confirms meaning.
                review.add(finding)
                continue
            raw_expansion = next(
                (
                    match.group("expansion").strip()
                    for match in pattern.finditer(visible_text(target, include_link_labels=False))
                    if normalize(match.group("key")) == key
                    and normalize(match.group("expansion")) == target_expansion
                ),
                "",
            )
            words = re.findall(r"[A-Za-z]+", raw_expansion)
            title_case_ratio = sum(word[0].isupper() for word in words) / max(1, len(words))
            if title_case_ratio >= 0.6:
                review.add(finding)
            else:
                blocking.add(finding)

    # A locale can transliterate the acronym itself, which hides the source key
    # from the matcher (for example, NFC -> एनएफसी). Queue those parentheticals
    # for semantic review instead of silently treating them as localized.
    source_keys_by_paragraph: list[set[str]] = []
    for paragraph in re.split(r"\n\s*\n", strip_fenced_blocks(source)):
        source_keys_by_paragraph.append(
            {
                normalize(match.group("key"))
                for match in pattern.finditer(
                    visible_text(paragraph, include_link_labels=False)
                )
            }
        )
    target_paragraphs = re.split(r"\n\s*\n", strip_fenced_blocks(target))
    for index, paragraph in enumerate(target_paragraphs):
        source_keys = (
            source_keys_by_paragraph[index]
            if index < len(source_keys_by_paragraph)
            else set()
        )
        if not source_keys:
            continue
        visible_paragraph = visible_text(paragraph, include_link_labels=False)
        for match in target_parenthetical.finditer(visible_paragraph):
            target_key = match.group("key").strip().lower()
            if target_key.isascii():
                continue
            expansion = normalize(match.group("expansion"))
            if len(expansion.split()) >= 2:
                possible_keys = ", ".join(sorted(source_keys))
                review.add(
                    f"{possible_keys}: possible noncanonical target key {target_key}; "
                    "map this occurrence and verify expansion meaning"
                )

    return sorted(blocking), sorted(review)


def taxonomy_count_differences(source: dict, target: dict) -> dict[str, tuple[int, int]]:
    """Find source/translation genre or tag cardinality differences."""
    differences = {}
    for key in ("genre", "tags"):
        source_values = source.get(key, [])
        target_values = target.get(key, [])
        if isinstance(source_values, list) and isinstance(target_values, list):
            if len(source_values) != len(target_values):
                differences[key] = (len(source_values), len(target_values))
    return differences


def fenced_blocks(text: str) -> list[dict[str, object]]:
    """Return Markdown fenced blocks, including their language, body, and offsets."""
    lines = text.splitlines(keepends=True)
    blocks = []
    offsets = []
    offset = 0
    for line in lines:
        offsets.append(offset)
        offset += len(line)
    index = 0
    opener = re.compile(r"^ {0,3}(?P<marker>`{3,}|~{3,})[ \t]*(?P<info>[^\n]*)$")
    closer = re.compile(r"^ {0,3}(?P<marker>`+|~+)[ \t]*$")
    while index < len(lines):
        match = opener.match(lines[index].rstrip("\r\n"))
        if not match:
            index += 1
            continue
        marker = match.group("marker")
        info = match.group("info").strip()
        if marker[0] == "`" and "`" in info:
            index += 1
            continue
        language = info.split(maxsplit=1)[0].lower() if info else ""
        body_start = index + 1
        close_index = body_start
        while close_index < len(lines):
            close = closer.match(lines[close_index].rstrip("\r\n"))
            if close and close.group("marker")[0] == marker[0] and len(close.group("marker")) >= len(marker):
                break
            close_index += 1
        body_end = close_index if close_index < len(lines) else len(lines)
        end_index = close_index + 1 if close_index < len(lines) else len(lines)
        blocks.append({
            "language": language,
            "body": "".join(lines[body_start:body_end]),
            "start": offsets[index],
            "end": offsets[end_index] if end_index < len(offsets) else len(text),
        })
        index = end_index
    return blocks


def strip_fenced_blocks(text: str) -> str:
    """Remove all fenced blocks from prose before Markdown syntax checks."""
    for block in reversed(fenced_blocks(text)):
        text = text[:block["start"]] + " " + text[block["end"]:]
    return text


def visible_text(text: str, *, include_link_labels: bool = True) -> str:
    # `text`, `plaintext`, and `markdown` fences hold reader-facing samples.
    # Keep those in the leakage screen. Exclude executable fences here, then
    # screen their comments and natural-language command strings separately.
    for block in reversed(fenced_blocks(text)):
        replacement = block["body"] if block["language"] in {"text", "plaintext", "markdown"} else " "
        text = text[:block["start"]] + replacement + text[block["end"]:]
    text = re.sub(r"(?m)^\s*\{\{<.*?>\}\}\s*$", " ", text)
    text = re.sub(r"\{\{<.*?>\}\}", " ", text)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"https?://[^\s)\]>]+", " ", text)
    link_replacement = r"\1" if include_link_labels else " "
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", link_replacement, text)
    text = re.sub(r"<[^>]+>", " ", text)
    return text


def reader_fenced_prose(text: str) -> list[str]:
    """Return complete reader-facing text, plaintext, or Markdown examples."""
    return [
        block["body"].strip()
        for block in fenced_blocks(text)
        if block["language"] in {"text", "plaintext", "markdown"}
    ]


def reader_fenced_code_prose(text: str) -> set[str]:
    """Extract reader-facing comments and natural-language command strings from code fences."""
    non_code_languages = {"text", "plaintext", "markdown", "json", "csv", "diff", "console", "output"}
    hash_comment_languages = {
        "bash", "sh", "shell", "zsh", "powershell", "pwsh", "python", "py",
        "ruby", "perl", "pl", "yaml", "yml", "toml", "ini", "dockerfile",
        "make", "makefile", "r", "terraform", "tf", "hcl", "julia", "jl",
        "azurecli", "azcli",
    }
    slash_comment_languages = {
        "javascript", "js", "typescript", "ts", "go", "rust", "c", "cpp",
        "csharp", "cs", "java", "php", "kotlin", "swift", "scala", "sbt",
        "groovy", "gradle", "objectivec", "objc", "dart", "solidity", "sol",
        "fsharp", "fs", "terraform", "tf", "hcl",
    }
    comment_languages = (
        hash_comment_languages | slash_comment_languages
        | {"sql", "lua", "haskell", "hs", "erlang", "erl", "clojure", "clj", "html", "xml", "css"}
    )
    command_languages = {
        "bash", "sh", "shell", "zsh", "powershell", "pwsh", "python", "py",
        "ruby", "perl", "r", "javascript", "js", "typescript", "ts", "c", "cpp",
        "java", "csharp", "cs", "go", "rust", "swift", "kotlin", "php", "lua",
        "scala", "groovy", "html",
    }
    hash_inline_requires_space = {
        "bash", "sh", "shell", "zsh", "powershell", "pwsh", "yaml", "yml",
        "toml", "ini", "dockerfile", "make", "makefile", "terraform", "tf", "hcl",
    }
    findings = set()
    for block in fenced_blocks(text):
        language = block["language"]
        if language in non_code_languages or language not in comment_languages:
            continue
        code = block["body"]
        if language in {"python", "py"}:
            try:
                python_tree = ast.parse(code)
            except (SyntaxError, ValueError):
                python_tree = None
            if python_tree is not None:
                for node in ast.walk(python_tree):
                    if isinstance(
                        node,
                        (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef),
                    ):
                        docstring = ast.get_docstring(node, clean=False)
                        normalized_docstring = normalize(docstring or "")
                        if normalized_docstring:
                            findings.add(normalized_docstring)
        if language in {"yaml", "yml"}:
            yaml_lines = code.splitlines()
            yaml_index = 0
            while yaml_index < len(yaml_lines):
                line = yaml_lines[yaml_index]
                sample_value = re.match(
                    r"^\s*(?:-\s*)?([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*"
                    r"([\"'])(.+?)\2\s*(?:#.*)?$",
                    line,
                )
                if sample_value and sample_value.group(1).lower() not in {
                    "name", "msg", "description", "message", "title", "caption",
                    "comment", "labeltext", "displaytext",
                }:
                    text_value = sample_value.group(3).strip()
                    words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text_value)
                    english_signals = sum(
                        word.lower() in ENGLISH_STOPWORDS for word in words
                    )
                    if (
                        len(words) >= 6
                        and english_signals >= 3
                        and english_signals / len(words) >= 0.22
                    ):
                        normalized = normalize(text_value)
                        if normalized:
                            findings.add(normalized)
                key = re.match(r"^(\s*)(?:-\s*)?(?:name|msg)\s*:\s*(.*?)\s*$", line)
                yaml_index += 1
                if not key:
                    continue
                indent = len(key.group(1))
                value = key.group(2).strip()
                is_message = re.match(r"^\s*msg\s*:", line) is not None
                if re.fullmatch(r"[|>](?:[+-]\d?|\d?[+-]?)?", value):
                    continuation = []
                    content_indent = None
                    while yaml_index < len(yaml_lines):
                        next_line = yaml_lines[yaml_index]
                        if next_line.strip():
                            next_indent = len(next_line) - len(next_line.lstrip())
                            if content_indent is None:
                                content_indent = next_indent
                            elif next_indent < content_indent:
                                break
                        continuation.append(next_line.strip())
                        yaml_index += 1
                    value = " ".join(continuation)
                if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                    value = value[1:-1]
                if re.fullmatch(r"\s*{{[^{}]+}}\s*", value):
                    continue
                if is_message and (
                    re.fullmatch(
                        r"(?:ok|success|failure|failed|error|complete|"
                        r"unknown|enabled|disabled|yes|no|true|false)",
                        value,
                        re.I,
                    )
                    or re.match(
                        r"^(?:PASS|FAIL|ERROR|WARN|INFO):\s|"
                        r"(?:permission denied|operation not permitted|command not found|"
                        r"no such file or directory|access denied|operation timed out|"
                        r"connection refused|connection timed out|request timed out|"
                        r"network is unreachable|host is unreachable|broken pipe|"
                        r"address already in use|no route to host|no changes detected)\b",
                        value,
                        re.I,
                    )
                ):
                    continue
                normalized = normalize(value)
                if normalized:
                    findings.add(normalized)
        if language in {"html", "xml"}:
            for element in re.finditer(
                r"<(button|a|label|option|title|summary|legend|h[1-6])\b[^>]*>(.*?)</\1\s*>",
                code,
                re.I | re.S,
            ):
                label = normalize(re.sub(r"<[^>]+>", " ", element.group(2)))
                if label:
                    findings.add(label)
            for attribute in re.finditer(
                r"\b(?:aria-label|title|placeholder|alt)\s*=\s*([\"'])(.*?)\1",
                code,
                re.I | re.S,
            ):
                label = normalize(attribute.group(2))
                if label:
                    findings.add(label)
        for comment in re.finditer(r"(?s)<!--(.*?)-->|/\*(.*?)\*/", code):
            normalized = normalize(comment.group(1) or comment.group(2))
            if normalized:
                findings.add(normalized)
        line_comment_markers = []
        if language in hash_comment_languages:
            line_comment_markers.append(r"#(?![!])")
        if language in slash_comment_languages:
            line_comment_markers.append(r"//")
        if language in {"sql", "lua", "haskell", "hs"}:
            line_comment_markers.append(r"--")
        if language in {"ini", "clojure", "clj"}:
            line_comment_markers.append(r";")
        if language in {"erlang", "erl"}:
            line_comment_markers.append(r"%")
        line_comment_marker = "|".join(line_comment_markers) or r"(?!)"
        for line in code.splitlines():
            comment = re.match(rf"^\s*(?:{line_comment_marker})\s*(.+?)\s*$", line)
            if comment:
                normalized = normalize(comment.group(1))
                if normalized:
                    findings.add(normalized)
            reader_text_assignment = re.search(
                r"\b[A-Za-z_]*(?:description|message|title|caption|comment|labeltext|displaytext)"
                r"\s*[:=]\s*([\"'])(.*?)\1",
                line,
                re.I,
            )
            if reader_text_assignment:
                text_value = reader_text_assignment.group(2).strip()
                words = normalize(text_value).split()
                if len(words) >= 5 and sum(word in ENGLISH_STOPWORDS for word in words) >= 2:
                    findings.add(normalize(text_value))
            returned_text = re.search(r"\breturn\s+([\"'])(.*?)\1", line)
            if returned_text:
                text_value = returned_text.group(2).strip()
                if normalize(text_value):
                    findings.add(normalize(text_value))
            inline_markers: list[tuple[str, bool]] = []
            if any(marker.startswith("#") for marker in line_comment_markers):
                inline_markers.append((r"#", language in hash_inline_requires_space))
            if "//" in line_comment_markers:
                inline_markers.append((r"//", False))
            if language in {"sql", "lua", "haskell", "hs"}:
                inline_markers.append((r"--", False))
            if language in {"ini", "clojure", "clj"}:
                inline_markers.append((r";", language == "ini"))
            if language in {"erlang", "erl"}:
                inline_markers.append((r"%", False))
            for marker, needs_space in inline_markers:
                for inline_comment in re.finditer(rf"{marker}\s*(.+?)\s*$", line):
                    prefix = line[:inline_comment.start()]
                    if needs_space and prefix and not prefix[-1].isspace():
                        continue
                    if marker == r"//" and re.search(r"https?:$", prefix, re.I):
                        continue
                    quote = None
                    escaped = False
                    for char in prefix:
                        if escaped:
                            escaped = False
                        elif char == "\\":
                            escaped = True
                        elif quote:
                            if char == quote:
                                quote = None
                        elif char in {"'", '"', "`"}:
                            quote = char
                    if quote:
                        continue
                    normalized = normalize(inline_comment.group(1))
                    if normalized:
                        findings.add(normalized)
            commit_subjects = re.finditer(
                r"\bgit\s+commit\b[^\n]*?\s-m\s+([\"'])(.+?)\1", line
            ) if language in {"bash", "sh", "shell", "zsh", "powershell", "pwsh"} else []
            for subject in commit_subjects:
                findings.add(normalize(subject.group(2)))
            user_output = re.finditer(
                r"(?:\b(?:echo|printf|Write-Host|Write-Output|Write-Warning|Write-Error|print|println|puts|say|warn|"
                r"console\.(?:log|info|warn|error)|process\.stdout\.write|"
                r"logger\.(?:debug|info|warn|error)|System\.(?:out|err)\.(?:print|println|printf)|"
                r"Console\.(?:Write|WriteLine)|fmt\.(?:Print|Println|Printf)|"
                r"log\.(?:Print|Println|Printf|Fatal|Panic)|NSLog|debugPrint|"
                r"document\.write|alert)\b|std::(?:cout|cerr)\s*<<|"
                r"(?:println|print|eprintln|eprint)!)[^\n]*?"
                r"([\"'`])((?:\\.|(?!\1)[^\\]){2,})\1",
                line,
            ) if language in command_languages else []
            for message in user_output:
                text_value = message.group(2).strip()
                identifier_only = (
                    re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", text_value)
                    and (
                        "_" in text_value
                        or re.search(r"[a-z0-9][A-Z]", text_value)
                    )
                )
                if (
                    identifier_only
                    or re.fullmatch(
                        r"(?:ok|success|failure|failed|error|"
                        r"complete|unknown|enabled|disabled|yes|no|true|false)",
                        text_value,
                        re.I,
                    )
                    or re.match(
                        r"^(?:PASS|FAIL|ERROR|WARN|INFO):\s|"
                        r"(?:permission denied|operation not permitted|command not found|"
                        r"no such file or directory|access denied|operation timed out|"
                        r"connection refused|connection timed out|request timed out|"
                        r"network is unreachable|host is unreachable|broken pipe|"
                        r"address already in use|no route to host|no changes detected)\b",
                        text_value,
                        re.I,
                    )
                ):
                    continue
                normalized = normalize(text_value)
                if normalized:
                    findings.add(normalized)
        if language == "html":
            html = re.sub(r"(?is)<(?:script|style)\b.*?</(?:script|style)\s*>", " ", code)
            for visible in re.finditer(r">([^<>]+)<", html):
                text_value = visible.group(1).strip()
                if normalize(text_value):
                    findings.add(normalize(text_value))
            for attribute in re.finditer(
                r"\b(?:aria-label|placeholder|title|alt)\s*=\s*([\"'])(.*?)\1",
                html,
                re.I,
            ):
                text_value = attribute.group(2).strip()
                if normalize(text_value):
                    findings.add(normalize(text_value))
    return {finding for finding in findings if finding}


def copied_reader_fenced_examples(source: str, target: str) -> set[str]:
    """Find unchanged reader-facing fenced examples with enough prose to review."""
    def has_english_prose(block: str) -> bool:
        tokens = normalize(block).split()
        return len(tokens) >= 8 and sum(token in ENGLISH_STOPWORDS for token in tokens) >= 2

    source_blocks = {
        normalize(block)
        for block in reader_fenced_prose(source)
        if has_english_prose(block)
    }
    target_blocks = {
        normalize(block)
        for block in reader_fenced_prose(target)
        if has_english_prose(block)
    }
    return source_blocks & target_blocks


def copied_reader_fenced_lines(source: str, target: str) -> set[str]:
    """Find unchanged descriptive lines inside reader-facing text fences."""
    def eligible_lines(text: str) -> set[str]:
        lines = set()
        for block in reader_fenced_prose(text):
            for line in block.splitlines():
                stripped = line.strip().strip("`*_ ")
                if re.match(r"^(?:PASS|FAIL|ERROR|WARN|INFO):\s", stripped, re.I):
                    # Literal validation output is evidence, not reader prose.
                    continue
                mapping = re.split(r"\s*(?:->|→)\s*", stripped)
                if len(mapping) > 1 and all(
                    re.fullmatch(r"[A-Za-z0-9_./-]+", part.strip())
                    for part in mapping
                ):
                    # Identifier/path mappings carry structural evidence, not prose.
                    continue
                normalized = normalize(line)
                words = normalized.split()
                # Ignore short proper names and numeric or identifier-only data.
                if len(words) >= 3 and sum(word.isalpha() for word in words) >= 3:
                    lines.add(normalized)
        return lines

    return eligible_lines(source) & eligible_lines(target)


def copied_english_fenced_formulas(source: str, target: str) -> list[str]:
    """Find copied English unit labels in reader-facing calculation lines."""
    units = {
        "layer", "layers", "head", "heads", "dimension", "dimensions",
        "byte", "bytes", "token", "tokens",
    }
    findings = []
    for line in copied_reader_fenced_lines(source, target):
        words = line.split()
        number_count = sum(word.isdigit() for word in words)
        unit_count = len(set(words) & units)
        if number_count >= 4 and unit_count >= 2:
            findings.append(line)
    return sorted(findings)


def copied_unlabeled_fence_lines(source: str, target: str) -> set[str]:
    """Find unchanged descriptive lines in fences without an info string."""
    def eligible_lines(text: str) -> set[str]:
        lines = set()
        for block in fenced_blocks(text):
            if block["language"]:
                continue
            for line in block["body"].splitlines():
                stripped = line.strip().strip("`*_ ")
                if not stripped:
                    continue
                if re.match(r"^(?:[0-9A-Fa-f]{2}:){2,}[0-9A-Fa-f]{2}(?:\s|$)", stripped):
                    # MAC/OUI address rows are literal identifiers, not prose.
                    continue
                arrow_parts = re.split(r"\s*(?:->|→|=>)\s*", stripped)
                if (
                    len(arrow_parts) == 2
                    and re.fullmatch(r"[A-Z][A-Z0-9]*(?:[-_][A-Z0-9]+)*", arrow_parts[0].strip())
                    and re.search(r"\d", arrow_parts[0])
                    and re.fullmatch(r"[A-Za-z0-9_./-]+", arrow_parts[1].strip())
                    and (
                        "/" in arrow_parts[1]
                        or re.search(r"\.[A-Za-z0-9]{1,8}$", arrow_parts[1].strip())
                    )
                ):
                    # Clear uppercase requirement IDs pointing to a path or file
                    # are data. Word-like and numbered phase flows remain prose.
                    continue
                # Numeric prose still needs review. Exclude only data-only lines
                # here; address rows receive the narrower check above.
                words = re.findall(r"[A-Za-z]{3,}", stripped)
                if not words:
                    continue
                has_numeric_quantity = bool(re.search(r"\b\d+(?:[,.]\d+)?\s*%?\b", stripped))
                if len(words) >= 2 or has_numeric_quantity or (
                    len(words) == 1 and words[0].lower() in UNLABELED_FENCE_SINGLE_WORD_LABELS
                ):
                    lines.add(normalize(stripped))
        return lines

    return eligible_lines(source) & eligible_lines(target)


def copied_reader_code_prose(source: str, target: str) -> set[str]:
    """Find unchanged natural-language comments or output strings in executable examples."""
    return reader_fenced_code_prose(source) & reader_fenced_code_prose(target)


def english_reader_code_prose_fallback(source: str, target: str) -> list[str]:
    """Screen copied code prose for English stopword-dense sentences and comments."""
    short_reader_strings = {
        "hello",
        "hello there",
        "welcome",
        "thank you",
        "please",
    }
    findings = []
    for phrase in copied_reader_code_prose(source, target):
        if phrase in short_reader_strings:
            findings.append(phrase)
            continue
        words = re.findall(r"[a-z]+(?:'[a-z]+)?", phrase.lower())
        if len(words) < 5:
            continue
        english_ratio = sum(word in ENGLISH_STOPWORDS for word in words) / len(words)
        if english_ratio >= 0.16:
            findings.append(phrase)
    return sorted(findings)


def split_word_emphasis(text: str, locale: str | None = None) -> list[str]:
    """Find emphasis spans embedded in words or isolated Japanese particles."""
    visible = visible_text(strip_fenced_blocks(text))
    findings = []
    spans = re.finditer(r"(?<!\\)(\*\*|__|\*|_)(.+?)(?<!\\)(\*\*|__|\*|_)", visible)
    japanese_particles = {
        "は", "が", "を", "に", "で", "と", "の", "へ", "も", "や", "か", "ね", "よ",
        "から", "まで", "より", "だけ", "しか", "こそ", "さえ", "など", "って",
    }
    for match in spans:
        start_marker = match.group(1)
        span_text = match.group(2).strip()
        end_marker = match.group(3)
        if start_marker != end_marker:
            continue
        open_start, open_end = match.span(1)
        close_start, close_end = match.span(3)
        boundaries = (
            (visible[open_start - 1] if open_start else " ", visible[open_end]),
            (visible[close_start - 1], visible[close_end] if close_end < len(visible) else " "),
        )
        splits_word = start_marker.startswith("*") and any(
            before.isalnum() and after.isalnum()
            and not _is_cjk(before) and not _is_cjk(after)
            for before, after in boundaries
        )
        isolates_particle = (
            start_marker.startswith("*")
            and locale and locale.lower() == "ja" and span_text in japanese_particles
        )
        if not (splits_word or isolates_particle):
            continue
        start, end = match.span()
        context_start = max(0, start - 28)
        context_end = min(len(visible), end + 28)
        findings.append(visible[context_start:context_end].strip())
    return sorted(set(findings))


def _is_cjk(char: str) -> bool:
    codepoint = ord(char)
    return (
        0x3040 <= codepoint <= 0x30FF
        or 0x3400 <= codepoint <= 0x9FFF
        or 0xF900 <= codepoint <= 0xFAFF
        or 0xAC00 <= codepoint <= 0xD7AF
        or 0x1100 <= codepoint <= 0x11FF
    )


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return " ".join(re.findall(r"\w+", text, flags=re.UNICODE))


def markdown_links(text: str) -> list[tuple[str, str]]:
    """Return reader-facing Markdown link labels and targets outside code."""
    text = re.sub(r"(?s)```.*?```|~~~.*?~~~", " ", text)
    text = re.sub(r"`[^`]*`", " ", text)
    links = []
    for match in re.finditer(r"(?<!!)\[([^\]]+)\]\(([^)\n]+)\)", text):
        label = match.group(1).strip()
        target = match.group(2).strip().split(maxsplit=1)[0].strip("<>")
        links.append((label, target))
    return links


def copied_english_link_labels(source: str, target: str) -> list[str]:
    """Find unchanged descriptive source link labels for manual review."""
    copied = []
    for source_link, target_link in zip(markdown_links(source), markdown_links(target)):
        source_label, source_target = source_link
        target_label, target_target = target_link
        normalized_label = normalize(source_label)
        normalized_target_label = normalize(target_label)
        copied_phrase = bool(
            normalized_label
            and re.search(
                rf"(?<![A-Za-z0-9]){re.escape(normalized_label)}(?![A-Za-z0-9])",
                normalized_target_label,
            )
        )
        if (
            source_target == target_target
            and (
                len(normalized_label.split()) >= 2
                or normalized_label in GENERIC_ENGLISH_LINK_LABELS
            )
            and copied_phrase
        ):
            copied.append(f"{source_label} => {target_label} => {source_target}")
    return copied


def copied_english_generic_link_labels(source: str, target: str, locale: str) -> list[str]:
    """Find unchanged generic English link labels that should be localized."""
    copied = []
    for source_label, source_target in markdown_links(source):
        for target_label, target_target in markdown_links(target):
            accepted_label = (
                source_label.strip().casefold(), target_label.strip().casefold()
            )
            if (
                source_target == target_target
                and normalize(source_label) in GENERIC_ENGLISH_LINK_LABELS
                and normalize(source_label) == normalize(target_label)
                and accepted_label not in ACCEPTED_GENERIC_LINK_LABELS.get(locale, set())
            ):
                copied.append(f"{source_label} => {target_label} => {source_target}")
    return copied


def copied_english_shortcode_descriptions(source: str, target: str) -> list[str]:
    """Find unchanged reader-facing descriptions/captions/alts in shortcodes."""
    shortcode_pattern = re.compile(r"\{\{[<%]\s*([\w-]+)(?P<attrs>.*?)\s*[>%]\}\}", re.S)
    attr_pattern = re.compile(
        r"(?<![\w-])(?P<key>description|caption|alt)\s*=\s*"
        r"(?P<quote>[\"'])(?P<value>.*?)(?P=quote)",
        re.S,
    )

    def values(text: str) -> list[tuple[str, str, str]]:
        found = []
        for shortcode in shortcode_pattern.finditer(text):
            for attr in attr_pattern.finditer(shortcode.group("attrs")):
                found.append((shortcode.group(1), attr.group("key"), attr.group("value")))
        return found

    source_values = values(source)
    target_values = values(target)
    target_fields = {(name, key, normalize(value)) for name, key, value in target_values}
    copied = []
    for source_name, key, source_value in source_values:
        normalized = normalize(source_value)
        if len(normalized.split()) < 2:
            continue
        if (source_name, key, normalized) in target_fields:
            copied.append(f"{source_name}.{key}: {source_value}")
    return copied


def copied_english_internal_link_labels(source: str, target: str, locale: str) -> list[str]:
    """Block copied labels for first-party articles with a localized sibling title."""
    copied = []
    source_links_by_target: dict[str, list[str]] = {}
    for source_label, source_target in markdown_links(source):
        source_links_by_target.setdefault(source_target, []).append(source_label)
    for target_label, target_target in markdown_links(target):
        source_labels = source_links_by_target.get(target_target, [])
        target_words = set(normalize(target_label).split())
        matched_source = None
        for source_label in source_labels:
            source_words = set(normalize(source_label).split())
            shared_words = source_words & target_words
            shared_descriptive_words = shared_words & ENGLISH_INTERNAL_LINK_DESCRIPTIVE_WORDS
            shared_descriptive_words -= LOCALIZED_TECHNICAL_LOANWORDS.get(locale, set())
            if (
                source_words == target_words
                or bool(shared_descriptive_words)
            ):
                matched_source = source_label
                break
        if matched_source is None:
            continue
        parsed = urlsplit(target_target)
        host = (parsed.hostname or "").lower()
        if host and host != "simeononsecurity.com" and not host.endswith(".simeononsecurity.com"):
            continue
        path = unquote(parsed.path)
        match = re.search(r"(?:^|/)articles/([^/]+)/?$", path)
        if not match:
            continue
        translated_page = ARTICLES / match.group(1) / f"index.{locale}.md"
        if not translated_page.is_file():
            continue
        translated_metadata, _ = read_page(translated_page)
        translated_title = translated_metadata.get("title")
        if (
            isinstance(translated_title, str)
            and normalize(translated_title)
            and normalize(translated_title) != normalize(target_label)
        ):
            copied.append(f"{matched_source} => {target_label} => {target_target}")
    return copied


def copied_english_link_connectors(text: str) -> list[str]:
    """Find English `and` or `or` left as a connector in a linked item list."""
    findings = []
    visible = strip_fenced_blocks(text)

    def blank_code_span(match: re.Match[str]) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group())

    visible = re.sub(r"(`+)(.+?)\1", blank_code_span, visible, flags=re.S)
    for line_number, line in enumerate(visible.splitlines(), start=1):
        for match in re.finditer(r"(?i)\b(and|or)\s+(?=\[)", line):
            if len(markdown_links(line[:match.start()])) < 2:
                continue
            next_link = re.match(r"\[([^\]]+)\]", line[match.end():])
            label = next_link.group(1).strip() if next_link else "linked item"
            findings.append(f"line {line_number}: {match.group(1).lower()} before {label}")
    return findings


def markdown_headings(text: str) -> list[tuple[int, str]]:
    """Return Markdown heading levels and normalized visible labels."""
    text = re.sub(r"(?s)(`{3,}|~{3,}).*?\1", " ", text)
    headings = []
    for match in re.finditer(r"(?m)^\s{0,3}(#{1,6})[ \t]+(.+?)\s*#*\s*$", text):
        label = re.sub(r"!?(?:\[([^\]]*)\]\([^)]*\))", r"\1", match.group(2))
        headings.append((len(match.group(1)), normalize(label)))
    return headings


def hugo_github_heading_ids(text: str) -> list[tuple[str, bool]]:
    """Approximate Hugo's configured GitHub heading IDs for source alignment."""
    text = re.sub(r"(?s)(`{3,}|~{3,}).*?\1", " ", text)
    result: list[tuple[str, bool]] = []
    seen: dict[str, int] = {}
    for match in re.finditer(r"(?m)^\s{0,3}(#{1,6})[ \t]+(.+?)\s*#*\s*$", text):
        raw_heading = match.group(2)
        explicit = re.search(r"\s*\{#([^}\s]+)\}\s*$", raw_heading)
        if explicit:
            result.append((explicit.group(1), True))
            continue
        label = visible_text(raw_heading).strip().lower()
        anchor = []
        for char in label:
            category = unicodedata.category(char)
            if char == "-" or category[0] in {"L", "N"}:
                anchor.append(char)
            elif category[0] == "M":
                # Goldmark's GitHub-compatible anchorization drops combining marks.
                continue
            elif char.isspace():
                anchor.append("-")
        base_id = "".join(anchor)
        duplicate_index = seen.get(base_id, 0)
        seen[base_id] = duplicate_index + 1
        result.append((base_id if duplicate_index == 0 else f"{base_id}-{duplicate_index}", False))
    return result


def localized_fragment_targets_match(source: str, target: str) -> bool:
    """Accept changed relative fragments only when they target aligned headings."""
    source_links = markdown_links(source)
    target_links = markdown_links(target)
    if len(source_links) != len(target_links):
        return False
    source_headings = hugo_github_heading_ids(source)
    target_headings = hugo_github_heading_ids(target)
    if (
        len(source_headings) != len(target_headings)
    ):
        return False
    target_by_source_id = {
        source_id: target_id
        for (source_id, source_explicit), (target_id, target_explicit)
        in zip(source_headings, target_headings)
        if not source_explicit and not target_explicit
    }
    for (_, source_url), (_, target_url) in zip(source_links, target_links):
        if source_url == target_url:
            continue
        source_parts = urlsplit(source_url)
        target_parts = urlsplit(target_url)
        if (
            source_parts.scheme or source_parts.netloc
            or target_parts.scheme or target_parts.netloc
            or source_parts.path or target_parts.path
            or source_parts.query != target_parts.query
            or not source_parts.fragment or not target_parts.fragment
        ):
            return False
        source_fragment = unquote(source_parts.fragment)
        target_fragment = unquote(target_parts.fragment)
        if target_by_source_id.get(source_fragment) != target_fragment:
            return False
    return True


def markdown_structure(text: str) -> dict[str, object]:
    """Return source-aligned Markdown shape signals for manual comparison."""
    def table_cell_count(line: str) -> int | None:
        stripped = line.strip()
        if "|" not in stripped:
            return None
        cells = re.split(r"(?<!\\)\|", stripped)
        if stripped.startswith("|"):
            cells = cells[1:]
        if stripped.endswith("|"):
            cells = cells[:-1]
        return len(cells) if cells else None

    def is_table_separator(line: str) -> bool:
        stripped = line.strip()
        if "|" not in stripped:
            return False
        cells = re.split(r"(?<!\\)\|", stripped)
        if stripped.startswith("|"):
            cells = cells[1:]
        if stripped.endswith("|"):
            cells = cells[:-1]
        return bool(cells) and all(re.fullmatch(r"\s*:?-{3,}:?\s*", cell) for cell in cells)

    heading_levels: list[int] = []
    fence_languages: list[str] = []
    unordered_items = 0
    ordered_items = 0
    section_items: list[dict[str, int]] = [{"ordered": 0, "unordered": 0}]
    table_shapes: list[list[int]] = []
    visible_lines: list[str] = []
    in_fence = False
    fence_char = ""
    fence_length = 0

    lines = text.splitlines()
    line_index = 0
    while line_index < len(lines):
        line = lines[line_index]
        fence = re.match(r"^\s*(`{3,}|~{3,})\s*([^\s`~]*)", line)
        if fence:
            marker = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_length = len(marker)
                fence_languages.append(fence.group(2).lower())
            elif marker[0] == fence_char and len(marker) >= fence_length:
                in_fence = False
                fence_char = ""
                fence_length = 0
            line_index += 1
            continue
        if in_fence:
            line_index += 1
            continue

        header_cells = table_cell_count(line)
        if (
            header_cells
            and line_index + 1 < len(lines)
            and is_table_separator(lines[line_index + 1])
            and table_cell_count(lines[line_index + 1]) == header_cells
        ):
            table = [header_cells, header_cells]
            visible_lines.extend((line, lines[line_index + 1]))
            line_index += 2
            while line_index < len(lines):
                row = lines[line_index]
                if re.match(r"^\s*(`{3,}|~{3,})", row):
                    break
                cells = table_cell_count(row)
                if cells != header_cells:
                    break
                table.append(cells)
                visible_lines.append(row)
                line_index += 1
            table_shapes.append(table)
            continue

        visible_lines.append(line)

        heading = re.match(r"^\s{0,3}(#{1,6})[ \t]+", line)
        if heading:
            heading_levels.append(len(heading.group(1)))
            section_items.append({"ordered": 0, "unordered": 0})

        list_item = re.match(r"^\s*(?P<marker>[-+*]|\d+[.)])\s+", line)
        if list_item:
            if list_item.group("marker")[0].isdigit():
                ordered_items += 1
                section_items[-1]["ordered"] += 1
            else:
                unordered_items += 1
                section_items[-1]["unordered"] += 1

        line_index += 1

    emphasis_markdown = re.sub(
        r"(?m)^\s*_{3,}\s*$", " ", "\n".join(visible_lines)
    )
    emphasis_markdown = re.sub(r"`+[^`\n]*`+", " ", emphasis_markdown)
    strong_emphasis_markers = len(
        re.findall(r"(?<!\\)(?:\*\*|__)", emphasis_markdown)
    )

    return {
        "heading_levels": heading_levels,
        "table_shapes": table_shapes,
        "strong_emphasis_markers": strong_emphasis_markers,
        "ordered_items": ordered_items,
        "unordered_items": unordered_items,
        "section_items": section_items,
        "fence_languages": fence_languages,
        "link_targets": [target for _, target in markdown_links(text)],
        "shortcodes": re.findall(r"\{\{[<%]\s*([\w-]+)", "\n".join(visible_lines)),
    }


def markdown_structure_differences(source: str, target: str) -> dict[str, tuple[object, object]]:
    """Find Markdown shape differences that need human inspection."""
    source_shape = markdown_structure(source)
    target_shape = markdown_structure(target)
    differences = {
        key: (source_shape[key], target_shape[key])
        for key in source_shape
        if source_shape[key] != target_shape[key]
    }
    if "link_targets" in differences and localized_fragment_targets_match(source, target):
        differences.pop("link_targets")
    return differences


TABLE_SHARED_TERMS = {"ca": {"cost"}, "fr": {"performance"}, "ro": {"cost"}}
TABLE_FIXED_NAMES = {
    "azure",
    "server 2019",
    "defender for cloud",
    "pci dss level 1",
    "sql database database for mysql postgresql",
    "cache for redis",
    "speech to text text to speech",
    "database for postgresql",
    "migrate for compute engine",
    "n a",
    "n a bigquery dataplex",
}


def copied_english_table_cells(
    source: str, target: str, locale: str | None = None
) -> list[str]:
    """Queue unchanged descriptive table cells for human review."""
    def tables(text: str) -> list[list[list[str]]]:
        lines = text.splitlines()
        result: list[list[list[str]]] = []
        in_fence = False
        fence_char = ""
        fence_length = 0

        def cells(line: str) -> list[str] | None:
            stripped = line.strip()
            if "|" not in stripped:
                return None
            parts = re.split(r"(?<!\\)\|", stripped)
            if stripped.startswith("|"):
                parts = parts[1:]
            if stripped.endswith("|"):
                parts = parts[:-1]
            return [part.strip() for part in parts] if parts else None

        def separator(line: str) -> bool:
            parts = cells(line)
            return bool(parts) and all(
                re.fullmatch(r":?-{3,}:?", cell) for cell in parts
            )

        i = 0
        while i < len(lines):
            line = lines[i]
            fence = re.match(r"^\s*(`{3,}|~{3,})", line)
            if fence:
                marker = fence.group(1)
                if not in_fence:
                    in_fence = True
                    fence_char = marker[0]
                    fence_length = len(marker)
                elif marker[0] == fence_char and len(marker) >= fence_length:
                    in_fence = False
                i += 1
                continue
            if in_fence:
                i += 1
                continue
            header = cells(line)
            if (
                header
                and i + 1 < len(lines)
                and separator(lines[i + 1])
                and len(cells(lines[i + 1]) or []) == len(header)
            ):
                table = [header]
                i += 2
                while i < len(lines):
                    row = cells(lines[i])
                    if not row or len(row) != len(header):
                        break
                    table.append(row)
                    i += 1
                result.append(table)
                continue
            i += 1
        return result

    source_tables = tables(source)
    target_tables = tables(target)
    copied = []
    source_cells = {
        normalize(cell)
        for source_table in source_tables
        for row in source_table
        for cell in row
    }
    for table_index, target_table in enumerate(target_tables, start=1):
        for row_index, target_row in enumerate(target_table, start=1):
            for cell_index, target_cell in enumerate(target_row, start=1):
                normalized = normalize(target_cell)
                words = normalized.split()
                openrouter_endpoint_id = (
                    table_index <= len(source_tables)
                    and normalized in {"a", "b"}
                    and any(
                        normalize(header_cell) == "illustrative endpoint"
                        for header_cell in source_tables[table_index - 1][0]
                    )
                    and any(
                        normalize(source_cell) == normalized
                        for source_row in source_tables[table_index - 1][1:]
                        for source_cell in source_row
                    )
                )
                if (
                    normalized
                    and (
                        normalized in source_cells
                        or normalized in TABLE_UNTRANSLATED_GENERIC_LABELS
                    )
                    and words
                    and (
                        normalized in TABLE_UNTRANSLATED_GENERIC_LABELS
                        or any(word in TABLE_ENGLISH_REVIEW_WORDS for word in words)
                    )
                    and normalized not in TABLE_FIXED_NAMES
                    and normalized not in TABLE_SHARED_TERMS.get(locale or "", set())
                    and not openrouter_endpoint_id
                ):
                    copied.append(
                        f"table {table_index}, row {row_index}, cell {cell_index}: {normalized}"
                    )
    return copied


def copied_english_headings(source: str, target: str) -> list[str]:
    """Find unchanged headings or heading fragments for human review."""
    source_labels = {label for _, label in markdown_headings(source)}
    source_words = {
        word
        for label in source_labels
        for word in label.split()
        if len(word) >= 3
    }
    copied = []
    for _, label in markdown_headings(target):
        if label in source_labels and any(char.isalpha() for char in label):
            copied.append(label)
            continue
        target_words = set(label.split())
        copied.extend(
            f"{word} in {label}"
            for word in sorted(source_words & target_words)
        )
    return sorted(set(copied))


FIXED_GLOSSARY_TERMS = {"aws cli", "esim", "ios", "qr code", "qubit"}
GLOSSARY_NAME_EXCEPTIONS = {"amazon web services"}
PARTIAL_EXPANSION_PHRASES = {
    "application programming",
    "as a service",
    "continuous deployment",
    "continuous delivery",
    "continuous integration",
    "one time pad",
    "one time password",
    "secure socket",
    "secure sockets",
    "transport layer",
}
REORDERED_PARTIAL_EXPANSION_PHRASES = {"access control", "backend service"}
LOCALE_EXPANSION_EXCEPTIONS = {"nl": {"bits per", "kilobits per"}}


def fixed_glossary_key(key: str) -> bool:
    """Identify acronym-like or fixed technical glossary keys."""
    candidate = key.strip()
    if normalize(candidate) in FIXED_GLOSSARY_TERMS:
        return True
    if re.fullmatch(r"[A-Z0-9]+(?:/[A-Z0-9]+)*", candidate):
        return any(char.isalpha() for char in candidate)
    return bool(
        re.fullmatch(r"[A-Z][a-z0-9]+[A-Z][A-Za-z0-9]*", candidate)
        or re.fullmatch(r"[A-Z]{2,}[a-z][A-Za-z0-9]*", candidate)
        or re.fullmatch(r"[A-Z][a-z]{1,3}[0-9]+", candidate)
    )


def copied_english_acronym_expansions(
    source: str,
    target: str,
    locale: str | None = None,
    *,
    glossary_page: bool = True,
) -> list[str]:
    """Find fully or substantially copied English glossary expansions."""
    if not glossary_page:
        return []
    entry_pattern = re.compile(
        r"^\s*[-+*]\s+\*\*(?P<key>[^*\n]+)\*\*\s*[:：]\s*(?P<expansion>.+?)\s*$"
    )

    def entries(text: str) -> dict[str, list[tuple[str, str]]]:
        found: dict[str, list[tuple[str, str]]] = {}
        for line in text.splitlines():
            match = entry_pattern.match(line)
            if not match:
                continue
            key = match.group("key").strip()
            if not fixed_glossary_key(key):
                continue
            raw_expansion = visible_text(match.group("expansion"))
            expansion = normalize(raw_expansion)
            if expansion:
                found.setdefault(key, []).append((expansion, raw_expansion))
        return found

    source_entries = entries(source)
    target_entries = entries(target)
    copied = []
    for key, source_expansions in source_entries.items():
        target_expansions = target_entries.get(key, [])
        for (source_expansion, _), (target_expansion, target_raw) in zip(
            source_expansions, target_expansions
        ):
            source_words = source_expansion.split()
            key_words = set(normalize(key).split())
            if len(source_words) < 2 and normalize(key) not in FIXED_GLOSSARY_TERMS:
                continue
            if source_expansion == target_expansion:
                copied.append(f"{key}: {source_expansion}")
                continue
            target_words = target_expansion.split()
            localized_words = [
                word for word in target_words
                if word not in source_words and word not in key_words
            ]
            expected_ranges = SCRIPT_RANGES.get(locale or "", ())
            target_script_letters = sum(
                char.isalpha()
                and any(start <= ord(char) <= end for start, end in expected_ranges)
                for char in target_expansion
            )
            parenthetical_parts = re.findall(r"\([^()]*\)|（[^（）]*）", target_raw)
            if any(source_expansion in normalize(part) for part in parenthetical_parts):
                outside_parentheses = re.sub(
                    r"\([^()]*\)|（[^（）]*）", " ", target_raw
                )
                outside_words = [
                    word for word in normalize(outside_parentheses).split()
                    if word not in source_words and word not in key_words
                ]
                outside_script_letters = sum(
                    char.isalpha()
                    and any(start <= ord(char) <= end for start, end in expected_ranges)
                    for char in outside_parentheses
                )
                outside_compound = any(
                    sum(char.isalpha() for char in word) >= 8
                    for word in outside_words
                )
                sufficient_outside_translation = (
                    len(outside_words) >= 2
                    or outside_script_letters >= 6
                    or (locale in {"de", "nl"} and outside_compound)
                )
                if sufficient_outside_translation:
                    continue
                copied.append(f"{key}: copied phrase {source_expansion}")
                continue
            if source_expansion in target_expansion:
                has_localized_compound = any(
                    sum(char.isalpha() for char in word) >= 8
                    for word in localized_words
                )
                has_dutch_unit_wording = (
                    locale == "nl"
                    and "seconde" in localized_words
                    and any(word in source_words for word in ("bit", "bits", "kilobit", "kilobits"))
                )
                if (
                    len(localized_words) >= 2
                    or target_script_letters >= 6
                    or has_dutch_unit_wording
                    or (locale in {"de", "nl"} and has_localized_compound)
                ):
                    continue
                copied.append(f"{key}: copied phrase {source_expansion}")
                continue
            longest = 0
            longest_phrase = []
            for source_index in range(len(source_words)):
                for target_index in range(len(target_words)):
                    run = 0
                    while (
                        source_index + run < len(source_words)
                        and target_index + run < len(target_words)
                        and source_words[source_index + run] == target_words[target_index + run]
                    ):
                        run += 1
                    phrase = source_words[source_index:source_index + run]
                    phrase_text = " ".join(phrase)
                    if (
                        run > longest
                        and phrase_text not in GLOSSARY_NAME_EXCEPTIONS
                        and phrase_text not in LOCALE_EXPANSION_EXCEPTIONS.get(locale or "", set())
                    ):
                        longest = run
                        longest_phrase = phrase
            phrase = " ".join(longest_phrase)
            has_english_connectors = sum(
                word in ENGLISH_STOPWORDS for word in longest_phrase
            ) >= 2
            target_word_positions = {word: index for index, word in enumerate(target_words)}
            reordered_phrase = next(
                (
                    candidate
                    for candidate in REORDERED_PARTIAL_EXPANSION_PHRASES
                    if all(word in target_word_positions for word in candidate.split())
                    and [target_word_positions[word] for word in candidate.split()]
                    != sorted(target_word_positions[word] for word in candidate.split())
                ),
                None,
            )
            is_version_label = bool(re.fullmatch(r"version \d+(?:\.\d+)*", phrase))
            if (
                longest >= 2
                and longest / len(source_words) >= 0.35
                and not is_version_label
                and (has_english_connectors or phrase in PARTIAL_EXPANSION_PHRASES)
            ):
                copied.append(f"{key}: copied phrase {' '.join(longest_phrase)}")
            elif reordered_phrase:
                copied.append(f"{key}: copied phrase {reordered_phrase}")
    return sorted(set(copied))


def missing_acronym_keys(
    source: str, target: str, *, glossary_page: bool = True
) -> list[str]:
    """Find fixed glossary keys changed or omitted in a translation."""
    if not glossary_page:
        return []
    entry_pattern = re.compile(
        r"^\s*[-+*]\s+\*\*(?P<key>[^*\n]+)\*\*\s*[:：]\s*.+?\s*$"
    )

    def keys(text: str) -> list[str]:
        return [
            match.group("key").strip()
            for line in text.splitlines()
            if (match := entry_pattern.match(line)) and fixed_glossary_key(match.group("key").strip())
        ]

    source_keys = keys(source)
    target_keys = keys(target)
    remaining = target_keys.copy()
    missing = []
    for key in source_keys:
        if key in remaining:
            remaining.remove(key)
        else:
            missing.append(key)
    return sorted(set(missing))


def prose_sentences(text: str) -> set[str]:
    """Return normalized reader-facing sentences outside code and markup."""
    visible = visible_text(text, include_link_labels=False)
    return {
        normalize(part)
        for part in re.split(r"(?<=[.!?])\s+|\n+", visible)
        if len(normalize(part).split()) >= 8
    }


def reader_prose_paragraphs(text: str) -> set[str]:
    """Return substantial reader-facing paragraphs and list items, excluding code."""
    prose = strip_fenced_blocks(text)
    paragraphs = set()
    for part in re.split(r"\n\s*\n", prose):
        raw = part.strip()
        if not raw:
            continue
        lines = [line.strip() for line in raw.splitlines() if line.strip()]
        # Tables often mix localized labels with model names, units, and
        # figures. The copied-table-cell screen is more precise here.
        if lines and all(line.startswith("|") for line in lines):
            continue
        candidates = []
        if lines and all(re.match(r"(?:[-+*]\s|\d+[.)]\s)", line) for line in lines):
            candidates.extend(lines)
        else:
            candidates.append(raw)
        for candidate in candidates:
            line = candidate.strip()
            if line.startswith(("#", ">", "|", "{{<", "{{%")):
                continue
            list_item = bool(re.match(r"(?:[-+*]|\d+[.)])\s", line))
            prose_around_links = re.sub(r"!?\[[^\]]*\]\([^)]+\)", " ", line)
            if list_item and "](" in line and len(normalize(prose_around_links).split()) < 8:
                # Linked product and bibliography lists mostly contain official names.
                continue
            title_words = re.findall(r"\b[A-Za-z][A-Za-z0-9'-]*\b", line)
            capitalized_words = sum(word[0].isupper() for word in title_words)
            if list_item and title_words and capitalized_words / len(title_words) >= 0.6:
                # Title-cased list entries are commonly document or product names.
                continue
            line = re.sub(r"^(?:[-+*]|\d+[.)])\s+", "", line)
            normalized = normalize(visible_text(line))
            words = re.findall(r"[a-z]+(?:'[a-z]+)?", normalized)
            if len(words) < 12:
                continue
            english_signals = sum(word in ENGLISH_STOPWORDS for word in words)
            if english_signals >= 3 and english_signals / len(words) >= 0.16:
                paragraphs.add(normalized)
    return paragraphs


def copied_english_prose_paragraphs(source: str, target: str) -> list[str]:
    """Find unchanged English paragraphs in reader-facing prose outside examples."""
    copied = reader_prose_paragraphs(source) & reader_prose_paragraphs(target)
    return sorted(copied)


def copied_english_opening(source: str, target: str) -> str:
    """Queue every unchanged opening for manual review."""
    def first_paragraph(text: str) -> str:
        for paragraph in re.split(r"\n\s*\n", text):
            visible = normalize(visible_text(paragraph))
            if visible:
                return visible
        return ""

    source_opening = first_paragraph(source)
    target_opening = first_paragraph(target)
    words = source_opening.split()
    if (
        source_opening
        and source_opening == target_opening
        and len(words) >= 2
    ):
        return source_opening
    return ""


def prose_sentences_with_link_slots(text: str) -> set[str]:
    """Return sentences with inline links replaced by neutral slots.

    This exposes copied English around retained product and organization links
    without requiring their labels to be translated or counted as prose.
    """
    slotted = re.sub(r"!?\[([^\]]*)\]\([^)]+\)", " LINK_SLOT ", text)
    visible = visible_text(slotted)
    return {
        normalize(part)
        for part in re.split(r"(?<=[.!?])\s+|\n+", visible)
        if len(normalize(part).split()) >= 5
        and sum(word in ENGLISH_STOPWORDS for word in normalize(part).split()) >= 2
    }


def copied_english_prose_spans(source: str, target: str) -> set[str]:
    """Find unchanged English spans, including clauses attached to proper names."""
    def windows(text: str) -> set[tuple[str, ...]]:
        result: set[tuple[str, ...]] = set()
        # Link labels have their own comparison and often retain official book,
        # product, or organization names. Do not count them as copied prose.
        prose = visible_text(text, include_link_labels=False)
        for sentence in re.split(r"(?<=[.!?])\s+|\n+", prose):
            words = re.findall(r"[a-z]+(?:'[a-z]+)?", sentence.lower())
            for start in range(max(0, len(words) - 7)):
                span = tuple(words[start:start + 8])
                if len(span) == 8 and sum(word in ENGLISH_STOPWORDS for word in span) >= 3:
                    result.add(span)
            # Short English clauses can remain embedded in translated sentences.
            # For five-to-seven-word spans, require several stopwords or a finite
            # verb pattern. This avoids treating formal names such as "National
            # Institute of Standards and Technology" as copied prose.
            for size in range(5, 8):
                for start in range(max(0, len(words) - size + 1)):
                    span = tuple(words[start:start + size])
                    stopword_count = sum(word in ENGLISH_STOPWORDS for word in span)
                    conjunction_fragment = span[0] in {"and", "or", "but"}
                    in_clause_verb = any(
                        word in {"is", "are", "was", "were", "has", "have", "should", "can", "will"}
                        and index < len(span) - 1
                        for index, word in enumerate(span)
                    )
                    if stopword_count >= 3 or in_clause_verb or conjunction_fragment:
                        result.add(span)
            # Three- and four-word clauses need a stronger grammatical signal.
            # Subject pronouns plus multiple stopwords catch cases such as
            # "They matter to you". A be-verb with a following content word
            # catches short passive clauses such as "data is collected online".
            for size in range(3, 5):
                for start in range(max(0, len(words) - size + 1)):
                    span = tuple(words[start:start + size])
                    stopword_count = sum(word in ENGLISH_STOPWORDS for word in span)
                    pronoun_clause = (
                        any(word in {"i", "you", "he", "she", "it", "we", "they"} for word in span)
                        and stopword_count >= 2
                    )
                    be_clause = any(
                        word in {"is", "are", "was", "were"}
                        and index < len(span) - 1
                        and span[index + 1] not in ENGLISH_STOPWORDS
                        for index, word in enumerate(span)
                    )
                    if pronoun_clause or be_clause:
                        result.add(span)
        return result

    matches = windows(source) & windows(target)
    copied_connectors = {
        span[0] for span in matches if span[0] in {"and", "or", "but"}
    }
    phrases = {" ".join(span) for span in matches}
    # Overlapping windows describe the same copied fragment. Keep only the
    # longest candidate so reports do not multiply one name or clause.
    return copied_connectors | {
        phrase for phrase in phrases
        if phrase.split()[0] not in {"and", "or", "but"}
        and not any(phrase != other and phrase in other for other in phrases)
    }


def copied_english_mixed_phrases(source: str, target: str, locale: str) -> list[str]:
    """Find exact English source phrases embedded in non-Latin translations."""
    if locale not in SCRIPT_RANGES:
        return []

    word_pattern = re.compile(r"[A-Za-z][A-Za-z0-9'-]*")

    def phrases(text: str) -> dict[tuple[tuple[str, ...], tuple[bool, ...]], str]:
        found: dict[tuple[tuple[str, ...], tuple[bool, ...]], str] = {}
        for line in visible_text(text).splitlines():
            matches = list(word_pattern.finditer(line))
            words = [match.group() for match in matches]
            letter_counts = [
                sum(char.isascii() and char.isalpha() for char in word)
                for word in words
            ]
            for size in range(2, 7):
                for start in range(max(0, len(words) - size + 1)):
                    original = words[start:start + size]
                    if sum(count >= 3 for count in letter_counts[start:start + size]) < 2:
                        continue
                    # Multiword title case is usually an official name or
                    # product label; dedicated checks cover reviewed generic
                    # labels that use this capitalization.
                    if sum(word[:1].isupper() for word in original) > 1:
                        continue
                    # Do not join words separated by commas, parentheses,
                    # Markdown table cells, or other punctuation. Such joins
                    # create false matches between product names in lists.
                    if any(
                        not all(
                            char.isspace() or char == "-"
                            for char in line[matches[index].end():matches[index + 1].start()]
                        )
                        for index in range(start, start + size - 1)
                    ):
                        continue
                    key = (
                        tuple(word.lower() for word in original),
                        tuple(word[:1].isupper() for word in original),
                    )
                    found.setdefault(key, " ".join(original))
        return found

    source_phrases = phrases(source)
    target_phrases = phrases(target)
    matches = source_phrases.keys() & target_phrases.keys()
    return sorted(
        source_phrases[key]
        for key in matches
        if " ".join(key[0]) not in MIXED_PHRASE_FIXED_VALUES
    )


def copied_english_generic_terms(source: str, target: str, locale: str) -> list[str]:
    """Find reviewed generic technical descriptors copied verbatim from English."""
    source_text = visible_text(source)
    target_text = visible_text(target)
    findings = []
    for term in GENERIC_ENGLISH_TECHNICAL_TERMS:
        pattern = re.escape(term).replace(r"\ ", r"\s+")
        boundary = rf"(?<![A-Za-z0-9]){pattern}(?![A-Za-z0-9])"
        accepted_compound = any(
            re.search(
                rf"(?<![A-Za-z0-9]){re.escape(compound)}(?![A-Za-z])",
                target_text,
                re.I,
            )
            for compound in ACCEPTED_GENERIC_TECHNICAL_COMPOUNDS.get(locale, set())
        )
        if term == "multi-gigabit" and accepted_compound:
            continue
        if re.search(boundary, source_text, re.I) and re.search(boundary, target_text, re.I):
            findings.append(term)
    return sorted(findings)


def english_dominant_paragraphs(text: str, locale: str) -> list[str]:
    """Screen for English paragraphs inside otherwise translated articles.

    This is a review queue, not a language verdict. Short paragraphs use a
    higher English-signal threshold because names and technical labels dominate
    their word counts.
    """
    locale_words = LOCALE_STOPWORDS.get(locale, set())
    findings = []
    for part in re.split(r"\n\s*\n", visible_text(text, include_link_labels=False)):
        paragraph = normalize(part)
        tokens = re.findall(r"[a-z]+(?:'[a-z]+)?", paragraph.lower())
        if len(tokens) < 5:
            continue
        english_ratio = sum(word in ENGLISH_STOPWORDS for word in tokens) / len(tokens)
        locale_ratio = sum(word in locale_words for word in tokens) / len(tokens)
        expected_script = script_ratio(paragraph, locale)
        # Count English signals among Latin words independently of surrounding
        # script. A short run of Chinese, Arabic, or Indic text can otherwise
        # hide a full English clause by pushing the paragraph-wide script ratio
        # above the threshold. Product names alone usually lack stopword density.
        locale_signal_is_weak = (
            True if expected_script is not None else locale_ratio < 0.10
        )
        if expected_script is not None and len(tokens) >= 15:
            english_threshold = 0.25
        elif len(tokens) < 10:
            english_threshold = 0.40
        else:
            english_threshold = 0.35 if len(tokens) < 30 else 0.28
        if english_ratio >= english_threshold and locale_signal_is_weak:
            findings.append(paragraph)
    return findings


def high_confidence_english_paragraphs(text: str, locale: str) -> list[str]:
    """Find substantial English reader prose while excluding names and citations.

    The broader paragraph screen intentionally flags mixed-script technical
    prose for manual review. This stricter result blocks only substantial prose
    paragraphs with English stopword density, weak target-language signals, and
    little or no expected script. It strips linked labels, skips bibliography
    sections, and excludes code, headings, tables, and title-cased reference
    entries.
    """
    locale_words = LOCALE_STOPWORDS.get(locale, set())
    findings = []
    in_references = False
    parts = []
    current = []
    for line in strip_fenced_blocks(text).splitlines():
        if re.match(r"^ {0,3}#{1,6}\s", line):
            if current:
                parts.append("\n".join(current))
                current = []
            parts.append(line)
        elif not line.strip():
            if current:
                parts.append("\n".join(current))
                current = []
        else:
            current.append(line)
    if current:
        parts.append("\n".join(current))

    for part in parts:
        raw = part.strip()
        if not raw:
            continue
        lines = [line.strip() for line in raw.splitlines() if line.strip()]
        if lines and all(line.startswith("|") for line in lines):
            continue
        heading_lines = [line for line in lines if line.startswith("#")]
        if heading_lines:
            in_references = is_reference_heading(
                re.sub(r"^#{1,6}\s*", "", heading_lines[-1])
            )
            if in_references or len(lines) == 1:
                continue
        if in_references:
            continue
        list_item = bool(re.match(r"(?:[-+*]|\d+[.)])\s", raw))
        if list_item:
            title_words = re.findall(r"\b[A-Za-z][A-Za-z0-9'-]*\b", raw)
            capitalized = sum(word[0].isupper() for word in title_words)
            if title_words and capitalized / len(title_words) >= 0.6:
                continue
        paragraph = normalize(visible_text(raw, include_link_labels=False))
        # Keep accented Latin words intact. Dropping them makes some localized
        # prose look English-heavy because short words overlap with English
        # stopwords.
        tokens = re.findall(r"[^\W\d_]+(?:'[^\W\d_]+)?", paragraph.lower())
        if len(tokens) < 12:
            continue
        english_signals = sum(word in ENGLISH_STOPWORDS for word in tokens)
        english_ratio = english_signals / len(tokens)
        locale_ratio = sum(word in locale_words for word in tokens) / len(tokens)
        expected_script = script_ratio(paragraph, locale)
        if expected_script is not None and expected_script >= 0.20:
            continue
        if english_signals >= 3 and english_ratio >= 0.22 and locale_ratio < 0.10:
            findings.append(paragraph)
    return sorted(findings)


def copied_english_reader_verbs(source: str, target: str, locale: str = "") -> list[str]:
    """Find common English reader prose verbs copied into translated paragraphs."""
    source_words = set(re.findall(r"[a-z]+", visible_text(source, include_link_labels=False).lower()))
    findings = []
    for part in re.split(r"\n\s*\n", strip_fenced_blocks(target)):
        raw = part.strip()
        lines = [line.strip() for line in raw.splitlines() if line.strip()]
        if not raw or any(line.startswith(("#", "|")) for line in lines):
            continue
        paragraph = normalize(visible_text(raw, include_link_labels=False))
        tokens = re.findall(r"[a-z]+(?:'[a-z]+)?", paragraph.lower())
        if len(tokens) < 8:
            continue
        copied = sorted(
            ENGLISH_READER_VERBS.intersection(tokens, source_words)
            - LOCALE_READER_VERB_HOMOGRAPHS.get(locale, set())
        )
        if copied:
            findings.extend(f"{word}: {paragraph}" for word in copied)
    return sorted(set(findings))


def script_ratio(text: str, locale: str) -> float | None:
    ranges = SCRIPT_RANGES.get(locale)
    if not ranges:
        return None
    letters = [char for char in text if char.isalpha()]
    if not letters:
        return 0.0
    return sum(any(start <= ord(char) <= end for start, end in ranges) for char in letters) / len(letters)


def report_path(path: Path) -> str:
    """Keep repo paths readable while allowing temporary candidate bundles."""
    resolved = path.resolve()
    try:
        return resolved.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return resolved.as_posix()


def english_dominant_body(text: str, locale: str) -> bool:
    """Block a body when English-dominant paragraphs make up most of it."""
    paragraphs = [
        normalize(part)
        for part in re.split(r"\n\s*\n", visible_text(text, include_link_labels=False))
        if normalize(part)
    ]
    findings = set(english_dominant_paragraphs(text, locale))
    total_tokens = 0
    english_tokens = 0
    for paragraph in paragraphs:
        tokens = re.findall(r"[a-z]+(?:'[a-z]+)?", paragraph.lower())
        total_tokens += len(tokens)
        if paragraph in findings:
            english_tokens += len(tokens)
    return total_tokens >= 8 and english_tokens / total_tokens >= 0.65


def published(metadata: dict) -> bool:
    if metadata.get("draft") is True:
        return False
    value = metadata.get("date")
    try:
        if isinstance(value, dt.datetime):
            value = value.date()
        elif isinstance(value, str):
            value = dt.date.fromisoformat(value[:10])
        return not isinstance(value, dt.date) or value <= dt.date.today()
    except (TypeError, ValueError):
        return True


def audit_bundle(source: Path, locales: list[str]) -> list[dict[str, str]]:
    source_meta, source_body = read_page(source)
    if not published(source_meta):
        return []
    source_paragraphs = {
        normalize(part)
        for part in re.split(r"\n\s*\n", visible_text(source_body))
        if len(normalize(part).split()) >= 12
    }
    source_sentences = prose_sentences(source_body)
    findings: list[dict[str, str]] = []
    for locale in locales:
        target = source.with_name(f"index.{locale}.md")
        misplaced = False
        if not target.is_file():
            alternatives = sorted(source.parent.rglob(f"index.{locale}.md"))
            alternatives = [path for path in alternatives if path != source]
            if not alternatives:
                findings.append({
                    "path": report_path(target),
                    "locale": locale,
                    "reasons": "translation_missing",
                    "tokens": "0",
                    "english_stopword_ratio": "0.000",
                    "locale_stopword_ratio": "0.000",
                    "exact_english_paragraphs": "0/0",
                    "expected_script_ratio": "",
                    "note": "Configured locale file is missing.",
                })
                continue
            target = alternatives[0]
            misplaced = True
        metadata, body = read_page(target)
        prose = visible_text(body)
        source_prose = visible_text(source_body)
        copied_body = (
            normalize(prose)
            if normalize(source_prose)
            and normalize(prose) == normalize(source_prose)
            else ""
        )
        tokens = re.findall(r"[a-z]+(?:'[a-z]+)?", prose.lower())
        english_ratio = sum(word in ENGLISH_STOPWORDS for word in tokens) / max(1, len(tokens))
        locale_words = LOCALE_STOPWORDS.get(locale, set())
        locale_ratio = sum(word in locale_words for word in tokens) / max(1, len(tokens))
        paragraphs = [
            normalize(part)
            for part in re.split(r"\n\s*\n", prose)
            if len(normalize(part).split()) >= 12
        ]
        exact = sum(part in source_paragraphs for part in paragraphs)
        exact_ratio = exact / max(1, len(paragraphs))
        copied_sentences = sorted(prose_sentences(body) & source_sentences)
        linked_source_sentences = prose_sentences_with_link_slots(source_body)
        linked_target_sentences = prose_sentences_with_link_slots(body)
        copied_sentences.extend(sorted(linked_source_sentences & linked_target_sentences))
        copied_sentences = sorted(set(copied_sentences))
        copied_sentences = [
            sentence for sentence in copied_sentences
            if sum(word in ENGLISH_STOPWORDS for word in sentence.split()) >= 2
        ]
        copied_spans = copied_english_prose_spans(source_body, body)
        copied_mixed_phrases = copied_english_mixed_phrases(source_body, body, locale)
        copied_generic_terms = copied_english_generic_terms(source_body, body, locale)
        copied_prose_paragraphs = copied_english_prose_paragraphs(source_body, body)
        english_paragraphs = english_dominant_paragraphs(body, locale)
        high_confidence_english_paragraphs_found = high_confidence_english_paragraphs(body, locale)
        copied_reader_verbs = copied_english_reader_verbs(source_body, body, locale)
        english_body_fallback = english_dominant_body(body, locale)
        copied_table_cells = copied_english_table_cells(source_body, body, locale)
        copied_headings = copied_english_headings(source_body, body)
        source_title = normalize(str(source_meta.get("title", "")))
        is_glossary_page = "glossary" in source_title or "acronym" in source_title
        copied_acronym_expansions = copied_english_acronym_expansions(
            source_body, body, locale, glossary_page=is_glossary_page
        )
        inline_acronym_blockers, inline_acronym_reviews = (
            copied_english_inline_acronym_expansions(source_body, body, locale)
        )
        copied_acronym_expansions.extend(inline_acronym_blockers)
        copied_acronym_expansions = sorted(set(copied_acronym_expansions))
        missing_acronym_keys_found = missing_acronym_keys(
            source_body, body, glossary_page=is_glossary_page
        )
        structure_differences = markdown_structure_differences(source_body, body)
        ratio = script_ratio(prose, locale)
        reasons = []
        copied_opening = copied_english_opening(source_body, body)
        title = str(metadata.get("title", ""))
        english_title_fallback = english_dominant_title(title, locale)
        english_title_review = english_dominant_title_review(title, locale)
        source_title_text = str(source_meta.get("title", ""))
        title_matches_source = normalize(title) == normalize(source_title_text)
        if copied_opening:
            reasons.append("copied_english_opening")
        if title_matches_source and (english_title_fallback or english_title_review):
            reasons.append("english_dominant_title_review")
        elif english_title_fallback:
            reasons.append("high_confidence_english_title")
        elif english_title_review:
            reasons.append("english_dominant_title_review")
        source_comparison_title = re.sub(r"\bVS Code\b", " ", source_title_text, flags=re.I)
        target_comparison_title = re.sub(r"\bVS Code\b", " ", title, flags=re.I)
        source_has_vs = re.search(r"\bvs\.?(?=\s|$|[,:;!?])", source_comparison_title, flags=re.I)
        target_has_vs = re.search(r"\bvs\.?(?=\s|$|[,:;!?])", target_comparison_title, flags=re.I)
        if source_has_vs and target_has_vs and not title_matches_source:
            reasons.append("copied_english_title_comparator")
        if copied_body:
            reasons.append("copied_english_body")
        if misplaced:
            reasons.append("translation_not_beside_source")
        copied_metadata = [
            key for key in ("title", "description", "coverAlt", "coverCaption")
            if isinstance(metadata.get(key), str)
            and isinstance(source_meta.get(key), str)
            and len(normalize(str(source_meta[key])).split()) >= {
                "title": 3,
                "description": 1,
                "coverAlt": 2,
                "coverCaption": 2,
            }[key]
            and normalize(str(metadata[key])) == normalize(str(source_meta[key]))
        ]
        if copied_metadata:
            reasons.append("copied_english_metadata")
        if any(key in copied_metadata for key in ("description", "coverAlt", "coverCaption")):
            reasons.append("copied_english_reader_metadata")
        copied_taxonomy = copied_english_taxonomy(source_meta, metadata)
        copied_generic_taxonomy = copied_generic_english_taxonomy(
            source_meta, metadata, locale
        )
        taxonomy_counts = taxonomy_count_differences(source_meta, metadata)
        metadata_keys = copied_metadata + sorted(copied_taxonomy)
        if len(prose.strip()) < 30:
            reasons.append("empty_or_nearly_empty")
        if exact >= 3 and exact_ratio >= 0.35:
            reasons.append("many_exact_English_paragraphs")
        if copied_reader_fenced_examples(source_body, body):
            reasons.append("copied_reader_fenced_example")
        copied_fence_lines = sorted(copied_reader_fenced_lines(source_body, body))
        if copied_fence_lines:
            reasons.append("copied_reader_fenced_line")
        copied_fence_formulas = copied_english_fenced_formulas(source_body, body)
        if copied_fence_formulas:
            reasons.append("copied_english_fenced_formula")
        copied_unlabeled_fence = sorted(copied_unlabeled_fence_lines(source_body, body))
        if copied_unlabeled_fence:
            reasons.append("copied_unlabeled_fence_line")
        copied_code_prose = sorted(copied_reader_code_prose(source_body, body))
        if copied_code_prose:
            reasons.append("copied_reader_code_prose")
        english_code_fallback = english_reader_code_prose_fallback(source_body, body)
        if english_code_fallback:
            reasons.append("English_reader_code_prose_fallback")
        split_emphasis = split_word_emphasis(body, locale)
        if split_emphasis:
            reasons.append("markdown_split_word_emphasis")
        if copied_sentences:
            reasons.append("exact_English_sentences")
        if copied_spans:
            reasons.append("copied_English_prose_span")
        if copied_mixed_phrases:
            reasons.append("copied_english_mixed_phrase_review")
            if len(copied_mixed_phrases) >= MIXED_PHRASE_STRICT_BLOCKER_THRESHOLD:
                reasons.append("high_density_copied_english_mixed_phrases")
        if copied_generic_terms:
            reasons.append("copied_english_generic_term")
        if copied_prose_paragraphs:
            reasons.append("copied_english_prose_paragraph")
        if english_paragraphs:
            reasons.append("English_dominant_reader_paragraph")
        if high_confidence_english_paragraphs_found:
            reasons.append("high_confidence_english_paragraph")
        if copied_reader_verbs:
            reasons.append("copied_english_reader_verb")
        if english_body_fallback:
            reasons.append("English_dominant_reader_body")
        if copied_table_cells:
            reasons.append("English_reader_table_cell_copy")
        if copied_headings:
            reasons.append("English_reader_heading_copy")
        if copied_acronym_expansions:
            reasons.append("copied_english_acronym_expansion")
        if inline_acronym_reviews:
            reasons.append("copied_english_acronym_expansion_review")
        if missing_acronym_keys_found:
            reasons.append("missing_acronym_key")
        if len(tokens) >= 120 and english_ratio >= 0.22 and locale_ratio < 0.12:
            reasons.append("English_stopword_dominance")
        if ratio is not None and len(prose) > 500 and ratio < 0.08:
            reasons.append("expected_script_missing")
        if metadata_keys:
            reasons.append("English_reader_metadata_copy:" + ",".join(metadata_keys))
        if copied_generic_taxonomy:
            reasons.append("copied_generic_english_taxonomy")
        if taxonomy_counts:
            reasons.append("taxonomy_count_mismatch:" + ",".join(sorted(taxonomy_counts)))
        copied_link_labels = copied_english_link_labels(source_body, body)
        copied_generic_link_labels = copied_english_generic_link_labels(
            source_body, body, locale
        )
        if copied_link_labels:
            reasons.append("English_reader_link_label_copy")
        if copied_generic_link_labels:
            reasons.append("copied_english_generic_link_label")
        copied_shortcode_descriptions = copied_english_shortcode_descriptions(source_body, body)
        if copied_shortcode_descriptions:
            reasons.append("copied_english_shortcode_description")
        copied_internal_link_labels = copied_english_internal_link_labels(
            source_body, body, locale
        )
        if copied_internal_link_labels:
            reasons.append("copied_english_internal_link_label")
        copied_link_connectors = copied_english_link_connectors(body)
        if copied_link_connectors:
            reasons.append("copied_english_link_connector")
        for key in structure_differences:
            reasons.append(f"markdown_{key}_mismatch")
        if reasons:
            findings.append({
                "path": report_path(target),
                "locale": locale,
                "reasons": ";".join(reasons),
                "tokens": str(len(tokens)),
                "english_stopword_ratio": f"{english_ratio:.3f}",
                "locale_stopword_ratio": f"{locale_ratio:.3f}",
                "exact_english_paragraphs": f"{exact}/{len(paragraphs)}",
                "exact_english_sentences": " | ".join(copied_sentences),
                "copied_reader_fenced_lines": " | ".join(copied_fence_lines),
                "copied_english_fenced_formulas": " | ".join(copied_fence_formulas),
                "copied_reader_code_prose": " | ".join(copied_code_prose),
                "english_reader_code_prose_fallback": " | ".join(english_code_fallback),
                "copied_unlabeled_fence_lines": " | ".join(copied_unlabeled_fence),
                "copied_english_spans": " | ".join(sorted(copied_spans)),
                "copied_english_mixed_phrases": " | ".join(copied_mixed_phrases),
                "copied_english_generic_terms": " | ".join(copied_generic_terms),
                "split_word_emphasis": " | ".join(split_emphasis),
                "english_dominant_paragraphs": " | ".join(english_paragraphs),
                "high_confidence_english_paragraphs": " | ".join(high_confidence_english_paragraphs_found),
                "copied_english_reader_verbs": " | ".join(copied_reader_verbs),
                "copied_english_table_cells": " | ".join(copied_table_cells),
                "copied_english_headings": " | ".join(copied_headings),
                "copied_english_acronym_expansions": " | ".join(copied_acronym_expansions),
                "copied_english_inline_acronym_expansion_review": " | ".join(
                    inline_acronym_reviews
                ),
                "missing_acronym_keys": " | ".join(missing_acronym_keys_found),
                "copied_english_metadata": " | ".join(
                    [f"{key}: {metadata[key]}" for key in copied_metadata]
                    + [f"{key}: {', '.join(values)}" for key, values in copied_taxonomy.items()]
                ),
                "english_dominant_title": title if english_title_fallback else "",
                "english_dominant_title_review": title if english_title_review else "",
                "taxonomy_count_differences": json.dumps(
                    taxonomy_counts, ensure_ascii=False, sort_keys=True
                ),
                "expected_script_ratio": "" if ratio is None else f"{ratio:.3f}",
                "copied_english_opening": copied_opening,
                "copied_link_labels": " | ".join(copied_link_labels),
                "copied_english_generic_link_labels": " | ".join(copied_generic_link_labels),
                "copied_english_internal_link_labels": " | ".join(copied_internal_link_labels),
                "copied_english_shortcode_descriptions": " | ".join(copied_shortcode_descriptions),
                "copied_english_link_connectors": " | ".join(copied_link_connectors),
                "copied_english_body": copied_body,
                "copied_english_prose_paragraphs": " | ".join(copied_prose_paragraphs),
                "markdown_structure_differences": json.dumps(
                    structure_differences, ensure_ascii=False, sort_keys=True
                ),
                "note": "Screening flag. Review prose and metadata manually.",
            })
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="article bundle directories or index.en.md files")
    parser.add_argument("--all", action="store_true", help="scan all published article bundles")
    parser.add_argument("--csv", type=Path, help="write findings to this CSV path")
    parser.add_argument(
        "--fail-on-english-fallback",
        action="store_true",
        help=(
            "fail on English fallbacks and required taxonomy-count mismatches: an exact English body or prose paragraph, "
            "missing configured translations, source structure mismatches (headings, lists, tables, links, shortcodes, fences, emphasis), "
            "one English-dominant reader paragraph, many copied English paragraphs, "
            "English stopword dominance, changed English-dominant titles, unchanged lowercase "
            "inline acronym expansions without a localized gloss; source-identical titles and "
            "bilingual or "
            "title-case expansions need manual review, copied reader-facing "
            "code text or English calculation labels, copied generic descriptors or link labels, "
            "or a missing target script; also fail when 20 or more distinct source-matched English "
            "phrases appear in a non-Latin translation"
        ),
    )
    args = parser.parse_args()
    if not args.all and not args.paths:
        parser.error("provide article paths or --all")
    try:
        locales = configured_locales()
        sources: set[Path] = set()
        if args.all:
            sources.update(ARTICLES.rglob("index.en.md"))
        for item in args.paths:
            path = (ROOT / item).resolve() if not item.is_absolute() else item.resolve()
            if path.is_dir():
                path = path / "index.en.md"
            if path.name != "index.en.md" or not path.is_file():
                raise ValueError(f"expected an existing index.en.md or article directory: {item}")
            sources.add(path)
        findings = [row for source in sorted(sources) for row in audit_bundle(source, locales)]
    except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
        print(f"translation leakage screen failed: {exc}", file=sys.stderr)
        return 2

    published_source_count = sum(
        1 for source in sources if published(read_page(source)[0])
    )
    if args.fail_on_english_fallback:
        high_confidence = {
            "copied_english_body",
            "copied_english_prose_paragraph",
            "many_exact_English_paragraphs",
            "English_stopword_dominance",
            "English_dominant_reader_body",
            "high_confidence_english_paragraph",
            "high_confidence_english_title",
            "copied_english_reader_verb",
            "expected_script_missing",
            "copied_english_opening",
            "copied_english_fenced_formula",
            "copied_english_link_connector",
            "copied_english_generic_link_label",
            "English_reader_code_prose_fallback",
            "copied_english_acronym_expansion",
            "missing_acronym_key",
            "copied_english_internal_link_label",
            "copied_english_shortcode_description",
            "copied_english_mixed_phrase",
            "high_density_copied_english_mixed_phrases",
            "copied_english_generic_term",
            "copied_english_reader_metadata",
            "English_reader_table_cell_copy",
            "copied_generic_english_taxonomy",
            "taxonomy_count_mismatch",
        }
        blockers = [
            row for row in findings
            if "translation_missing" in row["reasons"].split(";")
            or high_confidence.intersection(row["reasons"].split(";"))
            or any(
                reason.startswith("markdown_") and reason.endswith("_mismatch")
                for reason in row["reasons"].split(";")
            )
            or any(
                reason.startswith("taxonomy_count_mismatch:")
                for reason in row["reasons"].split(";")
            )
        ]
        print(
            f"published bundles scanned: {published_source_count}; configured locales: {len(locales)}; "
            f"strict blockers: {len(blockers)}"
        )
        mixed_phrase_reviews = [
            row for row in findings
            if "copied_english_mixed_phrase_review" in row["reasons"].split(";")
        ]
        print(f"source-matched mixed-script phrase reviews: {len(mixed_phrase_reviews)}")
        for row in mixed_phrase_reviews:
            print(
                f"{row['path']}\t{row['locale']}\t"
                f"{row['copied_english_mixed_phrases']}"
            )
        for row in blockers:
            reasons = [
                reason for reason in row["reasons"].split(";")
                if reason == "translation_missing"
                or reason in high_confidence
                or (reason.startswith("markdown_") and reason.endswith("_mismatch"))
                or reason.startswith("taxonomy_count_mismatch:")
            ]
            print(
                f"{row['path']}\t{','.join(sorted(reasons))}\t"
                f"English paragraphs {row['exact_english_paragraphs']}\t"
                f"EN stopwords {row['english_stopword_ratio']}"
            )
    else:
        print(f"published bundles scanned: {published_source_count}; configured locales: {len(locales)}; flags: {len(findings)}")
        for row in findings:
            print(f"{row['path']}\t{row['reasons']}\tEnglish paragraphs {row['exact_english_paragraphs']}\tEN stopwords {row['english_stopword_ratio']}")
    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(findings)
        print(f"CSV report: {args.csv}")
    if args.fail_on_english_fallback:
        return 1 if blockers else 0
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
