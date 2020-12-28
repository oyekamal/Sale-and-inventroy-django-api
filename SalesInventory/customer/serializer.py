from rest_framework import serializers
from .models import Customer, EmployeeManageCustomer
from rest_framework.serializers import SerializerMethodField

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
        

class EmployeeManageCustomerSerializer(serializers.ModelSerializer):
    employee =SerializerMethodField('get_employee_name',allow_null=True, required=False)
    customer = SerializerMethodField('get_customer_name',allow_null=True, required=False)
    
    def get_customer_name(self , obj):
        return obj.customer.first_name
    
    def get_employee_name(self , obj):
        return obj.employee.user.username
    class Meta:
        model=EmployeeManageCustomer
        fields=['employee','customer','description']
        


class EmployeeManageCustomerEditSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeManageCustomer
        fields=['employee','customer','description']