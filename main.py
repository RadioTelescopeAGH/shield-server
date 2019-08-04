from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

from config.actions import Actions
from config.config import Config


class Server(BaseHTTPRequestHandler):

    data = {}
    actions = Actions()

    def get_data(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.data = json.loads(post_data)

    def response(self, controller_response=(None, None, None)):
        status, code, data = controller_response

        if code is None:
            code = 500

        self.send_response(code)

        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(bytes(json.dumps({"status": status, "data": data}), "utf-8"))

    def exec_request(self):
        self.get_data()
        self.response(self.actions.exec(self.data.get('controller'), self.data.get('action'), self.data.get('data')))

    def do_GET(self):
        self.exec_request()

    def do_POST(self):
        self.exec_request()


def main():
    server = HTTPServer((Config.hostName, Config.hostPort), Server)
    print(time.asctime(), "Server Starts - %s:%s" % (Config.hostName, Config.hostPort))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (Config.hostName, Config.hostPort))


print("AGH SHIELD TEAM - 2019, All right reserved")
main()
