---
title: "Lesson 4: Design a Secure Local AI Server"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Design network, identity, TLS, rate, logging, update, and recovery controls for a local AI service."
genre: ["Artificial Intelligence", "Cybersecurity", "Self-Hosted"]
tags: ["secure local AI server", "Ollama security", "LLM API authentication", "AI reverse proxy", "private AI server"]
cover: "/img/cover/secure-local-ai-server-design.webp"
coverAlt: "Local AI server behind a private network, authenticated proxy, firewall, and monitoring controls"
coverCaption: "Lesson cover placeholder. Image generation follows editorial review."
---

[Return to the Local AI Course](/local-ai-secure-server-course/)

**Keep the inference runtime on loopback. Put network access behind a separate enforcement point.** This design limits direct reach to model management and native API routes.

## Start with Data Flow

Draw this path for a private service:

```text
approved client -> private network -> authenticated TLS proxy -> loopback model runtime
                                      |-> access log
                                      |-> rate limit
                                      |-> request size limit
```

Record each trust boundary, protocol, identity, owner, and log source. Add outbound paths for model downloads, telemetry, DNS, and updates. A local inference process still interacts with an operating system and supply chain.

## Bind the Runtime

Ollama uses loopback by default. Its [FAQ](https://docs.ollama.com/faq) documents `OLLAMA_HOST` for a different listener. Keep the runtime on `127.0.0.1` unless an approved design needs another boundary.

For llama.cpp, the [server documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) states the default listener is `127.0.0.1:8080`. Set the host explicitly in service configuration:

```bash
llama-server \
  -m /srv/models/approved-model.gguf \
  -c 4096 \
  --host 127.0.0.1 \
  --port 8080
```

Do not enable built-in tools or MCP server integration on an untrusted deployment. Current llama.cpp documentation labels those features experimental and warns against untrusted environments.

## Define the Entry Point

Your proxy or gateway should enforce:

- **Authentication:** One identity per user or workload
- **Authorization:** Named model and route permissions
- **TLS:** Protected client-to-gateway traffic
- **Request limits:** Body size, context, output, and timeout
- **Rate limits:** Per identity and service
- **Concurrency limits:** Values proven by memory tests
- **Network policy:** Private source ranges or device identity
- **Logging:** Identity, route, model, size, decision, duration, and status

Avoid storing full prompts by default. Decide whether incident needs justify bounded samples, encryption, strict access, and short retention.

## Protect the Host

Run the service under a dedicated operating-system account. Limit read access to approved model files and write access to required cache or log paths. Keep shells, package managers, credentials, and unrelated data outside service authority.

Container isolation helps package dependencies. It does not replace host device controls, model provenance, API authentication, or network policy. Rootless operation and read-only mounts reduce impact where the runtime supports them.

## Control Updates

Record four version sets:

1. Runtime and build source
2. Model identifier, license, and digest
3. Driver and accelerator stack
4. Proxy, policy, and service configuration

Test updates with the same prompt, API health check, memory profile, and access-denial tests. Preserve the previous runtime, model, and configuration until rollback passes.

## Beginner and Advanced Targets

**Beginner target:** One user, one model, loopback only, local firewall enabled, no remote access, and a manual update record.

**Advanced target:** Private network path, authenticated TLS proxy, per-user policy, bounded concurrency, external logs, health checks, staged update, and tested rollback.

## Expected Result

Your diagram has no direct public path to the model runtime. Every remote request crosses an authenticated policy point. The native runtime stays on loopback.

## Troubleshooting

- **The runtime listens on all interfaces:** Stop the service, repair its bind setting, then restart and recheck listeners.
- **The proxy authenticates but the native port stays reachable:** Add host firewall rules and bind the runtime to loopback.
- **Requests fail under concurrency:** Return to the measured safe parallel value and add queue limits.
- **Logs contain prompt bodies:** Disable body logging and review stored records for deletion under your policy.
- **Rollback needs a fresh download:** Retain the approved prior artifact or image before rollout.

## Verify the Design

Your review passes when it answers:

1. Which process listens on each address and port?
2. Which identity reaches each route and model?
3. Where do authentication, rate, and size checks run?
4. Which logs prove allowed and denied access?
5. Which artifact and configuration restore the previous version?

Continue with the [Secure Exposure Lab](/local-ai-secure-server-course/05-secure-exposure-lab/).
