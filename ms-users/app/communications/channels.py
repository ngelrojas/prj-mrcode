import connections


class ChannelManager:

    def __init__(self):
        self.channels = connections.connection.channel()
        self.queue_name = "mr_code_response"

    def get_channel(self, callback_func):
        self.channels.queue_declare(queue=self.queue_name, durable=True)
        return self.channels.basic_consume(
            queue=self.queue_name,
            on_message_callback=callback_func,
            auto_ack=True,
        )

    def get_start_consuming(self):
        return self.channels.start_consuming()

    def get_declare(self):
        return self.channels.queue_declare(queue=self.queue_name, durable=True)

    def get_basic_publish(self, json_data=None):
        self.channels.basic_publish(
            exchange="", routing_key=self.queue_name, body=json_data
        )
