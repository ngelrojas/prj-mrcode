import connections


channel = connections.connection.channel()
channel.queue_declare(queue="mr_code_response", durable=True)
