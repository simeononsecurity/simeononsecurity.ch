---
title: "Lesson 8: Secure Your AI Broker: Virtual Keys, Budgets, and Allowed Models"
date: 2026-10-21
lastmod: 2026-10-21
toc: true
draft: false
description: "Give each AI agent its own broker key with rate limits, token and cost budgets, and a fail-closed model allow-list, so one runaway caller stops at its own ceiling."
genre: ["Artificial Intelligence", "Cybersecurity", "Self-Hosted"]
tags: ["ai broker", "virtual keys", "llm rate limit", "token budget", "cost budget", "allowed models", "model allow-list", "fail-closed", "denial of wallet", "openai-compatible", "local ai", "self-hosted ai", "llm governance", "rpm limit", "tpm limit", "api key rotation", "per-key budget", "tenant budget", "owasp llm10", "unbounded consumption", "broker security", "local-first ai", "agent security", "key hashing", "429 rate limit"]
cover: "/img/cover/secure-ai-broker-governance-2026.webp"
coverAlt: "Diagram of an AI broker checking a virtual key for rate limits, budgets, and an allowed-models list before reaching backends"
coverCaption: ""
---
[Return to the Hermes Agent and Local AI Course](/hermes-local-ai-broker-course-start/)

A **virtual key** is a per-caller credential your broker checks before it forwards a request to any backend. Give each agent and each person a separate key, attach **rate limits**, **token and cost budgets**, and a **model allow-list**, and one leaked or runaway caller stops at its own ceiling instead of draining your whole stack. This guide shows how to define those keys, read the exact refusal a blocked caller receives, and decide which limits belong on which key.

The guidance here maps to the governance layer of a local-first broker exposing one OpenAI-compatible endpoint. Every behavior below is backed by the broker's own test suite unless marked otherwise.

## Key Takeaways

- **Separate keys isolate blast radius.** A compromised key spends only its own budget until you revoke it.
- **Budgets are fail-closed.** A key with no token or cost headroom gets a 429, not a backend call.
- **Allow-lists bind the resolved model.** A key scoped to `chat` never reaches a model outside its list, even through `auto`.
- **Aperture and the broker split the work.** Aperture decides who reaches the endpoint. Broker keys decide what each caller spends and runs.
- **Keys live as hashes.** A leaked keys file yields SHA-256 hashes, not working secrets.

## Prerequisites

- A running broker exposing one OpenAI-compatible endpoint in front of your backends. A companion article in this series covers the one-endpoint setup.
- Admin access to the broker host to edit the keys file and reload the service.
- One or more backends registered in the broker, such as a local runtime like Ollama or llama.cpp, or a hosted provider.

**Estimated time:** 30 to 45 minutes. **Difficulty:** intermediate. You edit a YAML file, mint keys, and read HTTP error envelopes. No code changes.

## Who Reaches the Endpoint vs What a Key Spends

Two controls sit in front of your backends, and they answer different questions. Keeping them separate is the core of a safe local-first setup.

**[Tailscale](/articles/tailscale-vs-headscale-comparison-guide/) Aperture** is the private edge. It decides **who** reaches the broker at all. Callers arrive over your tailnet with a machine identity, and the broker binds locally instead of listening on a public port. This keeps the endpoint off the public internet. Aperture is a deployment property you configure at the network layer. The broker code does not enforce it, so treat the private edge as an operator responsibility.

**Broker virtual keys** are the governance layer. Once a caller reaches the endpoint, its key decides **what** the caller spends and **which** models it reaches. Rate limits, token and cost budgets, and the model allow-list all live on the key. This is the layer the rest of this article configures.

| Control | Question it answers | Where it lives |
|---------|---------------------|----------------|
| **Aperture private edge** | Who reaches the broker | Tailnet and network config |
| **Broker virtual key** | What the caller spends and runs | Broker keys file |

Front the broker with Aperture for identity, then lean on keys for spend and model scope. Neither replaces the other.

## One Key Per Caller

Give every agent profile and every person a distinct key. The broker stores only the **SHA-256 hash** of each secret. The plaintext secret appears once, at creation, and is never retrievable afterward. A leaked keys file exposes hashes, not working credentials.

Mint a key with the broker's key tool:

```bash
python -m broker.keys create --label team-example --scope user
```

The tool prints the secret one time, in the form `brk_<id>_<random>`. Store it in your agent's secret manager right away. *Command shown as documented usage, untested in this article.*

Authentication is **generic on failure**. An unknown key, a revoked key, an expired key, and a wrong secret all return the same **401**, compared in constant time. A blocked caller learns only its key failed, not which reason applied.

## The Limits You Set Per Key

Each key carries its own ceilings. The broker enforces them before a request reaches a backend, so an over-budget caller never costs you compute. The table below pairs each limit with the abuse it stops.

| Limit | What it stops |
|-------|---------------|
| **`rpm`** | Too many requests per minute from one caller |
| **`rpm_burst`** | Short spikes above the steady rate, in GCRA mode |
| **`tpm`** | Token floods inside a single minute |
| **`max_concurrency`** | One caller holding many in-flight slots at once |
| **`daily_token_budget`** | A slow token drain across a day |
| **`monthly_token_budget`** | A slow token drain across a month |
| **`daily_cost_usd`** | Runaway spend in a single day |
| **`monthly_cost_usd`** | Runaway spend across a month |
| **`allowed_models`** | A caller reaching a model outside its list |
| **`per_model`** | One model soaking a key's entire rate budget |
| **`placement`** | Data processing outside an allowed location |
| **Tenant budgets** | One team's keys overspending in aggregate |

Rate limits (`rpm`, `tpm`, `max_concurrency`) throttle bursts. Budgets (`token` and `cost`, daily and monthly) cap sustained use and reset on their period boundary. The allow-list and `placement` bound scope rather than volume.

## A Keys File, End to End

Define keys in a YAML file the broker reads at startup. The example below shows one rate- and budget-limited user key and one admin key. Every secret value is a placeholder. The real `keys.yaml` is git-ignored, and only the hash is stored.

```yaml
keys:
  # Rate- and budget-limited user key. All values are placeholders.
  - id: 1a2b3c4d                 # non-secret lookup id; the secret is brk_<id>_<random>
    label: team-example
    tenant: example-tenant
    scope: user
    secret_sha256: "0000000000000000000000000000000000000000000000000000000000000000"
    enabled: true
    expiry: null                 # ISO "YYYY-MM-DD" or null for never
    limits:
      rpm: 60
      rpm_burst: 10              # GCRA burst; applies with BROKER_RATE_LIMIT_ALGO=gcra
      tpm: 100000
      max_concurrency: 4
      daily_token_budget: 1000000
      monthly_token_budget: 20000000
      daily_cost_usd: 5.0
      monthly_cost_usd: 100.0
      allowed_models: [chat, auto]   # fail-closed; also binds auto's resolved pick
      placement: [local]             # unioned with x-broker-placement; tightens only
      per_model:
        chat: { rpm: 30, tpm: 50000 }

  # Admin key, no limits, reads every key's usage. Placeholder hash.
  - id: 9f8e7d6c
    label: ops-admin
    scope: admin
    secret_sha256: "1111111111111111111111111111111111111111111111111111111111111111"
    enabled: true

# Aggregate per-tenant budgets, shared by every key with this tenant and
# enforced in addition to per-key budgets. Placeholder values.
tenants:
  example-tenant:
    daily_token_budget: 5000000
    monthly_token_budget: 100000000
    daily_cost_usd: 25.0
    monthly_cost_usd: 400.0
```

A caller then uses its secret as a bearer token. The broker checks the hash, applies the limits above, and forwards the request only if the key has headroom.

```bash
curl https://<broker-host>/v1/chat/completions \
  -H "Authorization: Bearer <USER_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"model":"chat","messages":[{"role":"user","content":"hello"}]}'
```

On success, the response carries `x-ratelimit-*` headers so the caller sees its remaining budget. *Command shown as documented usage, untested in this article.*

## What a Blocked Caller Sees

A refused request returns a structured error envelope. Reading it tells you which ceiling tripped and whether a retry helps. There are two distinct 429 cases, and the difference matters.

A **rate limit** is transient. The caller sent requests too fast, and the `Retry-After` value is a short number of seconds. The broker returns these headers:

```text
HTTP/1.1 429 Too Many Requests
retry-after: 60
x-ratelimit-limit-requests: 2
x-ratelimit-remaining-requests: 0
x-ratelimit-reset-requests: 60
content-type: application/json
```

The body names the limit and gives remediation:

```json
{
  "error": {
    "message": "request rate limit of 2/min reached",
    "type": "rate_limit_exceeded",
    "code": "rate_limit_exceeded",
    "param": null,
    "backend": null,
    "model": null,
    "state": null,
    "remediation": "slow down; see Retry-After and x-ratelimit headers"
  }
}
```

A **budget exhaustion** is not transient. A daily or monthly token or cost ceiling is spent, and `Retry-After` holds the seconds to the next UTC reset. The header block is shorter because no per-minute window applies:

```text
HTTP/1.1 429 Too Many Requests
retry-after: 37194
content-type: application/json
```

The body uses a different type so the caller knows waiting out a minute will not help:

```json
{
  "error": {
    "message": "daily token budget of 1000000 exhausted",
    "type": "insufficient_quota",
    "code": "insufficient_quota",
    "param": null,
    "backend": null,
    "model": null,
    "state": null,
    "remediation": "wait for the daily reset or raise the budget"
  }
}
```

A request for a model outside the key's allow-list returns a **403**, not a 429, because the fix is a policy change rather than a wait:

```json
{ "error": { "code": "model_not_allowed", "type": "...", "message": "model not in allowed_models" } }
```

> **Key Takeaway:** `rate_limit_exceeded` means retry soon. `insufficient_quota` means the budget period must reset or grow. `model_not_allowed` means the key is scoped away from the model.

## Fail-Closed Model Allow-Lists

The `allowed_models` list is **fail-closed**. A caller reaches only the models named on its key. A request for anything else returns **403 `model_not_allowed`** before any backend runs.

The check binds the **resolved** model, not the requested alias. When a key allows `auto`, the broker picks a concrete model, then re-checks the pick against the allow-list and against per-model limits at every cascade hop. A caller has no route past its allow-list by requesting `auto` and hoping the router lands on a model it should not reach.

*Scope keys tightly.* A coding agent limited to one chat model has a far smaller abuse surface than a key allowed to reach every backend you host.

## Cost Budgets Stop Denial of Wallet

Token budgets cap volume. **Cost budgets** cap spend. The broker tracks per-key cost in integer micro-USD using the pricing in your model registry, and it refuses a call once the daily or monthly cost ceiling is reached. An unpriced model records zero cost, so set pricing on every model you bill against.

Uncontrolled inference spend is **[OWASP LLM10:2025 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/)**, and the financial form of it is **Denial of Wallet**. Per-key cost budgets are the direct control for it. On a hosted backend they bound your bill. On a local runtime they bound how long your GPU runs for any one caller.

## Who Reads Usage

The `/usage` endpoint is **scope-aware**. A user key reads only its own counters. An admin key reads every key's usage, broken down by key. A leaked user key exposes one caller's numbers, not the whole fleet's spend.

Keep the admin key out of agent configs. Reserve it for the operator dashboard and billing reconciliation.

## Rotating and Revoking Keys

Rotation mints a **successor** key with a short grace window, so a live agent keeps working during the swap. Rotation only **shortens** a key's life, never extends it, and it refuses to resurrect a revoked or expired key, returning **409 `key_not_active`**. To cut a caller off at once, set `enabled: false` on its key and reload the broker.

> **Best Practice:** Give high-traffic agents a short `expiry` and rotate on a schedule. A stolen key then ages out on its own even if you miss the theft.

## What the Broker Does Not Do

An honest control list names its gaps. The broker's governance layer has clear edges.

- **It does not stop prompt injection.** The broker treats backend and tool output as data, never as control. It does not parse or act on model output. Prompt-injection defense belongs at the agent boundary. The [AI agent trust boundaries lesson](/secure-ai-agents-mcp-course/01-agent-trust-boundaries/) covers this control.
- **Legacy flat keys stay unlimited.** Keys defined through the old `BROKER_API_KEYS` variable keep working with no budgets and no rate-limit headers, and they are never throttled. Migrate them into the keys file to govern them.
- **It does not keep the host off the internet by itself.** The private-edge property comes from Aperture and your network config, not from broker code.
- **It does not log secrets.** Only a non-secret id and fingerprint reach the usage log and metrics. Key material never lands in logs, errors, or default traces. *This is enforced in code and documented, with no dedicated test in the governance suite.*

## Common Mistakes

> **Common Mistake:** Sharing one key across every agent. A single leaked or buggy caller then spends the whole budget. Mint a separate key per caller.

> **Common Mistake:** Setting token budgets but no cost budget. A low token count on an expensive model still drains your wallet. Set both.

> **Common Mistake:** Allowing `auto` on a narrow key and assuming the router stays cheap. Bind the key to the specific models you accept, and add per-model limits.

> **Common Mistake:** Leaving old `BROKER_API_KEYS` entries in place. They run unlimited and unthrottled. Move them into the keys file.

> **Common Mistake:** Treating the tailnet edge as the whole defense. Aperture controls reach, not spend. A trusted caller with a broad key still overspends without budgets.

## Next Steps

You now scope each caller with its own key, read the exact refusal it receives, and decide which ceiling belongs where. Pair this with the agent-side controls handling the risks the broker leaves open.

- Take the [Secure AI Agents and MCP Course](/secure-ai-agents-mcp-course-start/) to contain the agent consuming a model's output.
- Read [Local AI Privacy: What Stays on Your Computer and What Does Not](/articles/local-ai-privacy-boundary/) to decide which data stays local before it reaches any key.

{{< centerbutton href="/secure-ai-agents-mcp-course-start/" >}}
  Take the Secure AI Agents Course
{{< /centerbutton >}}

Continue with [Lesson 9: Threat-Model the Stack](/hermes-local-ai-broker-course/09-threat-model/).
