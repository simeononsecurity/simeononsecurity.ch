---
title: "Threat Model: Your Local AI Agent Stack Under Attack"
date: 2026-10-21
lastmod: 2026-10-21
toc: true
draft: false
description: "Map the real attack surface of a local AI agent stack: agents, a Tailscale private edge, an OpenAI-compatible broker, and GPU backends. See which controls hold in code and what stays unsolved."
genre: ["Cybersecurity", "Local AI", "Threat Modeling", "AI Security", "Self-Hosted AI"]
tags: ["local ai threat model", "ai agent security", "ai broker security", "ssrf", "prompt injection", "path traversal", "shell injection", "tailscale aperture", "private edge", "owasp llm top 10", "llm01 prompt injection", "excessive agency", "unbounded consumption", "ai gateway", "virtual api keys", "rate limiting", "lateral movement", "gpu host security", "secret leakage", "trust boundary", "self-hosted ai security", "agent attack surface", "openai compatible broker", "local inference security", "defense in depth"]
cover: "/img/cover/local-ai-agent-stack-threat-model.webp"
coverAlt: "Abstract diagram of a layered local AI agent stack with trust boundaries between agents, a private edge, a broker, and GPU backends"
coverCaption: ""
---

**A local AI agent stack is not one trusted machine.** It is a chain of trust boundaries: autonomous agents, a private network edge, a request broker, and the GPU backends behind it. Every boundary is a place where an attacker with the wrong foothold reaches further than you intend. This page models the attack surface of one specific design, names which controls hold in code, and states which protections are only deployment choices or out of scope on purpose.

*The design under test is Agents to a Tailscale private edge to an OpenAI-compatible broker to local and cloud model backends. A public internet edge such as LiteLLM is out of scope and appears once as the alternative.*

## Key Takeaways

- **Four boundaries, four attack surfaces.** Agent, private edge, broker, and backend each fail differently. Treat them separately.
- **Most broker-side controls are enforced in code and backed by tests**, from constant-time key checks to SSRF and path confinement.
- **The broker does not solve prompt injection.** It refuses to treat model and tool output as control, nothing more. Agent-side controls own the rest.
- **The private edge has no public ports by deployment, not by broker code.** Network segmentation is an operator responsibility.
- **A valid stolen key still works inside its budget until you revoke it.** Tight per-key limits and short lifetimes shrink the blast radius, they do not remove it.

## Prerequisites

This page assumes you know the stack from its companion articles. Read the [brokerized local AI workflow overview](/articles/hermes-agent-local-ai-brokerized-workflow-2026/) for the whole design, the [Tailscale private edge setup](/articles/tailscale-aperture-local-ai-gateway-2026/) for the edge, and the [broker governance guide](/articles/secure-ai-broker-governance-2026/) for keys and budgets. For the agent side of the chain, start with [AI agent trust boundaries](/secure-ai-agents-mcp-course/01-agent-trust-boundaries/).

## The Four Trust Boundaries

A request flows left to right. Identity, data, and authority change hands at each arrow:

**Agents** to **private edge** to **broker** to **backends**.

- An **agent** is an autonomous client: a Hermes bot profile or a coding agent. It holds a credential and makes requests on your behalf.
- The **private edge** is a Tailscale gateway. It authenticates the caller by tailnet identity and forwards granted traffic. It listens on the tailnet, not the public internet.
- The **broker** is an OpenAI-compatible reverse proxy. It authenticates keys, enforces budgets, validates every request-derived value, and dispatches to a backend.
- A **backend** is a model runtime: a local GPU process or a cloud provider.

The sections below walk the chain one boundary at a time. Each table lists the attack, the control in this stack, and where each control is proven. The columns stay narrow on purpose so the tables read on a phone.

## Boundary One: The Private Edge

The edge decides who even reaches the broker. Identity comes from the tailnet. The Tailscale gateway resolves the caller's address to a login, device, and tags, so a client does not forge its own identity. Access is deny-by-default: network reachability to the gateway grants no model access until a matching grant allows it.

The real risk here is a grant written too wide.

| Attack | Control in this stack |
|--------|-----------------------|
| **Over-broad tailnet grants** | Deny-by-default authorization. A request reaches a model only through an explicit additive grant scoped to a user, group, or tag |
| **Reaching the edge from the open internet** | The gateway listens on the tailnet, not on a public port, so there is no internet-facing listener to scan |

A new gateway ships with wide default grants. Narrowing them to the identities you intend is the step turning deny-by-default into real enforcement. Reserve service tags for CI and shared hosts, since a tag collapses every session under one synthetic identity and destroys per-user attribution.

> **Warning:** The no-public-ports property is a deployment choice of the edge, not something broker code enforces. If you expose the broker another way, this protection is gone.

## Boundary Two: The Broker's Front Door

Every request presents a virtual key as a Bearer token or `X-API-Key` header. The broker stores only a SHA-256 hash of each secret, so a leaked key file yields hashes, not usable credentials. Unknown, revoked, expired, and wrong-secret keys all fail with the same generic 401 through a constant-time comparison, which denies an attacker both an oracle and a timing side channel.

| Attack | Control in this stack |
|--------|-----------------------|
| **Compromised or leaked client key** | Per-key request, token, and cost budgets cap blast radius. Fail-closed `allowed_models` and placement scoping. Revoke or rotate with a kill-switch refusing to resurrect a dead key |
| **Oversized-request denial of service** | A request-size limit (default 2 MB) rejects large bodies with HTTP 413 through a content-length fast path and a post-read length check |

Key rotation mints a successor with a grace overlap and only shortens a key's life, never extending a revoked one. Budgets map directly to **LLM10:2025 Unbounded Consumption** in the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): a stolen key cannot spend past its daily and monthly token and cost limits.

The honest limit: a valid stolen key works within its budget until you revoke it. The broker does not flag in-budget use as anomalous. Short expiry, tight per-key limits, and rotation shrink the window. An external gateway or SIEM owns anomaly detection.

## Boundary Three: Inside the Broker

Once a request is authenticated, its fields are still untrusted input. Two classes of attack live here: smuggling operating-system commands through request data, and smuggling instructions through model and tool output.

| Attack | Control in this stack |
|--------|-----------------------|
| **Shell or flag injection via request fields** | Request-derived values are scanned for CLI flags, shell metacharacters, and NUL bytes. Child processes build as an argv list from whitelisted placeholders and run with no shell anywhere |
| **Prompt injection through tool or upstream output** | The broker treats upstream content as data, never as control. It does not parse, execute, or route on model or tool output |

The command-injection defense is strong because no shell exists in the dispatch path. The executable and the argument template come from configuration, not from requests, so the smuggling surface is narrow. This closes the entire shell-injection class at the broker.

> **Key Takeaway:** The broker provides no prompt-injection mitigation for the agent. It only refuses to act on untrusted content itself.

Prompt injection is the attack where external content an agent reads contains hidden instructions. **LLM01:2025 Prompt Injection** and **LLM06:2025 Excessive Agency** both live at the agent boundary, not the broker. The broker forwarding content as data does not stop a coding agent from obeying a malicious comment in a file it fetched. Agent-side controls own this problem. See [AI agent trust boundaries](/secure-ai-agents-mcp-course/01-agent-trust-boundaries/) and [the local AI privacy boundary](/articles/local-ai-privacy-boundary/) for where those controls belong.

## Boundary Four: Broker to Backends

When the broker dials a backend, the destination URL and the model path are attack surfaces. A tricked outbound request is server-side request forgery. A crafted model path is file-system traversal.

| Attack | Control in this stack |
|--------|-----------------------|
| **SSRF via upstream or backend URL** | The outbound URL must use `http` or `https` and must start with a trusted backend base. The resolved address blocks link-local, multicast, reserved, unspecified, and the cloud-metadata IP `169.254.169.254` |
| **Path traversal in model paths** | Model paths resolve to a real path confined under an allowed root. The `..` and symlink escapes are rejected, and the check fails closed when no root is configured |

The SSRF guard keeps the broker from becoming a pivot into internal services or a cloud metadata endpoint. The base-URL allow-list is the primary wall.

Two honest gaps remain. Loopback backends are allowed by default, because local runtimes bind to `127.0.0.1`. Disable the loopback toggle where runtimes are not co-located. A time-of-check to time-of-use DNS rebinding between the address check and the connect is not fully closed in-process, so the allow-list carries the weight. Mis-scoping the allowed model roots weakens path confinement, which is operator trust, not a code flaw.

## Boundary Five: The GPU Host

If an attacker reaches a backend runtime or the GPU host, the question is how far they move. The broker limits the pivot, it does not own the host.

| Attack | Control in this stack |
|--------|-----------------------|
| **Lateral movement from a reached backend** | Runtimes launch argv-only with no shell and in a new session, so the broker signals only its own process tree. The SSRF allow-list blocks internal and metadata pivots. Placement pins where data is permitted to process. Container hardening runs non-root with a read-only root filesystem and dropped capabilities |
| **Signalling the wrong process after a restart** | A durable runtime identity of process id, start time, and argv hash so reconciliation never signals a process the broker did not start (proposed on the unmerged ADR 0021 branch) |

The runtime-identity gate is real work, but it lives on a branch and is not merged to the main line yet. Treat it as planned, not shipped. A backend runtime's own internal safety is outside broker control. Network segmentation of the GPU host through the private edge is an operator responsibility, not a broker-enforced control.

## Cross-Cutting: Secret Leakage

Keys leak through logs, traces, and git history more often than through a broken auth check.

| Attack | Control in this stack |
|--------|-----------------------|
| **Key material in logs, metrics, or errors** | Keys are hashed at rest and shown once. Only a non-secret id or fingerprint reaches the usage log. Error envelopes carry remediation text, never key values |
| **Secrets committed to git** | The environment file and the live keys file are git-ignored, placeholders ship in the example files, and a secret scanner runs in CI |

One opt-in setting reopens this surface. Turning on request-content tracing sends prompts and responses, often full of personal data, to the trace backend. Leave it off or retain it briefly. Response and semantic caches store full bodies in the state store, so treat the store as confidential and scope its key prefix. This maps to **LLM02:2025 Sensitive Information Disclosure** in the OWASP list.

## What This Stack Deliberately Does Not Expose

Some surfaces are closed by design. Naming them is as useful as naming the threats, because it tells you what an attacker cannot reach even with a valid key.

| Surface kept closed | Why |
|---------------------|-----|
| **Arbitrary executable from a request** | The runtime binary comes from configuration and must pass executable validation, so a request never picks the binary |
| **Arbitrary model path from a request** | Model paths come from the registry and must resolve under an allowed root |
| **Any shell or command string** | No shell runs anywhere, and children are argv lists, which removes the shell-injection class |
| **Silent model fallback** | An unknown model alias returns 404, never a substitute model |
| **Non-allow-listed or metadata backends** | The SSRF guard blocks them, including `169.254.169.254` |
| **Admin control plane, by default** | The admin API is off unless enabled, and its scope is separate from data-plane keys |
| **Web UI, by default** | The UI is off unless enabled and adds no unauthenticated endpoint |
| **Retrievable keys** | Only SHA-256 hashes live at rest, and the lifecycle is rotation, not retrieval |
| **Key material in default traces** | Content tracing is opt-in, so no secret or personal data egresses by default |

## What This Stack Does Not Solve

A threat model earns trust by admitting its gaps. These are the parts this design does not fix.

- **In-budget abuse of a stolen key.** The broker enforces limits, not behavior analysis. A valid key works until revoked.
- **Prompt injection of the agent.** The broker never mitigates it. Agent-side controls own LLM01:2025 and LLM06:2025 entirely.
- **DNS rebinding on outbound connections.** The SSRF allow-list is the wall. The time-of-check to time-of-use window is not fully closed in-process.
- **A reached GPU host.** The broker limits its own blast radius. Host segmentation, runtime hardening, and the runtime-identity gate (still on an unmerged branch) are outside shipped broker code.
- **No public ports as an architectural promise.** This holds only while the edge stays the sole entry point.
- **Operator misconfiguration.** Wide grants, loose model roots, or content tracing left on each reopen a surface the code otherwise closes.
- **Compute cost of many small in-budget requests.** Per-key rate limits throttle a caller, they do not make inference free.

## Next Steps

Work the chain end to end. Set keys and budgets with the [broker governance guide](/articles/secure-ai-broker-governance-2026/), lock the edge with the [Tailscale private edge setup](/articles/tailscale-aperture-local-ai-gateway-2026/), and see the full picture in the [brokerized local AI workflow overview](/articles/hermes-agent-local-ai-brokerized-workflow-2026/). For the agent side, where prompt injection lives, read [AI agent trust boundaries](/secure-ai-agents-mcp-course/01-agent-trust-boundaries/). For why the host underneath still matters, see [containers are no longer a security boundary](/articles/containers-no-longer-security-boundary-2026/).
