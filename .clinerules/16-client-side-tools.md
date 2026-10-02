# Client-Side Tools: Privacy, Recalculation, and Verification

Every tool on this site lives at `content/<slug>/_index.en.md` (front matter only, with
`layout: "<slug>"`) plus `layouts/section/<slug>.html`. The tools index is
`content/tools/index.en.md`.

Two rules govern every tool. Both are hard requirements, not preferences.

---

## Rule 1: Every Tool Runs 100% Client-Side

A tool must not send user input anywhere. No `fetch`, no `XMLHttpRequest`, no remote
`src`, no form post. This is the whole point of the offering, and the tools index states
it publicly in the data-handling table.

**When a tool genuinely cannot be local, name the exception on the page.** Two exist:

| Tool | Exception | Why |
|------|-----------|-----|
| **What's My IP** | Queries `ipify.org` | The browser must ask someone for the address |
| **Security Headers Check** | Requests a user-supplied URL | The response depends on the remote host |

A tool parsing pasted input is always local. The SSL certificate tools
work this way on purpose: a browser does not expose the TLS handshake to JavaScript, so
reading a certificate from a live host would mean sending the hostname to a third party.
The pages tell the reader to fetch the chain with
`openssl s_client -connect host:443 -showcerts` and paste it.

**Audit a layout with:**

```bash
grep -cE 'fetch\(|XMLHttpRequest|src="http' layouts/section/<slug>.html
```

Zero is the only acceptable result for a local tool.

---

## Rule 2: Derived Values Must Recalculate on Modification

**If a tool computes a checksum, hash, fingerprint, error-detection value, or any other
derived integrity value from user input must recompute whenever the input changes. A
button-only recompute is not acceptable.**

This covers ECC, ERC, CRC, LRC, parity, Luhn, cryptographic hashes, HMAC, key
fingerprints, certificate signatures, and time-based codes. The reader must never see a
stale digest next to edited data.

The pattern is a debounced listener on every input feeding the computation:

```js
(function () {
  var timer = null;
  function auto() {
    if (timer) { clearTimeout(timer); }
    timer = setTimeout(function () {
      var el = document.getElementById('<inputId>');
      if (!el) { return; }
      if (!el.value.trim()) { <clearFn>(); return; }
      <computeFn>(false);
    }, 250);
  }
  ['<inputId>'].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) { el.addEventListener('input', auto); el.addEventListener('change', auto); }
  });
})();
```

Empty input resets the outputs rather than showing an error mid-typing.

### Analytics Fires Only on Explicit Activation

Give the compute function a `track` parameter and gate the event:

```js
if (track !== false) { yieldToMain(sendTrackingEvent); }
```

The button calls it with no argument, so a click still records. Every automatic path
passes `false`. Without this gate a debounced listener fires an event per keystroke, and
the TOTP interval fires a gtag `conversion` every 30 seconds for as long as the tab is
open.

**When adding an automatic path, check every existing caller.** A background
`setInterval` and an initial load call are the two most often missed.

### The Integrity Tool Inventory

| Tool | Derived value | Status |
|------|---------------|--------|
| `magnetic-stripe-decoder` | LRC, odd parity, Luhn | Auto |
| `hash-calculator` (+ theme `hash_calculator`) | MD5, SHA-1/256/512, RIPEMD-160 | Auto |
| `hmac-calculator` | HMAC signature, hex and Base64 | Auto |
| `totp-generator` | TOTP, HOTP | Auto, plus a 30 second interval |
| `password-checker` | Brute-force time estimate | Auto |
| `ssh-key-fingerprint` | SHA-256 key fingerprint | Auto |
| `ssl-certificate-info` | Fingerprints, validity, key size | Auto |
| `ssl-chain-tester` | Signature verification per link | Auto |

Any new tool in this class joins the list.

---

## Verifying a Tool Before Committing

Unit tests in the layout are not enough. Extract the shipped JavaScript and run it.

**1. Syntax check.** Hugo templates inside `<script>` break `node --check`, so strip them.

```python
import re, subprocess, tempfile, os
html = open('layouts/section/<slug>.html', encoding='utf-8').read()
js = '\n'.join(re.findall(r'<script>(.*?)</script>', html, re.S)).replace('{{','').replace('}}','')
t = tempfile.NamedTemporaryFile('w', suffix='.js', delete=False); t.write(js); t.close()
print(subprocess.run(['node','--check',t.name], capture_output=True, text=True).returncode)
```

**2. Assert against a reference implementation, never against your own output.** Generate
real artefacts and compare. Prior work used `openssl` for certificates, `ssh-keygen -lf`
for key fingerprints, Node's `crypto` for hashes and HMAC, the published RFC 6238 vectors
for TOTP, and the ISO/IEC 7811-2 tables for stripe encoding.

**3. Drive the recalculation through a DOM stub.** Build a stub whose `getElementById`
returns cached elements registering listeners, dispatches `input`, waits past the debounce,
and read the output element. Count `gtag` calls in the same run to prove the automatic
path stays silent.

```js
el.addEventListener = (t, f) => { (el._h[t] = el._h[t] || []).push(f); };
el.dispatch = t => { (el._h[t] || []).forEach(f => f({ target: el })); };
```

**A stub omitting `window.crypto` produces false failures.** Both the HMAC and TOTP
tools guard on `window.crypto.subtle` and correctly bail when it is missing, which reads
as a broken tool when the harness is at fault. Set
`global.window.crypto = require('crypto').webcrypto`.

**4. When a test fails, decide whose bug it is before editing the tool.** Across the tools
built so far, several failures were harness errors rather than code defects: a duplicated
sentinel character in an expected value, a mistyped CVSS tuple, and an expectation of a
pattern name which was never a real pattern. Two were genuine. Check the reference value
first.

---

## Reference: ISO/IEC 7811-2 Stripe Character Encoding

The two tracks use **different** character sets. Sharing one mapping produces an LRC a reader rejects.

| Track | Format | Code derivation | Start sentinel | Field separator | End sentinel |
|-------|--------|-----------------|----------------|-----------------|--------------|
| **1** | ALPHA, 6 data bits + odd parity | ASCII minus `0x20` | `%` = `0x05` | `^` = `0x3E` | `?` = `0x1F` |
| **2** | BCD, 4 data bits + odd parity | low nibble of ASCII | `;` = `0x0B` | `=` = `0x0D` | `?` = `0x0F` |

Track 1 maps `'A'` to `0x21`, `'0'` to `0x10`, and space to `0x00`. Track 2 maps `'0'`
to `0x00` and `'9'` to `0x09`.

**The LRC is a character, not a raw code.** Its data bits are the XOR of every character
from the start sentinel through the end sentinel inclusive, and it is then offset back
into the track's printable set:

```js
String.fromCharCode((xorOfDataValues & mask) + offset)   // offset 0x20 track 1, 0x30 track 2
```

Parity belongs to the bits written on the stripe, not to the ASCII character, so keep it
out of the emitted string and report it separately. Folding the parity bit into the value
and returning it directly yields a control character on track 2 and a wrong letter on
track 1.

**Do not ship real card data.** Sample values use the standard test PAN
`4111111111111111` with synthetic expiry, service code, and discretionary digits. A
partially edited real sample still leaks: swapping the PAN while leaving the expiry,
service code, and discretionary tail intact leaves the real values in the repository.
Scan for fragments, not only the full number.

---

## Layout Conventions for a New Tool

Copy an existing layout rather than starting from scratch. The shared parts:

- `{{ define "main" }}` wrapping a panel `<div>`
- `style-append.css` preload, breadcrumbs, and the shared ad partial
- A `<style scoped>` block with a **unique class prefix**. Scoped styles are not honoured
  by browsers, so the rules are global. Two tools sharing a prefix is a latent collision.
  Check with `grep -c '<prefix>-' layouts/section/<other>.html`.
- A plain-language note stating processing happens in the browser
- `yieldToMain` plus a `gtag` call inside `try/catch` for the tracking event

Several layouts exist in duplicate under `layouts/section/` with both a hyphen and an
underscore (`hash-calculator` and `hash_calculator`, `password-checker` and
`password_checker`). The project copy wins over the theme. **When fixing a bug in one,
fix the duplicate too**, or the fix is silently absent depending on which resolves.

Then add the tool to `content/tools/index.en.md` and, if it computes an integrity value,
follow Rule 2.

---

## When a Full Build Is Needed

Unit tests, extracted JavaScript checks, DOM recalculation tests, and a targeted
render are enough for an isolated tool layout change. Do not run the full site
build for every tool edit.

Run a full EN build when changing shared layouts, theme overrides, shared CSS or
JavaScript, Hugo configuration, output formats, shortcodes, resource processing,
or another component used by many pages. An EN build renders roughly 34,000 pages
and takes 10 to 15 minutes. It runs long past the 30 second command timeout, so
launch it in the background and poll:

```bash
nohup npx hugo --minify -D --config config/language/en/config.toml --destination /tmp/en_tools > /tmp/en_tools.log 2>&1 &
grep -o 'Total in [0-9]* ms' /tmp/en_tools.log
```

**Do not use the top-level directory count as a progress indicator.** Nearly every page
is nested under `articles/`, `guides/`, and similar, so the top-level count sits still
while thousands of files are being written below it. This misled a prior session into
killing a healthy build. Count rendered pages instead:

```bash
find /tmp/en_tools -name index.html | wc -l
```