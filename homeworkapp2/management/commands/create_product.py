from django.core.management.base import BaseCommand
from homeworkapp2.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        #product = Product(name='bread', price=2.02, description='nutritious', quantity=10, date_added='2023-09-20')
        #product = Product(name='milk', price=1.52, description='nutritious', quantity=12, date_added='2023-09-21')
        #product = Product(name='apples', price=0.52, description='tasty', quantity=9, date_added='2023-09-22')
        #product = Product(name='oranges', price=2.52, description='very tasty', quantity=5, date_added='2023-09-23')
        #product = Product(name='cheese', price=2.01, description='non-GMO', quantity=7, date_added='2023-09-24')
        product = Product(name='dill', price=1.11, description='healthy', quantity=4, date_added='2023-09-25')
        product.save()
        self.stdout.write(f'{product}')