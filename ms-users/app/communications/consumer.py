from channels import ChannelManager


def on_message_received(channel, method, properties, body):
    print(f"Received message: {body.decode()}")


class ConsumerManager:
    def __init__(self):
        self.channels = ChannelManager()

    def start(self):
        self.channels.get_channel(on_message_received)
        self.channels.get_start_consuming()
