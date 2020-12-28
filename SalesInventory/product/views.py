from rest_framework import status, viewsets
from .models import Supplier, Category, Product, SupplierSupplyProduct
from .serializers import CategorySerialzier, SupplierSupplyProductEditSerializer, SupplierSupplyProductSerializer, ProductSerializer, SupplierSerializar
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Avg, Max, Min, Sum

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzier
    permission_classes=[IsAuthenticated,]
    
    
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAuthenticated,]
    
class ProductStockInfo(viewsets.ViewSet):
    queryset = Product.objects.all()
    def list(self, request):
        queryset = Product.objects.all()
        max_price = queryset.aggregate(Max('price'))
        min_price = queryset.aggregate(Min('price'))
        avg_price = queryset.aggregate(Avg('price'))
        total_items_price = queryset.aggregate(Sum('price'))
        number_of_items = queryset.aggregate(Sum('stock'))
        
        stock_worth = total_items_price['price__sum'] * number_of_items['stock__sum']
        content = {'product':[max_price,
                         min_price,
                         avg_price,
                         total_items_price,
                         number_of_items,
                         ],'Total_worth':stock_worth}
        print(content)
        return Response(content,status=status.HTTP_200_OK)

class SupplierViewset(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializar
    permission_classes=[IsAuthenticated,]
    
    
class SupplierSupplyProductViewset(viewsets.ModelViewSet):
    queryset = SupplierSupplyProduct.objects.all()
    serializer_class = SupplierSupplyProductSerializer
    permission_classes=[IsAuthenticated,]

class SupplierSupplyProductEditViewset(viewsets.ModelViewSet):
    queryset = SupplierSupplyProduct.objects.all()
    serializer_class = SupplierSupplyProductEditSerializer
    permission_classes=[IsAuthenticated,]