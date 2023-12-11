#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8002
CERTFILE = "./localhost.pem"


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERTFILE)

class MyHandler(SimpleHTTPRequestHandler):
    #動作確認後に削除予定のメソッド。
    def do_OPTIONS(self):
       self.send_response(200)
       self.send_header('Access-Control-Allow-Origin', '*'); # すべてのオリジンからのアクセスを許可
       self.send_header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE'); # 許可するメソッド
       self.send_header('Access-Control-Allow-Headers', 'Content-Type'); # 許可するヘッダー
       self.end_headers()

Handler = MyHandler

with HTTPServer(("", PORT), Handler) as httpd:
    print("serving at address", httpd.server_address, "using cert file", CERTFILE)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()

