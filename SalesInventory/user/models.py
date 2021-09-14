from django.db import models
from django.contrib.auth.models import AbstractUser

    
    
class Location(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    

class User(AbstractUser):
    email = models.EmailField(max_length=255,unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    phone_no = models.PositiveIntegerField(null=True, blank=True)
    location=models.OneToOneField(Location, on_delete=models.CASCADE, null=True, blank=True, default=None)
    full_name = models.TextField(unique=True, default='')
    
    def __str__(self):
        return self.email


    
    def save(self, *args, **kwargs):
        print("args ____________",args)
        # print(kwargs)
        print("kwargs ____________",kwargs)
        print(self.first_name)
        print(self.username)
        # if User.objects.filter(first_name=str(self.first_name)).exists():
        #     # print("yes")
        #     # return False
        #     raise Exception(
        #             ('Draft entries may not have a publication date.')
        #         )
        # else:
        #     print("not found")

        self.full_name = str(self.email) + "_" + str(self.username)

        # super(User, self).save(*args, **kwargs)
        super().save(*args, **kwargs)
        return True

    class Meta:
        unique_together = (('first_name', 'last_name'),)
        permissions = [
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        ]


    
class Job(models.Model):
    title=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    
    
class Employee(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    job=models.OneToOneField(Job, on_delete=models.CASCADE)
    hired_date=models.DateField(auto_now_add=True)
        
