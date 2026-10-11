---
title: "Dependency Review and SBOMs for a Secure Release"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Review a dependency change, record its risk, and generate a CycloneDX SBOM before releasing software."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["dependency review", "SBOM tutorial", "CycloneDX", "Syft", "software supply chain"]
cover: "/img/cover/secure-cicd-course.webp"
coverAlt: "A source repository, build runner, artifact, and verification gate connected in a release workflow"
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**A release inherits the code and build inputs it consumes.** Review changed dependencies before merge, then record the components present in the built output. These are related checks with different questions. A pull request review asks what changed. A software bill of materials, or **SBOM**, records what a scanner found in a chosen artifact.

## Key Takeaways

- **Dependency review** compares a proposed revision with its base and flags known risk.
- **An SBOM** lists discovered components. It does not certify their safety or the publisher's identity.
- **Your decision record** should name the version, source, reason, risk, and owner.

## Prerequisites

**Use a disposable repository** for hosted work. The local SBOM route needs the [Syft CLI](https://github.com/anchore/syft) installed from its official release instructions. Check the installed binary with `syft version`. The review route needs a GitHub repository with a dependency graph and a pull request. Read [GitHub's dependency review guide](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-dependency-changes-in-a-pull-request) before starting. Plan 35 minutes.

## Review the Change

**Open the pull request's Files changed tab.** Find the manifest and lockfile. Expand the dependency review view. Write down each direct package change, its new version, any transitive additions, the reported advisory, and the reason the application needs the package. Inspect the lockfile even if the manifest changes by one line.

| Question | Record in your packet |
|---|---|
| **What changed?** | Package name, old and new version, direct or transitive |
| **Why now?** | Feature or fix requiring the change |
| **What is known?** | Advisory identifier, affected range, review date |
| **Who accepts it?** | Named maintainer and remediation date |

**Expected result:** Your packet distinguishes observed dependency facts from your acceptance decision. If GitHub shows no dependency diff, confirm the repository's dependency graph and ecosystem support. Do not infer “safe” from an empty view. GitHub documents the [feature's availability and limits](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review).

## Add a Review Gate

**Create a pull request workflow in a disposable repository.** Use the current [GitHub example](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-dependency-review-action) as the source of truth for supported action versions and settings. The core job needs read access to contents:

```yaml
name: Dependency review
on: pull_request
permissions:
  contents: read
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
        with:
          persist-credentials: false
      - uses: actions/dependency-review-action@v4
```

**Expected result:** A pull request adds a dependency review check. If the check fails because the feature is unavailable, inspect repository plan, dependency graph, and the action log. Do not bypass a blocked check without recording a review decision. Pin third-party actions to full commit IDs in a production workflow after validating the owner and release, as [GitHub recommends](https://docs.github.com/en/actions/reference/security/secure-use).

## Generate a Component Inventory

**Scan a chosen directory or image.** In a scratch project with a recognized package manifest, run:

```bash
syft dir:. -o cyclonedx-json=sbom.cdx.json
```

**Expected result:** `sbom.cdx.json` is a JSON document with a CycloneDX format marker and the components Syft found. Open it and search for one dependency from your review record. Syft documents [directory sources and CycloneDX output](https://github.com/anchore/syft). If the list is empty, check that you scanned the directory containing the manifest or build artifact. Scanner coverage varies by ecosystem and source type.

**Record the scan target and tool version.** An SBOM for a source tree and an SBOM for a released image answer different questions. Keep the generated file beside the release packet, but keep generated files out of your source commit unless your release policy requires them.

## Verify Your Work

**Pass this lesson** when your record identifies at least one package change, its reason, a review decision, the scan target, the Syft version, and one component found in the SBOM. If you used the local path only, mark the GitHub check “not run.”

**Next:** [Limit pipeline authority and use Scorecard](/articles/secure-cicd-pipeline-scorecard/).
