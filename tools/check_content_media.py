#!/usr/bin/env python3
"""Read-only media audit for explicitly selected Hugo Markdown pages.

Requires Pillow and PyYAML from tools/requirements.txt. Does not fetch remote
media or attempt complete Markdown/Hugo parsing. Fenced examples are ignored.
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ATTR = re.compile(r'''([\w-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')''')
RASTER = {'.webp', '.png', '.jpg', '.jpeg', '.gif', '.avif', '.bmp', '.tif', '.tiff'}


def without_examples(body):
    """Remove fenced examples and HTML comments before locating shortcodes."""
    lines = []
    fence = None
    for line in body.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
        if match:
            marker, tail = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not tail.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return re.sub(r'<!--.*?-->', '', '\n'.join(lines), flags=re.S)


def audit(page, root=ROOT, require_cover=False, generated=False):
    errors, notes, refs = [], [], []
    text = page.read_text(encoding='utf-8')
    match = re.match(r'\A---\s*\n(.*?)\n---\s*(?:\n|$)', text, re.S)
    if not match:
        return ['missing YAML front matter'], notes, 0
    try:
        front = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f'invalid YAML: {exc}'], notes, 0
    if not isinstance(front, dict):
        return ['front matter is not a mapping'], notes, 0
    cover = front.get('cover')
    if cover:
        refs.append(('cover', cover))
        if not isinstance(front.get('coverAlt'), str) or not front['coverAlt'].strip():
            errors.append('coverAlt is empty')
    elif require_cover:
        errors.append('cover is required')

    body = without_examples(text[match.end():])
    for figure in re.finditer(r'{{[<%]\s*figure\b(.*?)[>%]}}', body, re.S):
        attrs = {m[0]: m[1] or m[2] for m in ATTR.findall(figure.group(1))}
        if not attrs.get('src'):
            errors.append('figure requires a quoted src')
        else:
            refs.append(('figure', attrs['src']))
        if not attrs.get('alt', '').strip():
            errors.append('figure alt is empty')
    if re.search(r'!\[[^\]]*\]\s*[\[(]|<img\b', body, re.I):
        errors.append('body image uses raw Markdown/HTML; use the figure shortcode')

    count = 0
    for kind, ref in refs:
        if not isinstance(ref, str):
            errors.append(f'{kind} reference must be a string')
            continue
        parsed = urlsplit(ref)
        if parsed.scheme in ('http', 'https') or ref.startswith('//'):
            notes.append(f'manual remote verification required: {ref}')
            continue
        if parsed.scheme:
            errors.append(f'unsupported image scheme: {ref}')
            continue
        relative = Path(unquote(parsed.path).lstrip('/'))
        if parsed.path.startswith('/'):
            bases = [root / 'assets', root / 'static'] if kind == 'cover' else [root / 'static', root / 'assets']
            candidates = [base / relative for base in bases]
        else:
            candidates = [page.parent / relative]
            if kind == 'cover':
                candidates += [root / 'assets' / relative, root / 'static' / relative]
        # Do not read arbitrary files outside this repository through a reference.
        candidates = [p for p in candidates if p.resolve().is_relative_to(root.resolve())]
        target = next((p for p in candidates if p.is_file()), None)
        if target is None:
            alternatives = sorted({str(p) for c in candidates for p in c.parent.glob(c.stem + '.*')
                                   if p.is_file() and p.suffix.lower() in RASTER})
            hint = f'; inspect same-stem alternatives: {", ".join(alternatives)}' if alternatives else ''
            errors.append(f'missing exact {kind} target: {ref}{hint}')
            continue
        if target.suffix.lower() not in RASTER:
            notes.append(f'manual non-raster verification required: {target}')
            continue
        try:
            with Image.open(target) as image:
                image.verify()
            with Image.open(target) as image:
                image.load()
                if generated and (image.format != 'WEBP' or image.size != (2048, 1152)):
                    errors.append(f'generated image must be 2048x1152 WebP: {target}')
            count += 1
        except (OSError, ValueError, SyntaxError) as exc:
            errors.append(f'cannot decode {target}: {exc}')
    return errors, notes, count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pages', nargs='+', type=Path, help='Explicit Markdown page paths; no recursive scan')
    parser.add_argument('--require-cover', action='store_true', help='Fail if any selected page lacks a cover')
    parser.add_argument('--generated', action='store_true', help='Require 2048x1152 WebP for selected local rasters')
    args = parser.parse_args()
    failed = False
    for page in args.pages:
        page = page.resolve()
        if not page.is_relative_to(ROOT) or not page.is_file():
            print(f'ERROR: expected an existing repository page: {page}')
            failed = True
            continue
        try:
            errors, notes, count = audit(page, require_cover=args.require_cover, generated=args.generated)
        except (OSError, UnicodeError, ValueError) as exc:
            errors, notes, count = [str(exc)], [], 0
        failed |= bool(errors)
        print(f'{page}: {count} local raster images decoded, {len(errors)} errors, {len(notes)} manual checks')
        for label, messages in [('ERROR', errors), ('NOTE', notes)]:
            for message in messages:
                print(f'  {label}: {message}')
    return int(failed)


if __name__ == '__main__':
    sys.exit(main())
