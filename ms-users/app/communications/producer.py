import connections


class ProducerManager:

    def __init__(self):
        self.channel = connections.connection().channel()

    def get_queue_declare(self):
        return self.channel.get_declare()
