from rest_framework import request, status, viewsets
from .models import Job, Location, User, Employee
from .serializers import JobSerializer, LocationSerializer, UserSerializer, EmployeeSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response

from .serializers import UserSerializer, UserSigninSerializer
from .authentication import token_expire_handler, expires_in

@api_view(["POST"])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def signin(request):
    signin_serializer = UserSigninSerializer(data = request.data)
    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status = HTTP_400_BAD_REQUEST)


    user = authenticate(
            username = signin_serializer.data['username'],
            password = signin_serializer.data['password'] 
        )
    if not user:
        return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
        
    #TOKEN STUFF
    token, _ = Token.objects.get_or_create(user = user)
    
    #token_expire_handler will check, if the token is expired it will generate new one
    is_expired, token = token_expire_handler(token)     # The implementation will be described further
    user_serialized = UserSerializer(user)

    return Response({
        'user': user_serialized.data, 
        'expires_in': expires_in(token),
        'token': token.key}, status=HTTP_200_OK)


class LocationViewset(viewsets.ModelViewSet):
    """handle location CRUD"""
    queryset=Location.objects.all()
    serializer_class=LocationSerializer 
    permission_classes=[IsAuthenticated,]
    
class UserViewset(viewsets.ModelViewSet):
    """handle user CRUD"""
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated,]


class EmployeeViewset(viewsets.ModelViewSet):
    """handle employee CRUD"""
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    permission_classes=[IsAuthenticated,]


class UserSigninViewset(viewsets.ViewSet):
    """handle anyone can singup as a user"""
    permission_classes=[AllowAny,]
    def create(self, request):
        permission_classes=[IsAuthenticated,]
    
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class UserLoginApiView(ObtainAuthToken):
    """handl creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    


class LoginView(APIView):
    print("LoginView    "*3)

    def post(self, request):
        print("post ------\n    "*3)
        if 'username' in request.data:
            username = request.data['username'].strip()
        else:
            username = None

        if 'password' in request.data:
            password = request.data['password'].strip()
        else:
            password = None
        # print(username)
        # print(password)
        username_exist = User.objects.filter(username=username)
        if username_exist.exists() == False:
            response = {
                'message': 'No User Found!',
                'status': False,
                'result': None,

            }
            return Response(response) 

        user = authenticate(username=username, password=password)
        result = Token.objects.get_or_create(user=user)[0].key

        return Response({"token":result}, status=status.HTTP_201_CREATED)

class permission(APIView):


    # permission_classes=[AllowAny,]
    permission_classes=[IsAuthenticated,]
    # @permission_required('user.close_task')

    # def user_of_stores(user):
    #     if user.is_authenticated() and user.has_perm("user.close_task"):
    #         return True
    #     else:
    #         return False

    # # Method check using method
    # @user_passes_test(user_of_stores)

    # @permission_required('user_log.Log.can_search')
    def get(self, request):
        print(request.user.get_all_permissions())
        print(request.user.has_perm("user_log.can_search"))
        # @permission_required("user_log.can_search")
        # def check(request ):
        #     return Response("it hase the permission")

        return Response("yes its working")
        
    
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
        