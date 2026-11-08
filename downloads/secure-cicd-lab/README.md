# Secure CI/CD release lab

This directory is a disposable local exercise. It needs Python 3.10 or later. It has no network calls and no package installs. The dependency, SBOM, Scorecard, policy, and provenance files are synthetic teaching fixtures. They are not tool output or signed attestations.

Run `python3 verify_release.py release-good.txt` from this directory. Expect `PASS: digest matches trusted manifest`.

Run `python3 verify_release.py release-tampered.txt`. Expect `FAIL: digest mismatch` and exit code 1.

Run `python3 inspect_packet.py`. Expect five MATCH fields and a final message saying the signature was not verified. Run `python3 inspect_packet.py sample-provenance-wrong-source.json`. Expect `source: MISMATCH`, `HOLD`, and exit code 1.

The ZIP extracts into one `secure-cicd-lab` folder. Enter that folder before running the commands. On Windows, use `py -3` in place of `python3`. Python prints the same messages on either platform.

The manifest is trusted only because this lab gives you a separate known-good copy. Its path is relative to the extracted folder, so `shasum -a 256 -c trusted.sha256` also works on macOS or Linux. A checksum stored beside a downloaded artifact does not prove publisher identity. In production, verify a signed attestation and the expected source repository and workflow.

Reset the lab with `git restore static/downloads/secure-cicd-lab` when working in a Git clone. Otherwise, extract a fresh copy from the repository.
