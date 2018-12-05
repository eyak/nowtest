from http.server import BaseHTTPRequestHandler
import socketserver

PORT = 8080

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write((str("Hello from Python on Now 2.0!")+ str(self.path)).encode())
        return
    