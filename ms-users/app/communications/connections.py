import pika

credentials = pika.PlainCredentials(username="admin", password="admin")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="172.24.0.4", port="5672", credentials=credentials)
)
