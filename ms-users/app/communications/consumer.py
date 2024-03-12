import channels


def on_message_received(channel, method, properties, body):
    print(f"Received message: {body.decode()}")


channels.channel.basic_consume(
    queue="mr_code_response", on_message_callback=on_message_received
)
channels.channel.start_consuming()

# class MessageConsumer:
#     def __init__(self):
#         self.channel = channel
#
#     def on_message_received(self, channel_, method, properties, body):
#         print(f"received message: {body.decode()}")
#
#     def start(self):
#         self.channel.basic_consume(
#             queue="mr_code_response",
#             on_message_callback=self.on_message_received,
#             auto_ack=True,
#         )
#         self.channel.start_consuming()
