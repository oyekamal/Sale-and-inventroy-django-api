from django.urls import path, include
from rest_framework import routers
from . import views

router =routers.DefaultRouter()

router.register('customer', views.CustomerViewset)
router.register('emc', views.EmployeeManageCustomerViewset)
router.register('emec', views.EmployeeManageCustomerEditViewset)


urlpatterns = [
    path('', include(router.urls)),
]

