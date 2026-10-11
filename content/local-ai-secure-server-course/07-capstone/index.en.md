---
title: "Capstone: Plan and Validate a Secure Local AI Server"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Produce a deployment package for a measured, access-controlled, monitored, and recoverable local AI server."
genre: ["Artificial Intelligence", "Self-Hosted", "Capstone"]
tags: ["local AI capstone", "secure Ollama server", "llama.cpp deployment", "local LLM operations", "AI server plan"]
cover: "/img/cover/local-ai-secure-server-capstone.webp"
coverAlt: "Deployment package linking a model record, benchmark, network policy, tests, monitoring, and rollback"
coverCaption: "Capstone cover placeholder. Image generation follows editorial review."
---

[Return to the Local AI Course](/local-ai-secure-server-course-start/)

**Your capstone produces a deployment decision, not a running public service.** Use your measured host and model data. Keep tests on loopback or an approved private lab network.

## Choose a Track

**Beginner track:** One user on one host. The runtime stays on loopback. The package proves model identity, acceptable task output, measured memory, local API access, and update rollback.

**Advanced track:** Several approved users on a private network. The runtime stays on loopback behind an authenticated TLS gateway. The package adds per-user authorization, rate limits, concurrency limits, monitoring, backup, staged updates, and access-denial evidence.

## Required Package

Create **`local-ai-capstone/`**:

```text
local-ai-capstone/
  workload.md
  host-inventory.md
  model-record.md
  benchmark.md
  data-flow.md
  access-policy.md
  test-record.md
  update-rollback.md
  deployment-decision.md
```

## Build the Package

1. **Freeze the workload.** State input size, output size, users, latency target, and data class.
2. **Record the host.** Include CPU, RAM, GPU, VRAM, storage, operating system, and runtime version.
3. **Identify the model.** Include publisher, source, license, exact identifier, format, size, and digest where available.
4. **Measure the service.** Record three warm trials with separate prompt and generation rates.
5. **Draw data flow.** Show client, gateway, runtime, model storage, logs, updates, and outbound connections.
6. **Write access policy.** Name identities, routes, models, request limits, rate limits, and retention.
7. **Run boundary tests.** For the one-host beginner path, inspect the listener and record its `127.0.0.1` bind plus local firewall rules. A second private client is optional for a remote-denial test. For the advanced path, test authorized, unauthorized, oversized, listener, timeout, and overload behavior at the gateway.
8. **Test rollback.** Restore a prior approved configuration in the lab and repeat health and denial checks.
9. **Make a decision.** Choose approve, approve with conditions, or reject.

## Acceptance Rubric

| Area | Beginner pass | Advanced pass |
|---|---|---|
| **Model** | Source, license, identifier, and fit recorded | Digest and artifact retention added |
| **Quality** | Synthetic task reviewed | Fixed evaluation set and acceptance rule |
| **Performance** | Three warm single-user trials | Context, concurrency, queue, and overload profile |
| **Network** | Loopback-only runtime | Private route through gateway to loopback runtime |
| **Identity** | Host user boundary | Per-user authentication and route authorization |
| **Logs** | Local service and access record | Central protected metadata with retention rule |
| **Recovery** | Prior configuration restored | Runtime, model, driver, and policy rollback tested |

Fail the review when the service exposes a native runtime port to an untrusted network, lacks a clear model license, stores unneeded full prompts, or has no tested rollback.

## Reference Answer

A strong beginner decision reads:

> Approve for one local user with synthetic and low-sensitivity data. The runtime listens on loopback. The selected model fits with measured memory headroom. Three warm trials meet the stated response target. Remote access is absent. The prior configuration and model record support rollback.

A strong advanced decision reads:

> Approve with conditions for approved private-network users. The native runtime stays on loopback. An authenticated TLS gateway enforces per-user model access, request size, output, rate, and concurrency limits. Access tests show unauthorized and oversized requests denied before inference. Protected logs retain metadata under the stated schedule. Production data waits for privacy, legal, and incident reviews.

## Expected Result

Your package ties every claim to a source or observed test. The deployment decision names scope, conditions, evidence gaps, residual risk, owner, and review date.

## Troubleshooting

- **The selected model changed during testing:** Restart the benchmark record under one exact identifier.
- **Performance passes only after removing security controls:** Measure the approved end-to-end path and revise capacity.
- **Gateway tests pass but runtime port is reachable remotely:** Repair bind and firewall rules before approval.
- **Rollback restores service but access denial fails:** Treat rollback as failed and repair the prior policy package.
- **The decision lacks a data class:** Define allowed data before service approval.

## Verify Completion

```bash
find local-ai-capstone -maxdepth 1 -type f -print | sort
grep -Ein "model|license|digest|loopback|authentication|rollback|owner" \
  local-ai-capstone/deployment-decision.md
```

Pass when all nine files exist and all track requirements have evidence. The beginner path must show a loopback-only listener and recorded firewall policy, with remote denial labeled `not run` if no second client exists. The advanced path must show an unauthorized gateway request denied. The listener must match the design, rollback must pass the same checks, and the decision must name an owner for each remaining condition.

Return to the [course hub](/local-ai-secure-server-course-start/). Review the [Ollama documentation](https://docs.ollama.com/) and [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) before adapting commands to a newer release.
