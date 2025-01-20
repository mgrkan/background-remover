#!/usr/bin/env python
import pika, sys, os
import remover
from models import RembgModel

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello', durable=True)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        try:
            remover.process_image(body, 'output.png', RembgModel())
            print(" [x] Done")
            ch.basic_ack(delivery_tag = method.delivery_tag)
        except Exception as e:
            print(f" [x] Error: {e}")
            ch.basic_reject(delivery_tag = method.delivery_tag, requeue=False)

    channel.basic_consume(queue='hello', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)