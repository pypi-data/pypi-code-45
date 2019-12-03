#!/usr/bin/env python

import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler


class HttpsRedirector(SimpleHTTPRequestHandler):
    allow_reuse_address = True

    def do_GET(self):
        self.do_HEAD()

    def do_HEAD(self):
        host = self.headers["host"]
        if ":" in host:
            host = host.split(":", 1)[0]

        url = "https://" + host + self.path
        self.send_response(301)
        self.send_header("Location", url)
        self.end_headers()


def main():
    ap = argparse.ArgumentParser()  # pylint: disable=invalid-name
    ap.add_argument("--bind", default="0.0.0.0")
    ap.add_argument("--http-port", type=int, default=80)
    args = ap.parse_args()

    httpd = HTTPServer((args.bind, args.port), HttpsRedirector)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
