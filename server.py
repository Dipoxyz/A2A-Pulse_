from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json

API = "https://api.a2a.family"

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] in ("/api/feed", "/api/stats"):
            endpoint = self.path.split("?")[0].removeprefix("/api")
            try:
                req = Request(
                    API + endpoint,
                    headers={"User-Agent": "A2A-Pulse/1.0",
                             "Accept": "application/json"}
                )
                with urlopen(req, timeout=15) as response:
                    body = response.read()
                    self.send_response(response.status)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Cache-Control", "no-store")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
            except HTTPError as e:
                self.send_error(e.code, "A2A API returned an HTTP error")
            except (URLError, TimeoutError, OSError) as e:
                self.send_error(502, "Could not reach A2A API: " + str(e))
            return
        if self.path == "/":
            self.path = "/index.html"
        super().do_GET()

print("A2A Pulse running on port 8000")
port = int(os.environ.get("PORT", "8000"))
ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
