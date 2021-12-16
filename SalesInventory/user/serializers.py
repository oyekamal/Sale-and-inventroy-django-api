from rest_framework import serializers
from .models import User, Location, Job, Employee
from django.contrib.auth.hashers import make_password


class JobSerializer(serializers.ModelSerializer):
    """job serializer for employee"""
    class Meta:
        model=Job
        fields='__all__'
        

class LocationSerializer(serializers.ModelSerializer):
    """ loaction is for all user, employee, supplier """
    class Meta:
        model=Location
        fields='__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    """
    Nested serializer of location for user. 
    because user have one to one relationship with location.
    when creating a user you are aloud to give location information too.
    
    """
    location=LocationSerializer()
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','phone_no','password','location']
        
        
    def create(self, validated_data):
        
        location_data = validated_data.pop('location')
        location=LocationSerializer.create(LocationSerializer(), validated_data=location_data)
        user= User.objects.create(email=validated_data.get('email'),
                                  username=validated_data.get('username'),
                                  password=make_password(validated_data.get('password')),
                                  first_name=validated_data.get('first_name'),
                                  last_name=validated_data.get('last_name'),
                                  location=location)
        return user
        

    def update(self, instance, validated_data):
        location = validated_data.pop('location')
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.is_active = validated_data.get("is_active", instance.is_active)

        old_location = instance.location
   
        old_location.province = location.get('province',old_location.province)
        old_location.city = location.get('city',old_location.city)
        old_location.street = location.get('street',old_location.street)
        old_location.save()
        instance.save()

        return instance
    
    
class EmployeeSerializer(serializers.ModelSerializer):
    """
    handle nested serializer for user and job.
    because they are one to one relationship with eachother
    """
    user=UserSerializer()
    job=JobSerializer()
    class Meta:
        model=Employee
        fields=['user','job','hired_date']
        
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        job_data = validated_data.pop('job')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        job = JobSerializer.create(JobSerializer(), validated_data=job_data)
        employee = Employee.objects.create(job=job,
                                            user=user)
        return employee

    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        job = validated_data.pop('job')

        old_user = instance.user
        old_job = instance.job
   
        UserSerializer.update(user)
             
        old_job.title = job.get('title',old_job.title)
        old_job.salary = job.get('salary',old_job.salary)
        old_job.save()
        instance.save()

        return instance
    
    
# from rest_framework import serializers

class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)