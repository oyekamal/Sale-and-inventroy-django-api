from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views
from customer import views as customer_views
from product import views as product_views
from django.conf.urls import url



router=DefaultRouter()

router.register('job', views.JobViewset)
router.register('location', views.LocationViewset)
router.register('user', views.UserViewset)
router.register('employee', views.EmployeeViewset)
router.register('signup', views.UserSigninViewset, basename='signup')
router.register('customer', customer_views.CustomerViewset)
router.register('employee-manage-customer-list', customer_views.EmployeeManageCustomerViewset)
router.register('employee-manage-customer-edit', customer_views.EmployeeManageCustomerEditViewset)
router.register('category', product_views.CategoryViewset)
router.register('product', product_views.ProductViewset)
router.register('supplier', product_views.SupplierViewset)
router.register('supply-product', product_views.SupplierSupplyProductViewset)
router.register('supply-product-edit',product_views.SupplierSupplyProductEditViewset)
router.register('product-stock-info',product_views.ProductStockInfo)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.UserLoginApiView.as_view()),
]
