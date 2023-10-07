from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Productname: {self.name}, price: {self.price}, description: {self.description}, quantity: {self.quantity}, date_added: {self.date_added}'




