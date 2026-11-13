#!/usr/bin/env python3
"""Screen article translations for copied or English-dominant reader-facing prose.

Run on one or more article bundles, or scan all published article bundles:

    python3 tools/check_translation_english_leakage.py content/articles/<slug>
    python3 tools/check_translation_english_leakage.py --all --csv /tmp/leakage.csv

Findings require human review. A clean screen does not prove translation quality.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import tomllib
import unicodedata
from pathlib import Path



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
LOCALE_STOPWORDS = {
    "ca": set("el la els les un una i o de que en per amb és són es del dels al als sobre com no també si quan".split()),
    "de": set("der die das den dem des ein eine einer und oder zu im vom mit auf für ist sind wird werden nicht aus an bei nach über als dass weil sich von am zum zur auch".split()),
    "es": set("el la los las un una y o de que en para por con es son está están del al como no se también si cuando".split()),
    "fr": set("le la les un une des du et ou de que en pour par avec est sont pas dans sur au aux cette ces comme ne se aussi".split()),
    "it": set("il lo la gli le un una e o di che in per con è sono non del della dei al alla come si anche questo".split()),
    "nl": set("de het een en of van voor met is zijn in op aan niet dat als zich ook naar door deze dit".split()),
    "pl": set("i w z na do jest są nie się oraz albo że dla przez od co jak tego tej także".split()),
    "pt": set("o a os as um uma e ou de que em para por com é são não do da dos das como se também".split()),
    "ro": set("și de în la este sunt cu pentru din nu pe un o că ca aceasta acești".split()),
}
SCRIPT_RANGES = {
    "ar": ((0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF)),
    "bn": ((0x0980, 0x09FF),),
    "hi": ((0x0900, 0x097F),),
    "pa": ((0x0A00, 0x0A7F),),
    "ru": ((0x0400, 0x052F),),
    "ja": ((0x3040, 0x30FF), (0x3400, 0x9FFF)),
    "zh": ((0x3400, 0x9FFF),),
}


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
        value = re.search(rf"(?m)^{re.escape(key)}\s*:\s*(['\"])(.*?)\1\s*$", header)
        if value:
            metadata[key] = value.group(2)
    for key in ("genre", "tags"):
        values = yaml_front_matter_lists(header, key)
        if values:
            metadata[key] = values
    return metadata, match.group(2)


def copied_english_taxonomy(source: dict, target: dict) -> dict[str, list[str]]:
    """Find unchanged multiword genre or tag values for manual review."""
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
            and len(normalize(value).split()) >= 2
            and normalize(value) in target_normalized
        ]
        if values:
            copied[key] = sorted(set(values))
    return copied


def visible_text(text: str, *, include_link_labels: bool = True) -> str:
    # `text` and `plaintext` fences hold reader-facing samples such as prompts,
    # forms, and dialogue. Keep those in the leakage screen. Exclude executable
    # and other fenced content, which often contains literal English identifiers.
    text = re.sub(
        r"(?s)(?P<fence>`{3,}|~{3,})[ \t]*(?P<language>[^\s`~]*)[^\n]*\n(?P<body>.*?)(?:\n)?(?P=fence)",
        lambda match: match.group("body")
        if match.group("language").lower() in {"text", "plaintext"}
        else " ",
        text,
    )
    text = re.sub(r"(?m)^\s*\{\{<.*?>\}\}\s*$", " ", text)
    text = re.sub(r"\{\{<.*?>\}\}", " ", text)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"https?://[^\s)\]>]+", " ", text)
    link_replacement = r"\1" if include_link_labels else " "
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", link_replacement, text)
    text = re.sub(r"<[^>]+>", " ", text)
    return text


def reader_fenced_prose(text: str) -> list[str]:
    """Return complete reader-facing `text`/`plaintext` fenced examples."""
    return [
        match.group("body").strip()
        for match in re.finditer(
            r"(?s)(?P<fence>`{3,}|~{3,})[ \t]*(?P<language>[^\s`~]*)[^\n]*\n(?P<body>.*?)(?:\n)?(?P=fence)",
            text,
        )
        if match.group("language").lower() in {"text", "plaintext"}
    ]


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
    """Find unchanged multiword link labels for manual review."""
    copied = []
    for source_link, target_link in zip(markdown_links(source), markdown_links(target)):
        source_label, source_target = source_link
        target_label, target_target = target_link
        normalized_label = normalize(source_label)
        if (
            source_target == target_target
            and len(normalized_label.split()) >= 2
            and normalized_label == normalize(target_label)
        ):
            copied.append(f"{source_label} => {source_target}")
    return copied


def markdown_headings(text: str) -> list[tuple[int, str]]:
    """Return Markdown heading levels and normalized visible labels."""
    text = re.sub(r"(?s)(`{3,}|~{3,}).*?\1", " ", text)
    headings = []
    for match in re.finditer(r"(?m)^\s{0,3}(#{1,6})[ \t]+(.+?)\s*#*\s*$", text):
        label = re.sub(r"!?(?:\[([^\]]*)\]\([^)]*\))", r"\1", match.group(2))
        headings.append((len(match.group(1)), normalize(label)))
    return headings


def copied_english_headings(source: str, target: str) -> list[str]:
    """Find unchanged descriptive headings that remain in English."""
    source_labels = {label for _, label in markdown_headings(source)}
    copied = []
    for _, label in markdown_headings(target):
        words = label.split()
        if (
            label in source_labels
            and len(words) >= 3
            and any(word in ENGLISH_STOPWORDS for word in words)
        ):
            copied.append(label)
    return sorted(set(copied))


def prose_sentences(text: str) -> set[str]:
    """Return normalized reader-facing sentences outside code and markup."""
    visible = visible_text(text, include_link_labels=False)
    return {
        normalize(part)
        for part in re.split(r"(?<=[.!?])\s+|\n+", visible)
        if len(normalize(part).split()) >= 8
    }


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
    """Find unchanged eight-word English spans inside otherwise translated text."""
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
        return result

    matches = windows(source) & windows(target)
    return {" ".join(span) for span in matches}


def script_ratio(text: str, locale: str) -> float | None:
    ranges = SCRIPT_RANGES.get(locale)
    if not ranges:
        return None
    letters = [char for char in text if char.isalpha()]
    if not letters:
        return 0.0
    return sum(any(start <= ord(char) <= end for start, end in ranges) for char in letters) / len(letters)


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
                    "path": target.relative_to(ROOT).as_posix(),
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
        copied_headings = copied_english_headings(source_body, body)
        ratio = script_ratio(prose, locale)
        reasons = []
        if misplaced:
            reasons.append("translation_not_beside_source")
        copied_metadata = [
            key for key in ("title", "description", "coverAlt", "coverCaption")
            if isinstance(metadata.get(key), str)
            and isinstance(source_meta.get(key), str)
            and len(normalize(str(source_meta[key])).split()) >= 3
            and normalize(str(metadata[key])) == normalize(str(source_meta[key]))
        ]
        copied_taxonomy = copied_english_taxonomy(source_meta, metadata)
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
            copied_sentences.extend(copied_fence_lines)
            copied_sentences = sorted(set(copied_sentences))
        if copied_sentences:
            reasons.append("exact_English_sentences")
        if copied_spans:
            reasons.append("copied_English_prose_span")
        if copied_headings:
            reasons.append("English_reader_heading_copy")
        if len(tokens) >= 120 and english_ratio >= 0.22 and locale_ratio < 0.12:
            reasons.append("English_stopword_dominance")
        if ratio is not None and len(prose) > 500 and ratio < 0.08:
            reasons.append("expected_script_missing")
        if metadata_keys:
            reasons.append("English_reader_metadata_copy:" + ",".join(metadata_keys))
        copied_link_labels = copied_english_link_labels(source_body, body)
        if copied_link_labels:
            reasons.append("English_reader_link_label_copy")
        if reasons:
            findings.append({
                "path": target.relative_to(ROOT).as_posix(),
                "locale": locale,
                "reasons": ";".join(reasons),
                "tokens": str(len(tokens)),
                "english_stopword_ratio": f"{english_ratio:.3f}",
                "locale_stopword_ratio": f"{locale_ratio:.3f}",
                "exact_english_paragraphs": f"{exact}/{len(paragraphs)}",
                "exact_english_sentences": " | ".join(copied_sentences),
                "copied_english_spans": " | ".join(sorted(copied_spans)),
                "copied_english_headings": " | ".join(copied_headings),
                "copied_english_metadata": " | ".join(
                    [f"{key}: {metadata[key]}" for key in copied_metadata]
                    + [f"{key}: {', '.join(values)}" for key, values in copied_taxonomy.items()]
                ),
                "expected_script_ratio": "" if ratio is None else f"{ratio:.3f}",
                "copied_link_labels": " | ".join(copied_link_labels),
                "note": "Screening flag. Review prose and metadata manually.",
            })
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="article bundle directories or index.en.md files")
    parser.add_argument("--all", action="store_true", help="scan all published article bundles")
    parser.add_argument("--csv", type=Path, help="write findings to this CSV path")
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

    print(f"published bundles scanned: {len(sources)}; configured locales: {len(locales)}; flags: {len(findings)}")
    for row in findings:
        print(f"{row['path']}\t{row['reasons']}\tEnglish paragraphs {row['exact_english_paragraphs']}\tEN stopwords {row['english_stopword_ratio']}")
    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        fields = ["path", "locale", "reasons", "tokens", "english_stopword_ratio", "locale_stopword_ratio", "exact_english_paragraphs", "exact_english_sentences", "copied_english_spans", "copied_english_headings", "copied_english_metadata", "expected_script_ratio", "copied_link_labels", "note"]
        with args.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(findings)
        print(f"CSV report: {args.csv}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
