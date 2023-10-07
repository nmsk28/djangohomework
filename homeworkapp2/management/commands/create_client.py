from django.core.management.base import BaseCommand
from homeworkapp2.models import Client

class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        # client = Client(name='John', email='john@example.com', phone_number=11111111, address='Boston', registration_date='2020-11-11')
        # client = Client(name='Jack', email='jack@example.com', phone_number=33333333, address='New York', registration_date='2020-11-13')
        #client = Client(name='Max', email='max@example.com', phone_number=22222222, address='Edmonton', registration_date='2020-11-12')
        #client = Client(name='Don', email='don@example.com', phone_number=44444444, address='Sietl', registration_date='2020-10-12')
        client = Client(id= 3, name='Lee', email='leen@example.com', phone_number=12345678, address='Bonn',
                        registration_date='2020-10-22')
        client.save()
        self.stdout.write(f'{client}')
