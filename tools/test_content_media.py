"""Behavioral fixtures for the read-only media checker, all outside the repo."""

import tempfile
import unittest
from pathlib import Path

from PIL import Image

from check_content_media import audit


class MediaAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.page = self.root / 'content/articles/example/index.en.md'
        self.page.parent.mkdir(parents=True)
        self.cover = self.root / 'assets/img/cover/example.webp'
        self.cover.parent.mkdir(parents=True)
        Image.new('RGB', (2048, 1152)).save(self.cover, 'WEBP')
        self.write()

    def write(self, body='', cover='/img/cover/example.webp', extra=''):
        self.page.write_text(f'---\ncover: "{cover}"\ncoverAlt: "An example cover"\n{extra}---\n{body}')

    def check(self, **kwargs):
        return audit(self.page, self.root, **kwargs)

    def test_valid_generated_cover_and_bundle(self):
        inline = self.page.parent / 'figure.webp'
        inline.write_bytes(self.cover.read_bytes())
        self.write('{{< figure src="figure.webp" alt="Example figure" >}}')
        before = {p: p.read_bytes() for p in [self.page, self.cover, inline]}
        errors, notes, count = self.check(require_cover=True, generated=True)
        self.assertEqual((errors, notes, count), ([], [], 2))
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_missing_exact_reference_with_alternative_still_fails(self):
        self.write(cover='/img/cover/example.png')
        errors, _, count = self.check()
        self.assertEqual(count, 0)
        self.assertTrue(any('same-stem alternatives' in e for e in errors))

    def test_corrupt_asset(self):
        self.cover.write_bytes(b'invalid image')
        errors, _, count = self.check()
        self.assertEqual(count, 0)
        self.assertTrue(any('cannot decode' in e for e in errors))

    def test_generated_dimensions_are_opt_in(self):
        Image.new('RGB', (640, 360)).save(self.cover, 'WEBP')
        self.assertFalse(self.check()[0])
        self.assertTrue(self.check(generated=True)[0])

    def test_fenced_and_commented_examples_are_ignored(self):
        self.write('```text\n{{< figure src="absent.webp" >}}\n```\n'
                   '<!-- {{< figure src="absent.webp" >}} -->')
        self.assertEqual(self.check(), ([], [], 1))

    def test_remote_media_is_explicitly_unverified(self):
        self.write(cover='https://example.org/image.webp')
        errors, notes, count = self.check()
        self.assertEqual((errors, count), ([], 0))
        self.assertTrue(any('manual remote verification' in n for n in notes))

    def test_missing_alt_and_raw_image_are_errors(self):
        self.write('{{< figure src="missing.webp" >}}\n![raw](missing.webp)')
        errors, _, _ = self.check()
        self.assertTrue(any('alt is empty' in e for e in errors))
        self.assertTrue(any('raw Markdown/HTML' in e for e in errors))

    def test_missing_cover_and_invalid_yaml(self):
        self.page.write_text('---\ntitle: Example\n---\nBody')
        self.assertFalse(self.check()[0])
        self.assertTrue(self.check(require_cover=True)[0])
        self.page.write_text('---\ncover: [\n---\nBody')
        self.assertTrue(self.check()[0])

    def test_traversal_outside_root_is_rejected(self):
        self.write(cover='../../../../outside.webp')
        self.assertTrue(any('missing exact' in e for e in self.check()[0]))


if __name__ == '__main__':
    unittest.main()
