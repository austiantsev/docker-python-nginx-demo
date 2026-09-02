import os
from http.server import BaseHTTPRequestHandler, HTTPServer

MESSAGE = os.getenv("MESSAGE", "Hello from volume 2")
PORT = int(os.getenv("PORT", "8080"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response = f"Release 2 | {MESSAGE}"
        self.wfile.write(response.encode())

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()
