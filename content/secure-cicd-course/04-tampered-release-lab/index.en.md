---
title: "Tampered Release Lab: Reject Changed Artifact Bytes"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Run a local release verification lab, detect a modified artifact, and explain why trusted checksums and attestation identities matter."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["tampered release lab", "SHA-256 verification", "artifact integrity", "software supply chain training"]
cover: "/img/cover/secure-cicd-tampered-release-lab.webp"
coverAlt: "A clean package passes comparison while an altered package is blocked at a release gate."
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**This lab makes one controlled change to a fictional release.** You will verify a known-good text artifact, reject a modified copy, and state what the checksum proves. The lab runs locally with no credentials, network calls, or production systems.

## Key Takeaways

- **A trusted digest** detects changed bytes.
- **A checksum beside an untrusted download** does not establish publisher identity.
- **A release gate** should fail closed and retain evidence for triage.

## Prepare the Lab

**Download the [lab archive](/downloads/secure-cicd-lab.zip)** to a fresh folder. It includes the release files, a trusted digest, Python checks, and sample evidence for the other lessons. Python 3.10 or later is enough. Plan 30 to 60 minutes.

**On macOS or Linux, extract and enter the lab folder:**

```bash
unzip secure-cicd-lab.zip
cd secure-cicd-lab
python3 --version
```

**On Windows PowerShell, extract and enter the lab folder:**

```powershell
Expand-Archive .\secure-cicd-lab.zip -DestinationPath .
Set-Location .\secure-cicd-lab
py -3 --version
```

**Expected result:** The version is Python 3.10 or later, and `verify_release.py`, both release files, and `trusted.sha256` appear in the folder. Use `ls` on macOS or Linux or `Get-ChildItem` on Windows to list them.

**Record your starting state** in a table with artifact name, file size, SHA-256 digest, source of the trusted digest, and decision. On macOS or Linux, run `wc -c release-good.txt` and `shasum -a 256 release-good.txt`. On Windows, use `(Get-Item .\release-good.txt).Length` and `Get-FileHash .\release-good.txt -Algorithm SHA256`. In this exercise, `trusted.sha256` is the instructor-provided known-good digest. Production trust would need a protected channel or verified attestation.

## Verify the Good Artifact

```bash
python3 verify_release.py release-good.txt
```

Expected result:

```text
PASS: digest matches trusted manifest
```

**Confirm the exit code is zero.** On a shell with `$?`, run `echo $?` immediately after the command. The script reads bytes, computes SHA-256, and compares the result with the trusted manifest. This establishes byte equality with the instructor copy. It does not establish who authored the copy.

**On Windows, replace `python3` with `py -3`** and inspect `$LASTEXITCODE` immediately afterward. On macOS or Linux, `shasum -a 256 -c trusted.sha256` supplies a second checksum check. It should print `release-good.txt: OK`.

## Test the Tampered Artifact

```bash
python3 verify_release.py release-tampered.txt
```

Expected result:

```text
FAIL: digest mismatch
```

**Confirm the exit code is one.** Use `echo $?` on macOS or Linux or `$LASTEXITCODE` in PowerShell. Open both release files and identify the added telemetry line. Write a two-sentence incident note: what changed and which gate blocked it. Do not run or distribute the altered file. This controlled file is text, so the lab causes no network activity.

## Diagnose a Failed Setup

**Wrong directory:** If Python reports a missing file, run `pwd` and list the lab files. **Usage error:** The script accepts one filename from its own directory. **Unexpected pass:** Recheck that you used `release-tampered.txt` and did not change `trusted.sha256`. **Unexpected failure on the good file:** Download a fresh copy of the lab. Line-ending changes alter the digest.

## State the Trust Boundary

**Run a thought experiment.** If an attacker replaces both `release-tampered.txt` and the checksum fetched from the same untrusted server, the comparison can pass. Write the control needed to fix this: verify a signed attestation against the expected repository and workflow, or obtain the expected digest through an independently trusted channel. Use the [GitHub attestation verification guide](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) for the hosted path.

**Pass this lab** when your record has both commands, expected or observed exit codes, the changed line, the decision to reject the tampered copy, and the trust-boundary explanation. Mark outputs “expected” if you have not run the commands.

**Next:** [Take the knowledge check](/secure-cicd-course/05-quiz/).
