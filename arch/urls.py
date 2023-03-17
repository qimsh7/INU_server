from django.urls import path
from rest_framework.routers import DefaultRouter
from arch import views
from arch.views import PostListAPI

# router = DefaultRouter()

urlpatterns = [
    path('v1/test/', PostListAPI.as_view(), name="test")
]
