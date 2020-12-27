from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views


router=DefaultRouter()

router.register('job', views.JobViewset)
router.register('location', views.LocationViewset)
router.register('user', views.UserViewset)
router.register('employee', views.EmployeeViewset)

urlpatterns = [
    path('',include(router.urls))
]
