"""
server.py

- Listen for incoming messages on PORT at ENDPOINT of HTTP server
    - Upon new message, update clipboard
"""
import json
import sys
import pyperclip
import tornado.web
import tornado.ioloop
from socket import error as socket_error
from constants import PORT, ENDPOINT, KEY


class ClipHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Cache-control", "no-cache")

        try:
            response = json.loads(self.request.body)
        except ValueError:
            return self.error(400, "Unable to parse request")

        try:
            clip = response[KEY]
        except KeyError:
            return self.error(400, "Missing clipboard argument")

        print("Received: ", clip)
        print("----------------")

        try:
            pyperclip.copy(clip)
        except Exception:
            return self.error(500, "Unable to copy text to clipboard")

        self.set_status(200)

    def error(self, status, message):
        self.clear()
        self.set_status(status)
        self.write(json.dumps({
            'status': status,
            'error': message,
        }))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        PORT = sys.argv[1]

    application = tornado.web.Application([
        (ENDPOINT, ClipHandler),
    ])

    try:
        application.listen(PORT)
    except socket_error:
        print(f"Unable to listen on port {PORT}")

    print(f"Running Server on port {PORT}")
    tornado.ioloop.IOLoop.instance().start()
