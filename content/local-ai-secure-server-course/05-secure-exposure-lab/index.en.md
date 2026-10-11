---
title: "Lab: Test a Secure Local AI Entry Point"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Run a synthetic loopback model service and gateway, then test authentication, request limits, and listener scope."
genre: ["Artificial Intelligence", "Cybersecurity", "Hands-On Lab"]
tags: ["local AI security lab", "API authentication lab", "loopback server", "LLM gateway test", "secure model API"]
cover: "/img/cover/local-ai-secure-exposure-lab.webp"
coverAlt: "Lab gateway blocking unauthorized access before a synthetic loopback model service"
coverCaption: "Lab cover placeholder. Image generation follows editorial review."
---

[Return to the Local AI Course](/local-ai-secure-server-course/)

**This lab tests the access boundary without a model download.** A synthetic upstream mimics one model route. A loopback gateway requires a fake bearer token and limits request size.

> **Safety boundary:** Both listeners use `127.0.0.1`. Keep the fake token unchanged. Do not bind the lab to a LAN or public address.

## Create the Lab Server

Create a new directory and save this file as **`secure_gateway_lab.py`**:

```python
from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

TOKEN = "FAKE_LOCAL_AI_LAB_TOKEN"
MAX_BODY = 512


def send(handler: BaseHTTPRequestHandler, status: int, body: dict[str, object]) -> None:
    data = json.dumps(body).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


class ModelHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        if self.path != "/api/chat":
            send(self, 404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        self.rfile.read(length)
        send(self, 200, {"message": {"content": "READY"}})

    def log_message(self, format: str, *args: object) -> None:
        return


class GatewayHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        if self.headers.get("Authorization") != f"Bearer {TOKEN}":
            send(self, 401, {"error": "unauthorized"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        if length < 1 or length > MAX_BODY:
            send(self, 413, {"error": "request size rejected"})
            return
        body = self.rfile.read(length)
        request = Request(
            "http://127.0.0.1:18080/api/chat",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=2) as response:
                data = json.loads(response.read())
            send(self, 200, data)
        except HTTPError as error:
            send(self, error.code, {"error": "upstream rejected request"})

    def log_message(self, format: str, *args: object) -> None:
        return


def serve() -> None:
    upstream = ThreadingHTTPServer(("127.0.0.1", 18080), ModelHandler)
    gateway = ThreadingHTTPServer(("127.0.0.1", 18443), GatewayHandler)
    thread = threading.Thread(target=upstream.serve_forever, daemon=True)
    thread.start()
    print("upstream=127.0.0.1:18080 gateway=127.0.0.1:18443")
    gateway.serve_forever()


if __name__ == "__main__":
    serve()
```

Start the lab in one terminal:

```bash
python3 secure_gateway_lab.py
```

Expected result:

```text
upstream=127.0.0.1:18080 gateway=127.0.0.1:18443
```

## Test Authentication

In a second terminal, send a request without a token:

```bash
curl -i http://127.0.0.1:18443/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Return READY"}'
```

Expected result:

```text
HTTP status 401
{"error": "unauthorized"}
```

Send the approved fake token:

```bash
curl -i http://127.0.0.1:18443/api/chat \
  -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"message":"Return READY"}'
```

Expected result:

```text
HTTP status 200
{"message": {"content": "READY"}}
```

## Test Request Limits

```bash
python3 - <<'PY' | curl -i http://127.0.0.1:18443/api/chat \
  -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
  -H 'Content-Type: application/json' \
  --data-binary @-
import json
print(json.dumps({"message": "A" * 600}))
PY
```

Expected result:

```text
HTTP status 413
{"error": "request size rejected"}
```

## Inspect Listeners

On Linux:

```bash
ss -ltnp | grep -E '18080|18443'
```

On macOS:

```bash
lsof -nP -iTCP:18080 -iTCP:18443 -sTCP:LISTEN
```

Both services must show loopback addresses. Stop the server with Ctrl+C after testing.

## Advanced Extension

Replace the synthetic upstream URL with your loopback Ollama or llama.cpp endpoint only after the base tests pass. Keep the runtime bound to loopback. Replace the fixed fake token with your approved identity provider or gateway. Do not store production secrets in the lab script.

Add TLS at the gateway for any remote client path. Repeat unauthorized, authorized, oversized, timeout, and concurrency tests from an approved private client.

## Answer Key

- **No token:** Gateway returns 401 and sends nothing upstream.
- **Correct fake token:** Gateway forwards one bounded request and returns `READY`.
- **Oversized request:** Gateway returns 413 before upstream processing.
- **Listener scope:** Both ports bind to `127.0.0.1`.
- **Security limit:** The fixed token and plain HTTP suit loopback training only. They do not satisfy a remote deployment.

## Expected Result

The gateway rejects a missing token, accepts the approved fake token, rejects an oversized body, and keeps both listeners on loopback.

## Troubleshooting

- **Address already in use:** Stop the conflicting local process or choose two unused high ports and update every reference.
- **The request hangs:** Confirm both listeners started and no local proxy changes loopback traffic.
- **Authorized requests return 401:** Check the header spelling and exact fake token.
- **Oversized requests return 200:** Confirm the body exceeds 512 bytes and reaches the gateway port.
- **A listener shows `0.0.0.0`:** Stop the lab and restore both bind addresses to `127.0.0.1`.

## Verify Completion

Save status codes and listener output in **`local-ai-course-record.md`**. Pass when the three access tests match the answer key, both listeners use loopback, and the process stops cleanly.

Continue with the [Knowledge Check](/local-ai-secure-server-course/06-knowledge-check/).
