from django.db import models
from user.models import Location


class Supplier(models.Model):
    company_name = models.CharField(max_length=10)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    phone_no = models.PositiveIntegerField()

    def __str__(self):
        return self.company_name
    

class Category(models.Model):
    name=models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=10)
    description = models.TextField()
    price = models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    category=models.OneToOneField(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class SupplierSupplyProduct(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier= models.ForeignKey(Supplier , on_delete=models.CASCADE)
    description=models.TextField()
    
    