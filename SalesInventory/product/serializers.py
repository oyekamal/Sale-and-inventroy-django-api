from rest_framework import serializers
from .models import Supplier, Product, SupplierSupplyProduct, Category
from user.models import Location
from user.serializers import LocationSerializer
from rest_framework.serializers import SerializerMethodField


class CategorySerialzier(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerialzier()
    class Meta:
        model=Product
        fields=['name','description','price','stock','category']
        
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category=CategorySerialzier.create(CategorySerialzier(), validated_data=category_data)
        product= Product.objects.create(name=validated_data.get('name'),
                                  price=validated_data.get('price'),
                                  stock=validated_data.get('stock'),
                                  description=validated_data.get('description'),
                                  category=category)
        return product 
    
    
class SupplierSerializar(serializers.ModelSerializer):
    location=LocationSerializer()

    class Meta:
        model=Supplier
        fields=['company_name','phone_no','location']    
        
    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location=LocationSerializer.create(LocationSerializer(), validated_data=location_data)
        supplier= Supplier.objects.create(company_name=validated_data.get('company_name'),
                                  phone_no=validated_data.get('phone_no'),
                                  location=location)
        return supplier
    def update(self, instance, validated_data):
        location = validated_data.pop('location')
        instance.company_name = validated_data.get("company_name", instance.company_name)
        instance.phone_no = validated_data.get("phone_no", instance.phone_no)

        old_location = instance.location
   
        old_location.province = location.get('province',old_location.province)
        old_location.city = location.get('city',old_location.city)
        old_location.street = location.get('street',old_location.street)
        old_location.save()
        instance.save()

        return instance    
    
  
class SupplierSupplyProductSerializer(serializers.ModelSerializer):
    product=SerializerMethodField('get_product_name', allow_null=True, required=False)
    supplier=SerializerMethodField('get_supplier_name', allow_null=True, required=False)
    def get_product_name(self, obj):
        return obj.product.name
    def get_supplier_name(self, obj):
        return obj.supplier.company_name
    class Meta:
        model= SupplierSupplyProduct
        fields=['product','supplier','description']   


class SupplierSupplyProductEditSerializer(serializers.ModelSerializer):
    class Meta:
        model= SupplierSupplyProduct
        fields=['product','supplier','description']  