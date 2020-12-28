from django.db import models
from django.contrib.auth.models import AbstractUser

    
    
class Location(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    

class User(AbstractUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    phone_no = models.PositiveIntegerField(null=True, blank=True)
    location=models.OneToOneField(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email


    
class Job(models.Model):
    title=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    
    
class Employee(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    job=models.OneToOneField(Job, on_delete=models.CASCADE)
    hired_date=models.DateField(auto_now_add=True)
        
