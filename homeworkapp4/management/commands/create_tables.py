from django.core.management.base import BaseCommand
from homeworkapp4.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake Clients, Product and Orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'name{i}', email=f'email{i}@jmail.com.',
                            phone_number=i * 1111111111, address=f'address{i}')
            product = Product(name=f'name{i}', description=f'description{i}', price=i * 11, quantity=i)
            client.save()
            product.save()
            for j in range(1, count + 1):
                order = Order(customer=client, products=product, total_price=product.price_product())
                order.save()
