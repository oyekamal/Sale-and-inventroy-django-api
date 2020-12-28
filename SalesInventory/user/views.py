from rest_framework import request, status, viewsets
from .models import Job, Location, User, Employee
from .serializers import JobSerializer, LocationSerializer, UserSerializer, EmployeeSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response


class LocationViewset(viewsets.ModelViewSet):
    """handle location CRUD"""
    queryset=Location.objects.all()
    serializer_class=LocationSerializer 
    
    
class UserViewset(viewsets.ModelViewSet):
    """handle user CRUD"""
    queryset=User.objects.all()
    serializer_class=UserSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    """handle employee CRUD"""
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer


class UserSigninViewset(viewsets.ViewSet):
    """handle anyone can singup as a user"""
    permission_classes=[AllowAny,]
    def create(self, request):
        
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class UserLoginApiView(ObtainAuthToken):
    """handl creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    
class JobViewset(viewsets.ViewSet):
    """below code handle admin creating job and listing"""
    queryset = Job.objects.all()
    permission_classes=[IsAuthenticated,]
    def list(self, request):
        print(request.user.id)
        print(Employee.objects.get(user_id=request.user.id).job_id)
        job_id=Employee.objects.get(user_id=request.user.id).job_id
        print()
        if Job.objects.get(id=job_id).title== 'admin':
            queryset = Job.objects.all()
            serializer = JobSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(' you are not admin ',status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):
        job_id=Employee.objects.get(user_id=request.user.id).job_id
        if Job.objects.get(id=job_id).title!= 'admin':
            return Response(' you are not admin ',status=status.HTTP_400_BAD_REQUEST)
        
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        