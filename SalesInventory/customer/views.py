from rest_framework import viewsets
from .models import Customer, EmployeeManageCustomer
from .serializer import CustomerSerializer, EmployeeManageCustomerSerializer,EmployeeManageCustomerEditSerializer


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class=CustomerSerializer


class EmployeeManageCustomerViewset(viewsets.ModelViewSet):
    queryset = EmployeeManageCustomer.objects.all()
    serializer_class=EmployeeManageCustomerSerializer
    
    
class EmployeeManageCustomerEditViewset(viewsets.ModelViewSet):
    queryset = EmployeeManageCustomer.objects.all()
    serializer_class=EmployeeManageCustomerEditSerializer
