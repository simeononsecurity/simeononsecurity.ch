---
title: "Lesson 2: Run Your First Local Model"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Install a local runtime, pull a selected model, run a prompt, and verify the loopback API."
genre: ["Artificial Intelligence", "Self-Hosted", "Tutorial"]
tags: ["Ollama tutorial", "run local LLM", "local AI API", "first local model", "Ollama CLI"]
cover: "/img/cover/run-first-local-ai-model.webp"
coverAlt: "Terminal session pulling a local model and sending a prompt through a loopback API"
coverCaption: ""
---

[Return to the Local AI Course](/local-ai-secure-server-course-start/)

**Prove local inference on one machine before adding remote access.** This lesson uses Ollama for the beginner path and offers a llama.cpp route for advanced users.

## Install the Runtime

Follow the current [Ollama installation documentation](https://docs.ollama.com/quickstart) for your operating system. Record the installer source and installed version.

For the Windows course path, install and run Ollama inside the same WSL 2 distribution used for the Bash lessons. Keep the service, `curl` calls, and listener checks in that environment so `127.0.0.1` names the same host boundary.

```bash
ollama --version
```

On Linux, check the service:

```bash
systemctl status ollama --no-pager
```

Keep the default loopback listener. The [Ollama FAQ](https://docs.ollama.com/faq) states the server binds to `127.0.0.1:11434` by default. Do not change `OLLAMA_HOST` during this lesson.

## Pull and Inspect the Model

Set the exact identifier selected in Lesson 1:

```bash
MODEL_NAME='replace-with-your-model'
ollama pull "$MODEL_NAME"
ollama show "$MODEL_NAME"
ollama ls
```

Record the identifier, reported size, runtime version, and pull date. If the registry supplies a changing tag, preserve enough output to identify the artifact used in your tests.

## Run a CLI Prompt

```bash
ollama run "$MODEL_NAME" 'List three checks for a backup restore test. Use fewer than 80 words.'
```

Review the answer for three properties:

- **Format:** Three items and fewer than 80 words
- **Relevance:** Each item concerns restore verification
- **Safety:** No invented claim about an observed backup

Repeat the prompt once. Local inference does not guarantee identical output. Record material differences.

## Test the Loopback API

```bash
curl http://127.0.0.1:11434/api/chat \
  -H 'Content-Type: application/json' \
  -d "{\"model\":\"$MODEL_NAME\",\"messages\":[{\"role\":\"user\",\"content\":\"Return the word READY and no other text.\"}],\"stream\":false}"
```

Expected result:

```text
A JSON response with the assistant content under message.content
```

Inspect the listener.

On Linux:

```bash
ss -ltnp | grep 11434
```

On macOS:

```bash
lsof -nP -iTCP:11434 -sTCP:LISTEN
```

On Windows PowerShell:

```powershell
Get-NetTCPConnection -LocalPort 11434 -State Listen
```

Pass when the local address is loopback. A listener on `0.0.0.0`, `::`, or a LAN address needs immediate review.

## Advanced llama.cpp Path

The official [llama.cpp build guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md) covers current platform options. Build the CLI and server from a trusted checkout, then record the commit or release.

```bash
cmake -B build
cmake --build build --config Release
./build/bin/llama-cli -m /path/to/model.gguf -c 4096 -p 'Return the word READY and no other text.'
```

For GPU offload, use a build matching your accelerator and confirm startup diagnostics. Do not assume a requested offload succeeded.

## Expected Result

You have one local model, one CLI response, one loopback API response, and one listener check. Your record separates expected output from the response observed on your host.

## Troubleshooting

- **Connection refused:** Start the runtime, inspect service logs, and confirm the port.
- **Model not found:** Compare the identifier in `ollama ls` with the request.
- **Out of memory:** Stop other model processes, choose a smaller model, or reduce context.
- **CPU use stays high with an expected GPU:** Run `ollama ps` and inspect the `PROCESSOR` column.
- **The API returns streamed lines:** Set `stream` to `false` in the JSON request.

## Verify Completion

```bash
ollama ps
curl -s http://127.0.0.1:11434/api/tags
```

Pass when the model appears in local inventory, the API responds through loopback, and your course record contains the exact runtime and model identifiers.

Continue with [Lesson 3: Measure and Tune Inference](/local-ai-secure-server-course/03-measure-tune/).
