#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic-messages', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'Hola a todos'

channel.basic_publish(
    exchange='topic-messages', routing_key=routing_key, body=message)

print(" [x] Sent %r:%r" % (routing_key, message))

connection.close()
