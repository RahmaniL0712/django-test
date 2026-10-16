from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    colors = models.CharField(max_length=10)
    price = models.IntegerField(
        validators=[MinValueValidator(0)]
        )
    stock = models.IntegerField()
    
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50)
    vendor_nipt = models.CharField(max_length=14)
    vendor_address = models.CharField(max_length=250)
    
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    client_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    
    
