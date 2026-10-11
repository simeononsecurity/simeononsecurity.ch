---
title: "GitHub Actions Permissions and OpenSSF Scorecard"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Reduce GitHub Actions token scope, separate untrusted jobs, and turn OpenSSF Scorecard findings into release controls."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["GitHub Actions permissions", "OpenSSF Scorecard", "CI pipeline security", "GITHUB_TOKEN", "least privilege"]
cover: "/img/cover/secure-cicd-course.webp"
coverAlt: "A source repository, build runner, artifact, and verification gate connected in a release workflow"
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**A CI job should receive only the authority its task needs.** A test job reads code. A release job writes a package or attestation. Separate those jobs before asking whether the workflow passes. OpenSSF Scorecard then gives you a review list for repository practices, not a blanket approval.

## Key Takeaways

- **GITHUB_TOKEN permissions** belong at workflow or job scope and should match the operation.
- **Untrusted pull requests** should not run release steps with write access or secrets.
- **Scorecard scores** point to evidence and remediation. Read each check's reason.

## Map Job Authority

**Start with a two-row table.** Write the event, job, inputs, token permissions, secrets, and output for each job. Use GitHub's [token permissions documentation](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token) for permission names. Plan 40 minutes.

| Job | Expected permission | Output |
|---|---|---|
| **Pull request test** | `contents: read` | Test result, no release |
| **Protected release** | `contents: read`, then specific publication and attestation writes | Published digest and provenance |

**Make read access explicit** in the test workflow:

```yaml
name: Test
on: pull_request
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          persist-credentials: false
      - run: python3 -m compileall -q .
```

**Expected result:** The test job checks out code and reports syntax status without publishing. The example command checks Python syntax only. Replace it with project tests before relying on the job. If checkout fails, inspect repository access and the token scope. If the project is not Python, use its own test command.

## Separate the Release

**Trigger a release only from an approved source ref.** Protect that ref with repository rules and human review. Put release credentials and `attestations: write` only in the release job. GitHub's [secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) warns about untrusted workflow inputs and privileged `pull_request_target` patterns. Avoid checking out attacker-controlled code into a privileged job.

**Inspect every action reference.** A version tag is readable, but a full commit ID better fixes the action code reviewed at a point in time. Record the owner, commit, purpose, and update process. Do not copy a random commit ID from an example into production without checking the action repository.

## Use Scorecard as a Review Queue

**Run OpenSSF Scorecard** against a public repository you own or a known public training repository. Follow the [official CLI or action setup](https://www.scorecard.dev/) and record the tool version, repository, time, check names, scores, and reasons. Scorecard's automated checks cover source, build, dependencies, and maintenance. A score is evidence to investigate, not proof of a secure release.

**Choose one actionable finding.** For example, a low Pinned-Dependencies score may lead you to pin a workflow action after reviewing its upstream commit. A low Branch-Protection score may lead you to require review on the release branch. Record the original finding, the exact control change, and a second Scorecard result after the change. If a check reports `?`, record unavailable evidence instead of treating it as zero risk. Read the [check definitions](https://github.com/ossf/scorecard/blob/main/docs/checks.md) before interpreting a result.

## Verify Your Work

**Pass this lesson** when your packet contains the two-job permissions table, one untrusted-input boundary, and one Scorecard finding with a reason and proposed correction. If you lack repository access, mark the hosted checks “not run” and evaluate the sample workflow on paper. Do not claim Scorecard observed a control you did not run.

**Next:** [Verify provenance and attestations](/articles/secure-cicd-provenance-attestations/).
