"""
server.py

- Listen for incoming messages on PORT at ENDPOINT of HTTP server
    - Upon new message, update clipboard
"""
import json
import sys
import pyperclip
from http.server import BaseHTTPRequestHandler, HTTPServer
from constants import PORT, KEY


class ClipHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_success()
    
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            response = json.loads(body)
        except (KeyError, ValueError):
            return self.send_error(400, "Unable to parse request")

        try:
            clip = response[KEY]
        except KeyError:
            return self.send_error(400, "Missing clipboard argument")

        print("Received: ", clip)
        print("----------------")

        try:
            pyperclip.copy(clip)
        except pyperclip.PyperclipException:
            return self.send_error(500, "Unable to copy text to clipboard")

        self.send_success()

    def log_message(self, format, *args):
        # turn off logging
        return

    def send_success(self):
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])

    print(f"Running Server on port {PORT}")

    server = HTTPServer(('', PORT), ClipHandler)
    server.serve_forever()
