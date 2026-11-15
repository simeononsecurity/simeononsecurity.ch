#!/usr/bin/env python3
"""Screen article translations for copied or English-dominant reader-facing prose.

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
TABLE_ENGLISH_REVIEW_WORDS = ENGLISH_STOPWORDS | set(
    "average mean final score latency memory bandwidth method trial throughput "
    "value category result benchmark stage test cost price output input time "
    "performance description rate duration total size count level status per "
    "component privacy question local model server situation better choice "
    "reason evidence collect action recommendation finding concern response "
    "what check example setting location boundary control short project responsive assistant"
    .split()
)
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
    "ro": set("și de în la este sunt cu pentru din nu pe un o că ca aceasta acești".split()),
}
CSV_FIELDS = [
    "path", "locale", "reasons", "tokens", "english_stopword_ratio",
    "locale_stopword_ratio", "exact_english_paragraphs",
    "exact_english_sentences", "copied_reader_fenced_lines",
    "copied_reader_code_prose", "copied_english_spans",
    "split_word_emphasis", "english_dominant_paragraphs",
    "copied_english_table_cells", "copied_english_headings",
    "copied_english_metadata", "taxonomy_count_differences",
    "expected_script_ratio", "copied_english_opening", "copied_link_labels",
    "copied_english_body",
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


def copied_reader_code_prose(source: str, target: str) -> set[str]:
    """Find unchanged natural-language comments or output strings in executable examples."""
    return reader_fenced_code_prose(source) & reader_fenced_code_prose(target)


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


def markdown_headings(text: str) -> list[tuple[int, str]]:
    """Return Markdown heading levels and normalized visible labels."""
    text = re.sub(r"(?s)(`{3,}|~{3,}).*?\1", " ", text)
    headings = []
    for match in re.finditer(r"(?m)^\s{0,3}(#{1,6})[ \t]+(.+?)\s*#*\s*$", text):
        label = re.sub(r"!?(?:\[([^\]]*)\]\([^)]*\))", r"\1", match.group(2))
        headings.append((len(match.group(1)), normalize(label)))
    return headings


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
    return {
        key: (source_shape[key], target_shape[key])
        for key in source_shape
        if source_shape[key] != target_shape[key]
    }


def copied_english_table_cells(source: str, target: str) -> list[str]:
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
    for table_index, (source_table, target_table) in enumerate(
        zip(source_tables, target_tables), start=1
    ):
        for row_index, (source_row, target_row) in enumerate(
            zip(source_table, target_table), start=1
        ):
            for cell_index, (source_cell, target_cell) in enumerate(
                zip(source_row, target_row), start=1
            ):
                normalized = normalize(source_cell)
                words = normalized.split()
                if (
                    normalized
                    and normalized == normalize(target_cell)
                    and words
                    and any(word in TABLE_ENGLISH_REVIEW_WORDS for word in words)
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


def prose_sentences(text: str) -> set[str]:
    """Return normalized reader-facing sentences outside code and markup."""
    visible = visible_text(text, include_link_labels=False)
    return {
        normalize(part)
        for part in re.split(r"(?<=[.!?])\s+|\n+", visible)
        if len(normalize(part).split()) >= 8
    }


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
        english_paragraphs = english_dominant_paragraphs(body, locale)
        copied_table_cells = copied_english_table_cells(source_body, body)
        copied_headings = copied_english_headings(source_body, body)
        structure_differences = markdown_structure_differences(source_body, body)
        ratio = script_ratio(prose, locale)
        reasons = []
        copied_opening = copied_english_opening(source_body, body)
        if copied_opening:
            reasons.append("copied_english_opening")
        if copied_body:
            reasons.append("copied_english_body")
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
        copied_code_prose = sorted(copied_reader_code_prose(source_body, body))
        if copied_code_prose:
            reasons.append("copied_reader_code_prose")
        split_emphasis = split_word_emphasis(body, locale)
        if split_emphasis:
            reasons.append("markdown_split_word_emphasis")
        if copied_sentences:
            reasons.append("exact_English_sentences")
        if copied_spans:
            reasons.append("copied_English_prose_span")
        if english_paragraphs:
            reasons.append("English_dominant_reader_paragraph")
        if copied_table_cells:
            reasons.append("English_reader_table_cell_copy")
        if copied_headings:
            reasons.append("English_reader_heading_copy")
        if len(tokens) >= 120 and english_ratio >= 0.22 and locale_ratio < 0.12:
            reasons.append("English_stopword_dominance")
        if ratio is not None and len(prose) > 500 and ratio < 0.08:
            reasons.append("expected_script_missing")
        if metadata_keys:
            reasons.append("English_reader_metadata_copy:" + ",".join(metadata_keys))
        if taxonomy_counts:
            reasons.append("taxonomy_count_mismatch:" + ",".join(sorted(taxonomy_counts)))
        copied_link_labels = copied_english_link_labels(source_body, body)
        if copied_link_labels:
            reasons.append("English_reader_link_label_copy")
        for key in structure_differences:
            reasons.append(f"markdown_{key}_mismatch")
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
                "copied_reader_fenced_lines": " | ".join(copied_fence_lines),
                "copied_reader_code_prose": " | ".join(copied_code_prose),
                "copied_english_spans": " | ".join(sorted(copied_spans)),
                "split_word_emphasis": " | ".join(split_emphasis),
                "english_dominant_paragraphs": " | ".join(english_paragraphs),
                "copied_english_table_cells": " | ".join(copied_table_cells),
                "copied_english_headings": " | ".join(copied_headings),
                "copied_english_metadata": " | ".join(
                    [f"{key}: {metadata[key]}" for key in copied_metadata]
                    + [f"{key}: {', '.join(values)}" for key, values in copied_taxonomy.items()]
                ),
                "taxonomy_count_differences": json.dumps(
                    taxonomy_counts, ensure_ascii=False, sort_keys=True
                ),
                "expected_script_ratio": "" if ratio is None else f"{ratio:.3f}",
                "copied_english_opening": copied_opening,
                "copied_link_labels": " | ".join(copied_link_labels),
                "copied_english_body": copied_body,
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
        with args.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(findings)
        print(f"CSV report: {args.csv}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
