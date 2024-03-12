# import pika
#
#
# class ConnectionManager:
#     def __init__(self, username, password, host, port):
#         self.username = username
#         self.password = password
#         self.host = host
#         self.port = port
#
#     def get_connection(self):
#         credentials = pika.PlainCredentials(
#             username=self.username, password=self.password
#         )
#         return pika.BlockingConnection(
#             pika.ConnectionParameters(
#                 host=self.host, port=self.port, credentials=credentials
#             )
#         )
#
#     def get_is_connection(self):
#         if self.get_connection().is_open:
#             print("Connection to RabbitMQ is open")
#             return True
#
#         print("Connection to RabbitMQ is closed")
#         return False
import pika

credentials = pika.PlainCredentials(username="admin", password="admin")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="127.0.0.1", port=5672, credentials=credentials)
)

if connection.is_open:
    print("Connection to RabbitMQ is open")
else:
    print("Connection to RabbitMQ is closed")
