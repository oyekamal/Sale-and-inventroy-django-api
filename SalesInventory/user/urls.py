from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views


router=DefaultRouter()

router.register('job', views.JobViewset)
router.register('location', views.LocationViewset)
router.register('user', views.UserViewset)
router.register('employee', views.EmployeeViewset)
router.register('signup', views.UserSigninViewset, basename='signup')

urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.UserLoginApiView.as_view()),
]
