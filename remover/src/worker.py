#!/usr/bin/env python
import pika, sys, os
import remover
from models import RembgModel
from upload import upload_file

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='image_queue', durable=True)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        try:
            remover.process_image("/app/src/" + body.decode("utf-8"), '/app/images/output.png', RembgModel())
            upload_file('/app/images/output.png', 'output.png')
            print(" [x] Done")
            ch.basic_ack(delivery_tag = method.delivery_tag)
        except Exception as e:
            print(f" [x] Error: {e}")
            ch.basic_reject(delivery_tag = method.delivery_tag, requeue=False)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='image_queue', on_message_callback=callback)

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