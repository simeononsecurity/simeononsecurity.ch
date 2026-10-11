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

[Return to the Local AI Course](/local-ai-secure-server-course-start/)

**This lab tests the access boundary without a model download.** A synthetic upstream mimics one model route. A loopback gateway requires a fake bearer token and limits request size.

Run the Bash commands on Linux or macOS. On Windows, use the WSL 2 environment specified in the course prerequisites and start both the lab server and test commands there.

> **Safety boundary:** Both listeners use `127.0.0.1`. Keep the fake token unchanged. Do not bind the lab to a LAN or public address.

## Create the Lab Server

Create a new directory and save this file as **`secure_gateway_lab.py`**:

```python
from __future__ import annotations

import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

TOKEN = "FAKE_LOCAL_AI_LAB_TOKEN"
MAX_BODY = 512
MAX_RESPONSE = 1024
RATE_WINDOW_SECONDS = 60
RATE_MAX = 5
RATE_TIMES: list[float] = []
RATE_LOCK = threading.Lock()


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
        body = self.rfile.read(length)
        if json.loads(body).get("message") == "OVERSIZED_RESPONSE_TEST":
            send(self, 200, {"message": {"content": "X" * 1200}})
            return
        send(self, 200, {"message": {"content": "READY"}})

    def log_message(self, format: str, *args: object) -> None:
        return


class GatewayHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        if self.path != "/api/chat":
            send(self, 404, {"error": "not found"})
            return
        if self.headers.get("Authorization") != f"Bearer {TOKEN}":
            send(self, 401, {"error": "unauthorized"})
            return
        if not self.headers.get("Content-Type", "").lower().startswith("application/json"):
            send(self, 415, {"error": "JSON required"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            send(self, 400, {"error": "invalid length"})
            return
        if length < 1 or length > MAX_BODY:
            send(self, 413, {"error": "request size rejected"})
            return
        body = self.rfile.read(length)
        try:
            payload = json.loads(body)
        except (UnicodeDecodeError, json.JSONDecodeError):
            send(self, 400, {"error": "invalid JSON"})
            return
        if not isinstance(payload, dict) or not isinstance(payload.get("message"), str):
            send(self, 400, {"error": "message string required"})
            return
        with RATE_LOCK:
            now = time.monotonic()
            RATE_TIMES[:] = [value for value in RATE_TIMES if now - value < RATE_WINDOW_SECONDS]
            if len(RATE_TIMES) >= RATE_MAX:
                send(self, 429, {"error": "rate limit reached"})
                return
            RATE_TIMES.append(now)
        request = Request(
            "http://127.0.0.1:18080/api/chat",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=2) as response:
                raw = response.read(MAX_RESPONSE + 1)
            if len(raw) > MAX_RESPONSE:
                send(self, 502, {"error": "upstream response too large"})
                return
            data = json.loads(raw)
            send(self, 200, data)
        except HTTPError as error:
            send(self, error.code, {"error": "upstream rejected request"})
        except (URLError, TimeoutError):
            send(self, 502, {"error": "upstream unavailable"})
        except (UnicodeDecodeError, json.JSONDecodeError):
            send(self, 502, {"error": "invalid upstream JSON"})

    def log_message(self, format: str, *args: object) -> None:
        return


def serve() -> None:
    upstream = ThreadingHTTPServer(("127.0.0.1", 18080), ModelHandler)
    gateway = ThreadingHTTPServer(("127.0.0.1", 18443), GatewayHandler)
    thread = threading.Thread(target=upstream.serve_forever, daemon=True)
    thread.start()
    print("upstream=127.0.0.1:18080 gateway=127.0.0.1:18443")
    try:
        gateway.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        gateway.server_close()
        upstream.shutdown()
        upstream.server_close()
        print("lab stopped")


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

Verify that an authenticated request to another path never reaches the model route:

```bash
curl -i http://127.0.0.1:18443/admin/delete \
  -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"message":"Return READY"}'
```

Expected result: HTTP status 404 with `{"error": "not found"}`.

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

Test the upstream response limit:

```bash
curl -i http://127.0.0.1:18443/api/chat \
  -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"message":"OVERSIZED_RESPONSE_TEST"}'
```

Expected result: HTTP status 502 with `{"error": "upstream response too large"}`. The gateway reads at most 1,025 bytes from the upstream response.

Restart the lab server to clear its training counter. Send six valid requests inside one minute:

```bash
for n in 1 2 3 4 5 6; do
  curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:18443/api/chat \
    -H 'Authorization: Bearer FAKE_LOCAL_AI_LAB_TOKEN' \
    -H 'Content-Type: application/json' \
    -d '{"message":"Return READY"}'
done
```

Expected statuses are five `200` values, then `429`. This global in-memory counter is only a lab control. A shared service needs a gateway limit keyed to an authenticated identity and a defined window.

## Inspect Listeners

On Linux:

```bash
ss -ltnp | grep -E '18080|18443'
```

On macOS:

```bash
lsof -nP -iTCP:18080 -iTCP:18443 -sTCP:LISTEN
```

Both services must show loopback addresses. Stop the server with Ctrl+C after testing. Expect `lab stopped` and confirm both ports close.

## Advanced Extension

Adapt the gateway to your loopback Ollama or llama.cpp endpoint only after the base tests pass. The synthetic `{"message":"..."}` body is not a drop-in request for either runtime. Validate and translate the request to the selected runtime's model and messages fields, then validate its response before returning it to the client. Keep the runtime bound to loopback. Replace the fixed fake token with your approved identity provider or gateway. Do not store production secrets in the lab script.

Add TLS at the gateway for any remote client path. Repeat unauthorized, authorized, oversized, timeout, and concurrency tests from an approved private client.

## Answer Key

- **No token:** Gateway returns 401 and sends nothing upstream.
- **Correct fake token:** Gateway forwards one bounded request and returns `READY`.
- **Wrong path:** Gateway returns 404 without forwarding the request.
- **Oversized request:** Gateway returns 413 before upstream processing.
- **Oversized upstream response:** Gateway returns 502 before returning model content.
- **Sixth rapid valid request:** Gateway returns 429 until the one-minute window expires or the server restarts.
- **Listener scope:** Both ports bind to `127.0.0.1`.
- **Security limit:** The fixed token and plain HTTP suit loopback training only. They do not satisfy a remote deployment.

## Expected Result

The gateway rejects a missing token, accepts the approved fake token on `/api/chat`, rejects another path, an oversized body, an oversized upstream response, and a sixth rapid valid request. Both listeners stay on loopback.

## Troubleshooting

- **Address already in use:** Stop the conflicting local process or choose two unused high ports and update every reference.
- **The request hangs:** Confirm both listeners started and no local proxy changes loopback traffic.
- **Authorized requests return 401:** Check the header spelling and exact fake token.
- **Oversized requests return 200:** Confirm the body exceeds 512 bytes and reaches the gateway port.
- **A listener shows `0.0.0.0`:** Stop the lab and restore both bind addresses to `127.0.0.1`.

## Verify Completion

Save status codes and listener output in **`local-ai-course-record.md`**. Pass when all six access tests match the answer key, both listeners use loopback, and both ports close after Ctrl+C.

Continue with the [Knowledge Check](/local-ai-secure-server-course/06-knowledge-check/).
