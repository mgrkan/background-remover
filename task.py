#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='image_queue', durable=True)

channel.basic_publish(exchange='',
                      routing_key='image_queue',
                      body='sample1.jpeg',
                      properties=pika.BasicProperties(
                         delivery_mode = pika.DeliveryMode.Persistent, # make message persistent
                      ))
print(" [x] Sent 'sample1.jpeg'")

connection.close()