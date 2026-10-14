---
title: "Capstone: Plan and Validate a Secure Local AI Server"
date: 2026-10-10
lastmod: 2026-10-14
toc: true
draft: false
description: "Produce a deployment package for a measured, access-controlled, monitored, and recoverable local AI server."
genre: ["Artificial Intelligence", "Self-Hosted", "Capstone"]
tags: ["local AI capstone", "secure Ollama server", "llama.cpp deployment", "local LLM operations", "AI server plan"]
cover: "/img/cover/local-ai-secure-server-capstone.webp"
coverAlt: "Deployment package linking a model record, benchmark, network policy, tests, monitoring, and rollback"
coverCaption: ""
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
7. **Run boundary tests.** For the one-host beginner path, inspect the listener and record its `127.0.0.1` bind plus local firewall rules. A second private client is optional for a remote-denial test. For the advanced path, use the [tested gateway lab source](/downloads/local-ai-secure-server-course/secure_gateway_lab.py) from Lesson 5 to test authorized, unauthorized, oversized, unexpected-path, response-size, and rate-limit behavior. Inspect both loopback listeners. Test timeout and concurrency overload on your own approved gateway. The advanced capstone is incomplete until those two observed results exist. Separate synthetic lab evidence from server evidence.
8. **Test rollback.** Restore a prior approved configuration in the lab and repeat health and denial checks.
9. **Make a decision.** Choose approve, approve with conditions, or reject.

### Beginner Rollback Drill

Use the course gateway lab for a concrete rollback drill. It uses fixed loopback ports and synthetic responses. For your own runtime, repeat the same checks with its documented service command.

```bash
mkdir -p local-ai-rollback
cp secure_gateway_lab.py local-ai-rollback/secure_gateway_lab.before.py
cp secure_gateway_lab.py local-ai-rollback/secure_gateway_lab.py
hash_file() { if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1"; else shasum -a 256 "$1"; fi; }
check_listeners() { if command -v ss >/dev/null 2>&1; then ss -ltn | grep -E ':(18080|18443) '; else lsof -nP -iTCP:18080 -sTCP:LISTEN; lsof -nP -iTCP:18443 -sTCP:LISTEN; fi; }
# On macOS, the fallback above uses /usr/bin/shasum and /usr/sbin/lsof.
hash_file local-ai-rollback/secure_gateway_lab.before.py
python3 - <<'PY'
from pathlib import Path
path = Path("local-ai-rollback/secure_gateway_lab.py")
text = path.read_text()
path.write_text(text.replace("MAX_BODY = 512", "MAX_BODY = 256", 1))
PY
python3 local-ai-rollback/secure_gateway_lab.py > local-ai-rollback/changed.log 2>&1 &
LAB_PID=$!
trap 'kill "$LAB_PID" 2>/dev/null || true' EXIT
sleep 1
```

The controlled change lowers the request limit from 512 to 256 bytes. Record the changed health response, listener addresses, and unauthorized request result:

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:18443/api/chat \
  -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"message":"READY"}'
check_listeners
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:18443/api/chat \
  -H 'Content-Type: application/json' -d '{"message":"READY"}'
python3 - <<'PY' | curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:18443/api/chat \
  -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
  -H 'Content-Type: application/json' --data-binary @-
import json
print(json.dumps({"message": "A" * 400}))
PY
kill "$LAB_PID"
wait "$LAB_PID" 2>/dev/null || true
cp local-ai-rollback/secure_gateway_lab.before.py local-ai-rollback/secure_gateway_lab.py
hash_file local-ai-rollback/secure_gateway_lab.py
python3 local-ai-rollback/secure_gateway_lab.py > local-ai-rollback/restored.log 2>&1 &
LAB_PID=$!
sleep 1
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:18443/api/chat \
  -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
  -H 'Content-Type: application/json' -d '{"message":"READY"}'
check_listeners
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:18443/api/chat \
  -H 'Content-Type: application/json' -d '{"message":"READY"}'
python3 - <<'PY' | curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:18443/api/chat \
  -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
  -H 'Content-Type: application/json' --data-binary @-
import json
print(json.dumps({"message": "A" * 400}))
PY
kill "$LAB_PID"
wait "$LAB_PID" 2>/dev/null || true
trap - EXIT
```

Expected status codes are `200`, `401`, and `413` before restore, then `200`, `401`, and `200` after restore. Record both hashes, observed results, cleanup, and any test left `not run`. Do not expose the service during this drill. The synthetic lab does not prove a production runtime rollback.

## Acceptance Rubric

| Area | Beginner pass | Advanced pass |
|---|---|---|
| **Model** | Source, license, identifier, and fit recorded | Digest and artifact retention added |
| **Quality** | Synthetic task reviewed | Fixed evaluation set and acceptance rule |
| **Performance** | Three warm single-user trials | Context and concurrency measurements, plus observed timeout and overload results from the approved gateway. A test plan alone earns partial credit. |
| **Network** | Loopback-only runtime | Private route through gateway to loopback runtime |
| **Identity** | Host user boundary | Per-user authentication and route authorization |
| **Logs** | Local service and access record | Central protected metadata with retention rule |
| **Recovery** | Prior configuration restored | Runtime, model, driver, and policy rollback tested |

Fail the review when the service exposes a native runtime port to an untrusted network, lacks a clear model license, stores unneeded full prompts, or has no tested rollback.

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

Pass when all nine files exist and all track requirements have evidence. The beginner path must show a loopback-only listener and recorded firewall policy, with remote denial labeled `not run` if no second client exists. The advanced path must show an unauthorized gateway request denied in the synthetic lab plus observed timeout and concurrency overload results from the approved gateway. The synthetic lab does not test timeout or concurrency overload. The listener must match the design, rollback must pass the same checks, and the decision must name an owner for each remaining condition.

After you finish the package and decision, compare them with the separate [capstone answer key](/local-ai-secure-server-course/09-capstone-answer-key/).

Return to the [course hub](/local-ai-secure-server-course-start/). Review the [Ollama documentation](https://docs.ollama.com/) and [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) before adapting commands to a newer release.
