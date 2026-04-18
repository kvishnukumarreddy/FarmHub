from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
        ('Grain', 'Grain'),
        ('Pulse', 'Pulse'),
        ('Crop', 'Crop'),
        ('Spice', 'Spice'),
    ]

    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username