"""Behavioral tests for local Hugo image-sitemap URL resolution."""

import tempfile
import unittest
from pathlib import Path

from check_image_sitemap_paths import audit


class ImageSitemapPathTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def sitemap(self, *urls):
        images = "".join(f"<image:image><image:loc>{url}</image:loc></image:image>" for url in urls)
        (self.root / "imagessitemap.xml").write_text(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
            '<url><loc>https://example.test/post/</loc>' + images + '</url></urlset>'
        )

    def test_encoded_space_must_resolve_to_decoded_filename(self):
        url = "https://example.test/img/tls_%20cover.webp"
        self.sitemap(url)
        folder = self.root / "img"
        folder.mkdir()
        (folder / "tls_%20cover.webp").write_bytes(b"broken-public-path")
        errors, checked, skipped = audit(self.root)
        self.assertEqual((checked, skipped), (1, 0))
        self.assertEqual(len(errors), 1)
        (folder / "tls_%20cover.webp").rename(folder / "tls_ cover.webp")
        self.assertEqual(audit(self.root), ([], 1, 0))

    def test_normal_local_image_and_remote_skip(self):
        self.sitemap("https://example.test/img/cover.webp", "https://cdn.example.test/remote.webp")
        (self.root / "img").mkdir()
        (self.root / "img/cover.webp").write_bytes(b"ok")
        self.assertEqual(audit(self.root), ([], 1, 1))

    def test_encoded_traversal_is_rejected(self):
        self.sitemap("https://example.test/img/%2e%2e/%2e%2e/outside.webp")
        self.assertEqual(len(audit(self.root)[0]), 1)


if __name__ == "__main__":
    unittest.main()
