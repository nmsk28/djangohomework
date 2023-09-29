from django.core.management.base import BaseCommand
from homeworkapp2.models import Client

class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        # client = Client(name='John', email='john@example.com', phone_number=11111111, address='Boston', age=25, registration_date='2020-11-11')
        # client = Client(name='Jack', email='jack@example.com', phone_number=33333333, address='New York', age=50,
                        # registration_date='2020-11-13')
        client = Client(name='Max', email='max@example.com', phone_number=22222222, address='Edmonton', age=20,
                        registration_date='2020-11-12')
        client.save()
        self.stdout.write(f'{client}')
