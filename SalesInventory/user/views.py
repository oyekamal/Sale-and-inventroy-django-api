from rest_framework import request, status, viewsets
from .models import Job, Location, User, Employee
from .serializers import JobSerializer, LocationSerializer, UserSerializer, EmployeeSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response

class JobViewset(viewsets.ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    
    
class LocationViewset(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer 
    
    
class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated,]


class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


class UserSigninViewset(viewsets.ViewSet):
    permission_classes=[AllowAny,]
    def create(self, request):
        
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class UserLoginApiView(ObtainAuthToken):
    """handl creatgin user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES