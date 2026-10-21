---
title: "Tailscale Aperture: The Private Gateway to Your Local AI"
date: 2026-10-21
lastmod: 2026-10-21
toc: true
draft: false
description: "Reach your local AI broker and cloud models from every device with zero public ports, tailnet identity, deny-by-default grants, and one URL using Tailscale Aperture."
genre: ["AI", "Network Security", "Self-Hosted", "Zero Trust", "Local AI", "Tailscale", "API Gateway", "Remote Access", "Identity", "Private Networking"]
tags: ["tailscale aperture", "aperture ai gateway", "private ai gateway", "local ai broker", "zero trust ai", "tailnet identity", "openai compatible gateway", "self-hosted ai access", "aperture grants", "deny by default ai", "wireguard ai gateway", "no public ports", "identity aware ai access", "aperture configuration", "aperture troubleshooting", "local llm remote access", "hermes agent", "ai broker gateway", "aperture self-hosted provider", "aperture passthrough", "tailscale ai", "magicdns ai gateway", "per identity model access", "aperture cloud provider", "private llm endpoint"]
cover: "/img/cover/tailscale-aperture-local-ai-gateway-2026.webp"
coverAlt: "An illustration of a private network gateway routing AI requests from laptops and phones to a local GPU server and a cloud model on a dark background."
coverCaption: ""
---

## Introduction

**Tailscale Aperture** is a reverse-proxy AI gateway. Every request to a model passes through it, and it reaches your local AI broker and your cloud models over your private tailnet with **no public ports open to the internet**. One URL fronts both your self-hosted models and a paid cloud provider, and each caller sees only the models their identity is allowed to use.

This guide answers one question: how do you reach your broker and cloud models from every device with **zero public exposure, identity-aware access, and a single base URL**? You will set up the gateway, front your broker and one cloud provider, write deny-by-default access rules, point clients at the gateway, and decide whether Aperture should sit in front of your broker or in front of each backend.

*Aperture is under active development. Tailscale has not published a GA or stability badge for it as of October 2026. Treat every configuration key below as current to the September and October 2026 Aperture documentation and re-check it before a production rollout.*

## Key Takeaways

- **Aperture is the private edge.** It listens on your tailnet, so there are **no public ports** and no reverse proxy to harden on the open internet.
- **Identity comes from the tailnet, not the client.** Aperture asks Tailscale who the caller is by their IP, so a client cannot forge its own identity.
- **Access is deny-by-default.** Network reachability grants no model access on its own. A matching grant per identity is what opens a model.
- **Clients need a base URL and a model name.** The provider key lives server-side, so most on-tailnet clients send no real credential.
- **One gateway fronts many upstreams.** Put your broker behind Aperture for local models and add a cloud provider in the same config.

## Before You Begin

You need the following in place:

- A **Tailscale tailnet** with **MagicDNS enabled** and your devices joined. If tailnets, identity, and MagicDNS are new to you, read the [Tailscale vs Headscale comparison](/articles/tailscale-vs-headscale-comparison-guide/) first.
- An **OpenAI-compatible AI broker** already serving your local models on the tailnet. The sibling guide [one endpoint for every model](/articles/openai-compatible-ai-broker-one-endpoint-2026/) covers the broker itself.
- A **GPU host** reachable from the device running the gateway, at a tailnet address shown here as `<GPU_HOST>`.
- An Aperture account from `aperture.tailscale.com`. The free personal plan is enough to follow along.

**Estimated time:** 30 to 45 minutes. **Difficulty:** intermediate. You should be comfortable editing HuJSON config and reading Tailscale access rules.

## What Aperture Does

**Aperture** is a centralized gateway for large language model traffic. It accepts OpenAI-wire requests, works out which upstream provider owns the requested model, injects the provider credential on the server side, forwards the request, and records who made it.

Three properties make it the right fit for a private local-AI setup:

- **Tailnet-native identity.** Aperture queries Tailscale with the caller's IP and receives the login, device, and tags bound to the source address. Identity is a property of the network, not a header the client sets.
- **Model-name routing.** Aperture reads the model name from the request body and routes to the matching upstream. Adding a provider needs no change on the client.
- **Server-side credentials.** The provider API key stays in the gateway config. Clients on the tailnet send a base URL and a model name, and nothing more in the common case.

> **Key Takeaway:** Aperture turns "reach my models securely from anywhere" into "join the tailnet and ask for a model by name."

## The Private Edge, Not the Public Edge

This series treats Aperture as the **private edge**: the entry point for your own devices and trusted identities over the tailnet. A **public edge** for anonymous internet traffic is a separate concern and out of scope here, where the usual pick is a public-facing proxy such as LiteLLM. The rest of this guide stays on the private path.

The layering for the series is fixed:

```text
Agents  ->  Aperture (private edge)  ->  OpenAI-compatible broker  ->  backends
```

Every hop after Aperture lives on the tailnet, and the first hop from a client to Aperture rides Tailscale's WireGuard transport. For the relay and direct-connection mechanics behind the first hop, see [why Tailscale uses a relay](/articles/why-tailscale-uses-a-relay/).

## How Identity Works

When a request arrives, Aperture takes the source Tailscale IP and performs a `WhoIs` lookup against your tailnet. The answer is the authenticated login or the device tags bound to the source address. The client never asserts its own identity, so a forged header buys nothing.

Two identity shapes matter:

- **User identity** attributes each session to a real login and device. This is what you want for per-person access and audit.
- **Tag identity** collapses every session behind a service tag into one synthetic login. Reserve tags for CI and shared service hosts, not for people, because per-user attribution disappears under a tag.

*Tag-based identity is the common pitfall: a shared CI host tagged once will log every run as the same caller.*

## Who Reaches What

The table below shows the access model you will build in the next sections. **Network reachability alone grants nothing.** Each row depends on a matching grant.

| Identity | Local broker models | Cloud models | What permits it |
|----------|--------------------|--------------|-----------------|
| **`group:ai-users`** | Yes | Yes | A grant listing `broker/**` and `openai/**` |
| **`tag:ci`** | Yes | No | A grant listing `broker/**` only |
| **On-tailnet device, no grant** | No | No | Deny-by-default, no matching grant |
| **Off-tailnet device** | Via bridge only | Via bridge only | Aperture CLI bridge or `ts-unplug`, beta |

*Grants are additive and allow-only. You remove access by removing or narrowing a grant, never by writing a deny rule.*

## Set Up the Gateway

Each step is marked for how it was checked. **Verified against docs** means confirmed against the Tailscale Aperture documentation dated September and October 2026. **Not tested here** means the step was not independently run in a lab for this guide.

**Step 1. Sign up and install the gateway.** Create an Aperture account at `aperture.tailscale.com` and bring up the gateway node on a host already joined to your tailnet. *(Verified against docs.)*

**Step 2. Confirm MagicDNS reachability.** From another tailnet device, open `http://<APERTURE_HOST>` in a browser. A response confirms the gateway is reachable by name. A "cannot connect using hostname" error means MagicDNS is disabled or the URL is wrong. *(Verified against docs.)*

**Step 3. Narrow the default grants.** A new gateway ships with wide-open "all users, all models" grants. Narrowing these is the step enforcing per-identity access. *(Verified against docs.)*

> **Warning: a fresh Aperture gateway is open to every tailnet identity until you narrow the shipped grants.** Do this before you add a paid cloud provider.

## Front the Broker and a Cloud Model

Open **Administration > Configuration** and add your upstreams. The config is HuJSON. Merge this provider fragment into the existing config instead of replacing it.

```jsonc
{
  "providers": {
    // (a) The OpenAI-compatible BROKER as a self-hosted-style upstream.
    //     baseurl = broker root WITHOUT a trailing /v1 (Aperture appends the path).
    //     Omit apikey if the broker is keyless on the tailnet.
    "broker": {
      "baseurl": "http://<GPU_HOST>:<BROKER_PORT>",
      "models": ["gpt-oss-20b", "qwen3-coder:30b", "<local-model-id>"]
    },

    // (b) One CLOUD provider fronted by the SAME gateway.
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey":  "<cloud-provider-key>",
      "models":  ["<cloud-model-id>", "<cloud-model-mini-id>"],
      "compatibility": { "openai_chat": true, "openai_responses": true }
    }
  }
}
```

Two settings decide whether the first request works:

- **Strip the trailing `/v1` from every `baseurl`.** Aperture appends the full incoming path. A leftover `/v1` produces a doubled path and an HTTP 405. *(Verified against docs.)*
- **Omit `apikey` for a keyless broker.** The local broker needs no credential from the gateway. Add a key only when the broker itself requires one. *(Verified against docs.)*

Test each upstream from **Administration > Models** with the play control before you expose it to clients. *(Not tested here.)*

## Grants: Deny by Default

Grants are the authorization layer. Each grant maps a source identity to a capability over a model glob. Add these to the Aperture config alongside the providers.

```jsonc
{
  "grants": [
    {
      // Engineers reach BOTH the broker's local models and the cloud models.
      "src": ["group:ai-users"],
      "app": { "tailscale.com/cap/aperture": [
        { "role": "user" },
        { "models": "broker/**" },
        { "models": "openai/**" }
      ]}
    },
    {
      // A CI identity reaches ONLY the local broker models, never the paid cloud upstream.
      "src": ["tag:ci"],
      "app": { "tailscale.com/cap/aperture": [
        { "role": "user" },
        { "models": "broker/**" }
      ]}
    }
  ]
}
```

A few rules keep the grant layer correct:

- **The `models` field is a single glob over `provider/model`.** The most specific glob wins, so one grant entry is needed per provider a caller reaches.
- **Using `group:` in `src` needs the `tailscale.com/visible-groups` node attribute** on the gateway device.
- **Grants live in the Aperture config or in the tailnet policy file.** In the policy file the `dst` field is required and targets the Aperture node, and you also need a network grant opening the gateway port, for example `ip: ["tcp:80"]`.

*For managing access as code in your policy file, mirror the same source-to-model mapping and add the network grant.*

## Connect Your Clients

On the tailnet, a client needs a **base URL and a model name**. The provider credential is already server-side. The matrix below shows the common clients.

| Client | Base URL | Auth on tailnet | Model field |
|--------|----------|-----------------|-------------|
| **Agent plugin, OpenAI wire** | `http://<APERTURE_HOST>/v1` | Placeholder key for the SDK check | A granted id, for example `gpt-oss-20b` |
| **Agent plugin, Anthropic wire** | `http://<APERTURE_HOST>/v1` | Real subscription token, passthrough | A granted id |
| **OpenAI SDK, Python or Node** | `http://<APERTURE_HOST>/v1` | `api_key="placeholder"`, non-empty | Any granted id from `/v1/models` |
| **curl, chat completions** | `http://<APERTURE_HOST>/v1/chat/completions` | None needed on tailnet | `"model": "<granted-id>"` |
| **curl, list models** | `http://<APERTURE_HOST>/v1/models` | None needed on tailnet | Returns only granted models |

Listing models from an on-tailnet shell shows the deny-by-default model in action:

```bash
curl http://<APERTURE_HOST>/v1/models
```

The response lists **only the models the caller's identity is granted**. Each entry carries the bare model name as its `id` and names the upstream in `metadata.provider.id`. To force a specific upstream, send the prefixed `provider/model` id.

> **Note:** Some clients require a non-empty API key field even when the upstream is keyless. A placeholder string satisfies the SDK check. The real credential never leaves the gateway.

A caveat on transport: plain `http://` over the tailnet works for OpenAI-wire SDKs, curl, and agent plugins. A few clients, Claude Desktop and Gemini CLI version 0.40 and later, require **HTTPS with a trusted certificate for a fully qualified gateway hostname**. Check your client before you assume plain `http://` is enough. *(Verified against docs.)*

## One Gateway, Broker or Backends?

With the gateway working, the design question is whether Aperture's upstream should be **your broker** (Agents to Aperture to broker to backends) or whether Aperture should **front each backend directly** (Agents to Aperture to the GPU host and the cloud). The Aperture docs support both shapes, so this is a judgment call.

| Dimension | Aperture to broker to backends | Aperture to each backend directly |
|-----------|-------------------------------|-----------------------------------|
| **Routing logic** | Broker owns retries, failover, load balancing, and model aliasing | Aperture routes by model name only, no cross-backend failover |
| **Model catalog** | One place, the broker, to add and alias models | Every backend declared in Aperture config, list churns as backends change |
| **Identity and audit** | Sharp at Aperture, coarsens at the broker boundary | Native per-user attribution per backend at the edge |
| **Failure surface** | Two hops to reason about | One hop, simpler to debug |
| **Series fit** | Matches the fixed layering | Collapses the broker out of the series |

**Recommendation:** make **Aperture's upstream the broker**. It matches the series layering, keeps all reliability and model-sizing logic in the broker you already maintain, and gives one URL fronting both local and cloud models. Accept one real cost: per-user audit is sharp at Aperture but coarsens where traffic enters the broker, because Aperture logs who hit the gateway while the broker logs what it dispatched. If finer backend attribution is ever needed, have Aperture carry the identity into the broker through a forwarded header.

*Direct-fronting wins in one case: a single backend with no broker value-add, where per-user cost attribution on the backend itself matters. The two are not exclusive. Aperture fronts the broker for your local fleet and a cloud provider directly in the same config.*

For the threat model behind these choices, see [the local AI broker threat model](/articles/local-ai-broker-threat-model-2026/). For wiring coding agents into this setup, see [local models in Claude Code, Cursor, and OpenCode](/articles/local-models-claude-code-cursor-opencode-2026/).

## Devices Outside the Tailnet

Aperture listens on Tailscale interfaces, so a device off the tailnet fails at the network level. To reach the gateway from such a device, use an **Aperture CLI bridge** or **`ts-unplug`**, an embedded tailnet node. The client then points at `http://localhost:<port>` and keeps its own Tailscale identity.

> **Warning: `ts-unplug` and `ts-plug` are under active development.** They build from source, have no prebuilt binaries, and bind to `localhost` only. Treat off-tailnet access as a beta path and verify it in a test environment before relying on it.

The simpler answer for most readers is to join the device to the tailnet. For hardening the entry point itself, the course lab on [secure exposure](/local-ai-secure-server-course/05-secure-exposure-lab/) covers authentication, request limits, and listener scope.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| **"Cannot connect using hostname"** | MagicDNS disabled or wrong URL | Enable MagicDNS, open `http://<APERTURE_HOST>` to confirm reachability |
| **HTTP 403, or a model missing from `/v1/models`** | No matching grant for the caller, deny-by-default | Add a grant whose `src` matches the identity and whose `models` glob covers the model |
| **All sessions show one user** | Tag identity instead of per-user | Connect from each user's own device, reserve tags for service accounts |
| **HTTP 502 or upstream errors** | Broker or backend unreachable from the gateway, or wrong `baseurl` | Confirm the upstream is reachable from the gateway, test from Administration > Models |
| **HTTP 405** | Doubled `/v1`, the `baseurl` kept a trailing `/v1` | Strip the trailing `/v1` from `baseurl` |
| **HTTP 404 on `/v1/responses` or `/v1/messages`** | Provider missing the matching compatibility flag | Set `openai_responses` or `anthropic_messages` in the provider block |
| **Client will not connect over `http://`** | Client requires HTTPS plus a trusted cert for an FQDN | Use the HTTPS hostname the client needs, plain `http://` stays for OpenAI-wire SDKs and curl |
| **Connection fails from a non-tailnet device** | Aperture binds to Tailscale interfaces only | Use an Aperture CLI bridge or `ts-unplug`, point the client at `http://localhost:<port>` |

## Next Steps

You now have a private gateway fronting your broker and a cloud model, with deny-by-default access keyed to tailnet identity and one base URL for every client.

- Read the series master, [the Hermes Agent local AI brokerized workflow](/articles/hermes-agent-local-ai-brokerized-workflow-2026/), for how the private edge fits the full stack.
- Front your models first with the [OpenAI-compatible broker guide](/articles/openai-compatible-ai-broker-one-endpoint-2026/).
- Review [the local AI broker threat model](/articles/local-ai-broker-threat-model-2026/) before widening access.
- Point your coding agents at the gateway with [local models in Claude Code, Cursor, and OpenCode](/articles/local-models-claude-code-cursor-opencode-2026/).
