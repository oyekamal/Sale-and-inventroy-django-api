from rest_framework import viewsets
from .models import Job, Location, User, Employee
from .serializers import JobSerializer, LocationSerializer, UserSerializer, EmployeeSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class JobViewset(viewsets.ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    
    
class LocationViewset(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer 
    
    
class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    
class UserLoginApiView(ObtainAuthToken):
    """handl creatgin user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES