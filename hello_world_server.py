"""Serve the built PyPO web app on the local machine."""

import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

import PyPO as pypo


ROOT_DIR = Path(__file__).resolve().parent
BUILD_DIR = ROOT_DIR / "web" / "dist"


class PyPOWebHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BUILD_DIR), **kwargs)

    def do_GET(self):
        if urlsplit(self.path).path == "/api/pypo-version":
            content = json.dumps({"version": pypo.__version__}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        if not (BUILD_DIR / "index.html").is_file():
            self.send_error(
                503,
                "Svelte app not built. Run `npm --prefix web run build` first.",
            )
            return

        super().do_GET()


if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    if not (BUILD_DIR / "index.html").is_file():
        print("Svelte build not found; run `npm --prefix web run build` to serve the app.")
    with ThreadingHTTPServer(address, PyPOWebHandler) as server:
        print(f"PyPO web app: http://{address[0]}:{address[1]}")
        print("Press Ctrl+C to stop the server.")
        server.serve_forever()
