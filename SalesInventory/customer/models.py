from django.db import models
from user.models import Employee

class Customer(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    phone=models.PositiveIntegerField()
    
    def __str__(self):
        return self.first_name
    
    
class EmployeeManageCustomer(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employeeManageCustomer_employee_field')
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='employeeManageCustomer_customer_field')
    description=models.TextField()