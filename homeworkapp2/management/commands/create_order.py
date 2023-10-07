from django.core.management.base import BaseCommand
from homeworkapp2.models import Client, Product, Order
import random
class Command(BaseCommand):
    help = "Generate fake orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        customers = Client.objects.all()
        products = Product.objects.all()
        # for i in range(1, count + 1):
        #     customer = Client(name='Lee', email='leen@example.com', phone_number=12345678, address='Bonn',
        #                 registration_date='2020-10-22')
        #     product = Product(name='bread', price=2.02, description='nutritious', quantity=10, date_added='2023-09-20')
        #     customer.save()
        #     product.save()
        #     customers.append(customer)
        #     products.append(product)

        for i in range(len(customers)):

            cust = customers[i]
            prod = products[i]
            order = Order(customer=cust, total_price = prod.price * prod.quantity)
            order.save()
            order.products.add(prod)

            self.stdout.write(f'{order}')