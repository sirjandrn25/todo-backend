from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)
# Create your tests here.
router = SimpleRouter()
router.register("tasks", TaskViewSet, basename="task")
urlpatterns = [
    path("", include(router.urls)),
    path("user_register/", UserRegisterApiView.as_view(), name="user_signup"),
    path("user_login/", UserLoginApiView.as_view(), name="user_signin"),
    path('refresh_token/', TokenRefreshView.as_view(), name="refresh"),
]
