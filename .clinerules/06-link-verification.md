# Link Verification Before Publishing

Every external URL placed in content, front matter, or templates must be verified
before the file is committed. A broken link or a mislabeled link hurts reader trust
and SEO. Apply this rule to all new links and to any existing links you touch while
editing a file.

## When This Rule Applies

- Any `http://` or `https://` URL added to a markdown file, shortcode, or template.
- The `link` parameter of a `{{< figure >}}` shortcode.
- URLs in front matter (e.g. `canonical`, `source`, or custom params).
- Internal `simeononsecurity.com` links are exempt from the HTTP-status check but
  must still be checked for slug accuracy against the actual content file.

## Required Verification Steps

### Step 1 — Confirm the URL resolves (no 404 / no redirect to an error page)

Use `cIv3Kr0mcp0visit_page` to fetch the URL. A valid page must:

- Return rendered content (not a browser error, Cloudflare block page, or "Page not
  found" message).
- Not redirect to a generic homepage or unrelated page (domain-level redirects count
  as broken for the specific resource).

If the page returns 404 or is otherwise unavailable, find a working replacement
(archived version, official docs, alternative authoritative source) before adding
the link.

### Step 2 — Verify the page title / H1 matches your expected topic

After fetching the page, read the returned content and confirm:

- The `<title>` tag or the first `<h1>` contains the topic you are linking to.
- The page description (meta description or opening paragraph) is topically
  consistent with the anchor text and the surrounding sentence.

**Mismatch examples that must be corrected:**
- Anchor text says "NIST SP 800-53" but the page title is "NIST SP 800-171 Overview."
- Anchor text says "official CompTIA objectives" but the page redirected to the
  CompTIA store homepage.
- Anchor text says "CVE-2024-1234" but the NVD page shows a different CVE.

If the title or description does not match, either update the anchor text to
accurately describe the destination, or find a page that does match.

### Step 3 — Prefer authoritative / canonical sources

When choosing between multiple URLs for the same resource, use this priority order:

1. Official documentation or specification (e.g. `docs.microsoft.com`, `nist.gov`,
   `nvd.nist.gov`, `tools.ietf.org`, vendor official docs).
2. Official project repository (e.g. `github.com/<official-org>/<project>`).
3. Reputable third-party reference with a stable URL and a named author.
4. Archive.org snapshot as a last resort when the original is gone.

Do not link to paywalled articles, login-gated pages, or transient content (e.g.
social media posts) as primary references.

## How to Use the Web Research Tool

```
cIv3Kr0mcp0visit_page(url="https://example.com/target-page")
```

Read the returned text for:
- HTTP status signals (look for "404", "not found", "error" in the body or title).
- The page `<title>` or leading `<h1>`.
- The opening paragraph or meta description to confirm topic alignment.

If the page content is ambiguous, use `cIv3Kr0mcp0search_google` to find the
canonical URL for the resource before visiting it.

```
cIv3Kr0mcp0search_google(query="NIST SP 800-53 Rev 5 official PDF site:nist.gov")
```

## Internal Link Accuracy

For links to other pages on this site (relative paths like `/secot-plus/` or
`/articles/foo/`):

- Confirm the target content file exists at the expected path before committing.
- Use `os.FileExists` (in Hugo templates) or check `content/` with the filesystem
  tools in this environment.
- Do not guess at slugs. Read the actual front matter `slug` or directory name.

## Verification Record

You do not need to add a comment or annotation to the markdown file. The verification
is a pre-commit check, not a runtime artifact. If a link fails verification and you
replaced it, note the original URL in your commit message so the change is traceable.

## Summary Checklist

Before committing any file that contains new or changed URLs:

1. [ ] Visited each external URL with `cIv3Kr0mcp0visit_page`.
2. [ ] Confirmed HTTP 200 (no 404, no error page, no unrelated redirect).
3. [ ] Confirmed page title / H1 matches the anchor text topic.
4. [ ] Confirmed page description or opening content is topically consistent.
5. [ ] Replaced any failed URLs with a working authoritative alternative.
6. [ ] Confirmed all internal links resolve to an existing content file.
