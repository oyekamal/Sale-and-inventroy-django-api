from django.db import models
from user.models import Location


class Supplier(models.Model):
    company_name = models.CharField(max_length=10)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
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
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock=models.DecimalField(max_digits=7, decimal_places=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name
    

class SupplierSupplyProduct(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='supplierSupplyProduct_product_field')
    supplier= models.ForeignKey(Supplier , on_delete=models.CASCADE, related_name='supplierSupplyProduct_supplier_field')
    description=models.TextField()
    
    