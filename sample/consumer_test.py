import pika

import os
ip = os.environ["LLM_SVC_QUEUE_SERVER_IP"]
port = os.environ["LLM_SVC_QUEUE_SERVER_PORT"]
path = os.environ["LLM_SVC_QUEUE_SERVER_PATH"]
user = os.environ["LLM_SVC_QUEUE_SERVER_USER"]
passwd = os.environ["LLM_SVC_QUEUE_SERVER_PASSWD"]
credentials = pika.PlainCredentials(user, passwd)
connection = pika.BlockingConnection(
        pika.ConnectionParameters(ip, port, path, credentials)
    )
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("Received len = ", len(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    with open("/tmp/sample.wav", 'wb') as f:
        f.write(body)


# basic_getを使用してメッセージを一度だけ取り出す
method_frame, header_frame, body = channel.basic_get(queue='hello')

if method_frame:
    # メッセージが存在する場合はコールバックを呼び出す
    callback(channel, method_frame, None, body)
else:
    print("No message in the queue")

# 接続を閉じる
connection.close()
