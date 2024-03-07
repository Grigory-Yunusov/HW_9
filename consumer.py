# import pika 
# import json
# from connect import connect_to_db
# from models import Contact

# connect_to_db()

# connection_params = pika.ConnectionParameters(host="localhost")
# connecton = pika.BlockingConnection(connection_params)
# chanel = connecton.channel()

# queue_name = "email_queue"
# chanel.queue_declare(queue=queue_name)

# def process_message(ch, method, properties, body):
#     message = json.loads(body)
#     contact_id = message["contact_id"]
#     contact = Contact.objects.get(id=contact_id)

#     print(f"Sending email to {contact.email}...")

#     contact.notified = True
#     contact.save()

#     ch.basic_ack(delivery_tag=method.delivery_tag)

# chanel.basic_consume(queue=queue_name, on_message_callback=process_message)

# print("Consumer is waiting for message. To exit, press Ctrl+C")
# chanel.start_consuming()
