from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default="5")

class Order(models.Model):
    product = models.ForeignKey('app.Product')
    status = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
