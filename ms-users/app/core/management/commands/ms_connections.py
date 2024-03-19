from django.core.management.base import BaseCommand
from communications.connections import monitor_connection, connection


class Command(BaseCommand):
    help = "monitor rabbitmq connection"

    def handle(self, *args, **options):
        self.stdout.write("Staring RabbitMQ connection monitor...")
        monitor_connection(connection)
