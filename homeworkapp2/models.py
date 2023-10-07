from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Clientname: {self.name}, email: {self.email}, phone_number: {self.phone_number}, address: {self.address}, registration_date: {self.registration_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateField()

    def price_product(self):
        return self.price * self.quantity

    def __str__(self):
        return f'Productname: {self.name}, price: {self.price}, description: {self.description}, quantity: {self.quantity}, date_added: {self.date_added}'

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Ordercustomer: {self.customer}, date_ordered: {self.date_ordered}'