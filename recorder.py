#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pika
import ssl
import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler
# settting of import messaging
sys.path.append("messaging")
from messaging import *

CERTFILE = "./localhost.pem"
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERTFILE)


def queue_message(data):
    rec = RawAudioRecord(data)
    RecoderServiceMessaging().connect_and_basic_publish_record(rec)


class MyHandler(CGIHTTPRequestHandler):
    def do_PUT(self):
        try:
            # PUTリクエストの対象のパスを取得
            path = "./" + self.path

            # PUTデータのサイズを取得
            content_length = int(self.headers['Content-Length'])

            print("受信データを読み込みます. content_length=", content_length)

            # ここでパスとデータを処理できます
            # 例: パスに基づいてファイルにデータを書き込む
            chunks = bytes()
            with open(path, 'wb') as f:
                # データを少しずつ読み取り、ファイルに書き込む
                while content_length > 0:
                    # 最大1024バイトずつ読み取る
                    chunk = self.rfile.read(min(1024, content_length))
                    if not chunk:
                        print("not chunk")
                        break
                    print("受信データtype = ", type(chunk))
                    print("受信データlen = ", len(chunk))
                    f.write(chunk)
                    chunks += chunk
                    content_length -= len(chunk)

            # 応答を返す
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'PUT req ok')
            queue_message(chunks)
        except BrokenPipeError:
            print("クライアントが接続を閉じました")

    def do_OPTIONS(self):
        self.send_response(204)
        # すべてのオリジンからのアクセスを許可
        self.send_header('Access-Control-Allow-Origin', '*')
        # 許可するメソッド
        self.send_header('Access-Control-Allow-Methods', '*')
        # 許可するヘッダー
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()


if __name__ == '__main__':
    server_address = ('', 8001)
    httpd = HTTPServer(server_address, MyHandler)
    print('サーバーがポート8001で実行中...')
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()
