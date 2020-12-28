from rest_framework import viewsets
from .models import Customer, EmployeeManageCustomer
from .serializer import CustomerSerializer, EmployeeManageCustomerSerializer,EmployeeManageCustomerEditSerializer
from rest_framework.permissions import IsAuthenticated


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=[IsAuthenticated,]


class EmployeeManageCustomerViewset(viewsets.ModelViewSet):
    queryset = EmployeeManageCustomer.objects.all()
    serializer_class=EmployeeManageCustomerSerializer
    permission_classes=[IsAuthenticated,]
    
    
class EmployeeManageCustomerEditViewset(viewsets.ModelViewSet):
    queryset = EmployeeManageCustomer.objects.all()
    serializer_class=EmployeeManageCustomerEditSerializer
    permission_classes=[IsAuthenticated,]
