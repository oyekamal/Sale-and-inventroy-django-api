from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views
from customer import views as customer_views
from product import views as product_views
from user_log import views as log_views
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls


# from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
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
router.register('Log', log_views.LogViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.UserLoginApiView.as_view()),
    path(r'docs/', include_docs_urls(title='Polls API')),
]
