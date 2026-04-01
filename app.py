from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Docker Michael CICD Pipeline corrected!")

PORT = 5000
server = HTTPServer(("", PORT), handler)

print("Server running on port", PORT)
server.serve_forever()