# connection_manager = ConnectionManager("admin", "admin", "rabbitmq", 5672)
# connection = connection_manager.get_connection()

# from connections import ConnectionManager
#
#
# class ConnectionProducer:
#     def __init__(self, username, password, host, port):
#         self.connection_manager = ConnectionManager(username, password, host, port)
#
#     def get_connection(self):
#         return self.connection_manager.get_connection()
import connections

channel = connections.connection.channel()
channel.queue_declare(queue="mr_code_response", durable=True)
