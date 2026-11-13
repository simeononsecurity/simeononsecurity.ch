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
    return metadata, match.group(2)


def visible_text(text: str) -> str:
    text = re.sub(r"(?s)```.*?```|~~~.*?~~~", " ", text)
    text = re.sub(r"(?m)^\s*\{\{<.*?>\}\}\s*$", " ", text)
    text = re.sub(r"\{\{<.*?>\}\}", " ", text)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"https?://[^\s)\]>]+", " ", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return text


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return " ".join(re.findall(r"\w+", text, flags=re.UNICODE))


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
        if len(prose.strip()) < 30:
            reasons.append("empty_or_nearly_empty")
        if exact >= 3 and exact_ratio >= 0.35:
            reasons.append("many_exact_English_paragraphs")
        if len(tokens) >= 120 and english_ratio >= 0.22 and locale_ratio < 0.12:
            reasons.append("English_stopword_dominance")
        if ratio is not None and len(prose) > 500 and ratio < 0.08:
            reasons.append("expected_script_missing")
        if copied_metadata:
            reasons.append("English_reader_metadata_copy:" + ",".join(copied_metadata))
        if reasons:
            findings.append({
                "path": target.relative_to(ROOT).as_posix(),
                "locale": locale,
                "reasons": ";".join(reasons),
                "tokens": str(len(tokens)),
                "english_stopword_ratio": f"{english_ratio:.3f}",
                "locale_stopword_ratio": f"{locale_ratio:.3f}",
                "exact_english_paragraphs": f"{exact}/{len(paragraphs)}",
                "expected_script_ratio": "" if ratio is None else f"{ratio:.3f}",
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
        fields = ["path", "locale", "reasons", "tokens", "english_stopword_ratio", "locale_stopword_ratio", "exact_english_paragraphs", "expected_script_ratio", "note"]
        with args.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(findings)
        print(f"CSV report: {args.csv}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
