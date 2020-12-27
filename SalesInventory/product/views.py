from rest_framework import viewsets
from .models import Supplier, Category, Product, SupplierSupplyProduct
from .serializers import CategorySerialzier, SupplierSupplyProductEditSerializer, SupplierSupplyProductSerializer, ProductSerializer, SupplierSerializar


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzier
    
    
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierViewset(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializar
    
    
class SupplierSupplyProductViewset(viewsets.ModelViewSet):
    queryset = SupplierSupplyProduct.objects.all()
    serializer_class = SupplierSupplyProductSerializer

class SupplierSupplyProductEditViewset(viewsets.ModelViewSet):
    queryset = SupplierSupplyProduct.objects.all()
    serializer_class = SupplierSupplyProductEditSerializer