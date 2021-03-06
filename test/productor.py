#!/usr/bin/env python
import pika
import sys

#Las credenciales para conectarnos al servidor RabbitMQ
#credentials = pika.PlainCredentials('root','password')

#Conexion con nuestro servidor RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='broadcast', exchange_type='fanout')

message = "Hello Everyone!!"
channel.basic_publish(exchange='broadcast', routing_key='general', body=message)
print(" [x] Sent %r" % message)
connection.close()