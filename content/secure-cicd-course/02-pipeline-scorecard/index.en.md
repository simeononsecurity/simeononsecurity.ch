---
title: "GitHub Actions Permissions and OpenSSF Scorecard"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Reduce GitHub Actions token scope, separate untrusted jobs, and turn OpenSSF Scorecard findings into release controls."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["GitHub Actions permissions", "OpenSSF Scorecard", "CI pipeline security", "GITHUB_TOKEN", "least privilege"]
cover: "/img/cover/secure-cicd-pipeline-scorecard.webp"
coverAlt: "Two build jobs use separate keys while a broad-permission path is stopped beside a security checklist."
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**A CI job should receive only the authority its task needs.** A test job reads code. A release job writes a package or attestation. Separate those jobs before asking whether the workflow passes. OpenSSF Scorecard then gives you a review list for repository practices, not a blanket approval.

## Key Takeaways

- **GITHUB_TOKEN permissions** belong at workflow or job scope and should match the operation.
- **Untrusted pull requests** should not run release steps with write access or secrets.
- **Scorecard scores** point to evidence and remediation. Read each check's reason.

## Map Job Authority

**Start with the [lab archive](/downloads/secure-cicd-lab.zip).** Extract it and open `release-policy.json`. A **job** is one group of workflow steps. `GITHUB_TOKEN` is the temporary token GitHub provides to a workflow. **Job permissions** limit its API access. A **source ref** names a branch or tag. **Secrets** are credentials supplied to a job. Write the event, job, inputs, permissions, secrets, and output for each row below. Use GitHub's [token permissions documentation](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token) for permission names. Plan 40 minutes.

| Job | Expected permission | Output |
|---|---|---|
| **Pull request test** | `contents: read` | Test result, no release |
| **Protected release** | `contents: read`, then specific publication and attestation writes | Published digest and provenance |

**For the hosted path, save this as `.github/workflows/test.yml`** in a disposable repository. It runs on a pull request and grants read access only:

```yaml
name: Test
on: pull_request
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
        with:
          persist-credentials: false
      - run: python3 -m compileall -q .
```

**Expected result:** After opening a pull request, the Actions tab shows `Test` and a syntax result. The command checks Python syntax only. Replace it with project tests before relying on the job. If checkout fails, inspect repository access and the token scope. If the project is not Python, use its own test command. For the local path, review the YAML on paper and mark the run “not run.”

## Separate the Release

**Trigger a release only from an approved source ref.** Protect that ref with repository rules and human review. Put release credentials and `attestations: write` only in the release job. GitHub's [secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) warns about untrusted workflow inputs and privileged `pull_request_target` patterns. Avoid checking out attacker-controlled code into a privileged job.

**Inspect every action reference.** A version tag is readable, but a full commit ID better fixes the action code reviewed at a point in time. Record the owner, commit, purpose, and update process. Do not copy a random commit ID from an example into production without checking the action repository.

## Use Scorecard as a Review Queue

**For the local path, open `sample-scorecard.json`.** It is an illustrative finding, not output from Scorecard. Its Pinned-Dependencies score is 3 because the fictional workflow uses mutable tags. Record the check name, score, reason, and a correction. Inspect the `uses: actions/checkout@v7` line above and explain why a reviewed full commit ID would give a stronger pin.

**For the optional live path, run OpenSSF Scorecard** against a public repository you own. Install the CLI from its [official repository](https://github.com/ossf/scorecard), then run `scorecard --repo=github.com/OWNER/REPOSITORY` with your real owner and repository. Record the version, time, checks, scores, and reasons. If the command is unavailable, use the local fixture and mark the live run “not run.” Scorecard's automated checks cover source, build, dependencies, and maintenance. A score is evidence to investigate, not proof of a secure release.

**Choose one actionable finding.** For the fixture, write `Pinned-Dependencies | 3 | mutable tags | review and pin action commit | rerun Scorecard after change`. A low Branch-Protection score in a live result may lead you to require review on the release branch. Record the original finding, the exact control change, and a second result when you run the tool. If a check reports `?`, record unavailable evidence instead of treating it as zero risk. Read the [check definitions](https://github.com/ossf/scorecard/blob/main/docs/checks.md) before interpreting a result.

## Verify Your Work

**Pass this lesson** when your packet contains the two-job permissions table, one untrusted-input boundary, and the fixture finding with a reason and correction. Mark hosted checks “not run” on the local path. Do not claim Scorecard observed a control you did not run.

**Next:** [Verify provenance and attestations](/secure-cicd-course/03-provenance-attestations/).
