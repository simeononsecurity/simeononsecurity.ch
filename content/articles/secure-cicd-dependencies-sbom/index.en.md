---
title: "Dependency Review and SBOMs for a Secure Release"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Review a dependency change, record its risk, and generate a CycloneDX SBOM before releasing software."
genre: ["Software Engineering", "Cybersecurity", "DevOps"]
tags: ["dependency review", "SBOM tutorial", "CycloneDX", "Syft", "software supply chain"]
cover: "/img/cover/secure-cicd-dependencies-sbom.webp"
coverAlt: "A reviewer follows a package dependency tree to a bill of materials with one new package highlighted."
coverCaption: ""
---

[Return to the Secure CI/CD Course](/secure-cicd-course-start/)

**A release inherits the code and build inputs it consumes.** Review changed dependencies before merge, then record the components present in the built output. These are related checks with different questions. A pull request review asks what changed. A software bill of materials, or **SBOM**, records what a scanner found in a chosen artifact.

## Key Takeaways

- **Dependency review** compares a proposed revision with its base and flags known risk.
- **An SBOM** lists discovered components. It does not certify their safety or the publisher's identity.
- **Your decision record** should name the version, source, reason, risk, and owner.

## Prerequisites

**Download and extract the [lab archive](/downloads/secure-cicd-lab.zip).** Enter its `secure-cicd-lab` folder. Python 3.10 or later runs the local path. Syft and GitHub are optional. For hosted work, use a disposable repository with a dependency graph and a pull request. Read [GitHub's dependency review guide](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-dependency-changes-in-a-pull-request). Plan 35 minutes.

**Terms:** A **manifest** declares direct packages. A **lockfile** records resolved versions, including transitive packages pulled in by direct packages. An **advisory** describes a reported vulnerability. A **scan target** is the directory, image, or artifact inspected. **CycloneDX** is an SBOM data format. The local files are synthetic examples with no real advisory claim.

## Inspect a Local Change

**Open `sample-dependency-change.json`.** Compare `before` with `after`. The direct `workshop-core` version changes from `1.0.0` to `1.1.0`, and `workshop-parser` appears as a new transitive package. Write one packet row: `workshop-parser 2.0.0 | transitive addition | advisory not assessed | hold for owner review`. The fixture does not claim a real package or vulnerability.

**Run the local inspection command** from the extracted folder:

```bash
python3 inspect_packet.py
```

**Expected result:** The first lines show `Direct version: 1.0.0 -> 1.1.0` and `New transitive package: workshop-parser`. On Windows use `py -3 inspect_packet.py`. If Python cannot find the script, enter the extracted `secure-cicd-lab` folder. Keep your own reasoning in the packet. The script prints facts but does not approve the change.

## Review the Change

**For the optional hosted path, open the pull request's Files changed tab.** Find the manifest and lockfile. Expand the dependency review view. Write down each direct package change, its new version, any transitive additions, the reported advisory, and the reason the application needs the package. Inspect the lockfile even if the manifest changes by one line.

| Question | Record in your packet |
|---|---|
| **What changed?** | Package name, old and new version, direct or transitive |
| **Why now?** | Feature or fix requiring the change |
| **What is known?** | Advisory identifier, affected range, review date |
| **Who accepts it?** | Named maintainer and remediation date |

**Expected result:** Your packet distinguishes observed dependency facts from your acceptance decision. The local row uses the fixture and says “advisory not assessed.” If GitHub shows no dependency diff, confirm the repository's dependency graph and ecosystem support. Do not infer “safe” from an empty view. GitHub documents the [feature's availability and limits](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review).

## Add a Review Gate

**For the hosted path, create `.github/workflows/dependency-review.yml` in a disposable repository.** Use the current [GitHub example](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-dependency-review-action) as the source of truth for supported action versions and settings. The core job needs read access to contents:

```yaml
name: Dependency review
on: pull_request
permissions:
  contents: read
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
        with:
          persist-credentials: false
      - uses: actions/dependency-review-action@v5
```

Dependency Review Action v5 uses the Node 24 runtime and needs an Actions runner at version 2.327.1 or newer. If your disposable runner is older, record the compatibility limit and use the supported version for that runner instead of silently changing the gate.

**Expected result:** After you open a pull request, its Checks tab shows dependency review. If the check fails because the feature is unavailable, inspect repository plan, dependency graph, and the action log. Do not bypass a blocked check without recording a review decision. Pin actions to full commit IDs in a production workflow after validating the owner and release, as [GitHub recommends](https://docs.github.com/en/actions/reference/security/secure-use).

## Generate a Component Inventory

**First read `sample-sbom.cdx.json`.** It lists two synthetic library components. Record `workshop-parser 2.0.0`, the `CycloneDX` format marker, and the fact that this is a supplied example, not a scan result. The file gives the local path a complete inventory exercise.

**For the optional tool path, install Syft** using the official [installation guide](https://oss.anchore.com/docs/installation/syft/) for your operating system. Check `syft version`. In a scratch project with a recognized package manifest, run:

```bash
syft dir:. -o cyclonedx-json=sbom.cdx.json
```

**Expected result:** `sbom.cdx.json` is a JSON document with a CycloneDX format marker and the components Syft found. Open it and search for one dependency from your real project. Syft documents [directory sources and CycloneDX output](https://github.com/anchore/syft). If the list is empty, check that you scanned the directory containing the manifest or build artifact. Scanner coverage varies by ecosystem and source type. Do not expect a real Syft scan to reproduce the synthetic fixture exactly.

**Record the scan target and tool version.** An SBOM for a source tree and an SBOM for a released image answer different questions. Keep the generated file beside the release packet, but keep generated files out of your source commit unless your release policy requires them.

## Verify Your Work

**Pass this lesson** when your record identifies the direct version change, the transitive addition, the unassessed advisory, a hold decision, and one component in the supplied SBOM. If you used Syft, add its scan target, version, and result. Mark hosted checks “not run” when you use only the local path.

**Next:** [Limit pipeline authority and use Scorecard](/articles/secure-cicd-pipeline-scorecard/).
