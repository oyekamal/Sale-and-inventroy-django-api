from django.db import models
from user.models import Employee

class Customer(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    phone=models.PositiveIntegerField()
    
    def __str__(self):
        return self.first_name
    
    
class EmployeeManageCustomer(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    description=models.TextField()