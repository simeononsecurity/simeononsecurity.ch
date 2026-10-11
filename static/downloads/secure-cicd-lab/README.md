# Secure CI/CD release lab

This directory is a disposable local exercise. It needs Python 3.10 or later. It has no network calls and no package installs.

Run `python3 verify_release.py release-good.txt` from this directory. Expect `PASS: digest matches trusted manifest`.

Run `python3 verify_release.py release-tampered.txt`. Expect `FAIL: digest mismatch` and exit code 1.

The manifest is trusted only because this lab gives you a separate known-good copy. A checksum stored beside a downloaded artifact does not prove publisher identity. In production, verify a signed attestation and the expected source repository and workflow.

Reset the lab with `git restore static/downloads/secure-cicd-lab` when working in a Git clone. Otherwise, extract a fresh copy from the repository.
