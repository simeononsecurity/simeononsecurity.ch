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
