from django.db import models
from django.contrib.auth.models import AbstractUser


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None,**extra_fields):
#         """
#         Creates and saves a User with the given email, favorite color
#          and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#             **extra_fields
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password,**extra_fields):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#             **extra_fields
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
    
    
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

    # objects = MyUserManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['favorite_color','location']

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
    
    
class Job(models.Model):
    title=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    
    
class Employee(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    job=models.OneToOneField(Job, on_delete=models.CASCADE)
    hired_date=models.DateField(auto_now_add=True)
        
