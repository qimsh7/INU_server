from django.urls import path
from arch import views

urlpatterns = [
    path('', views.index, name="index"), # URL 패턴이 감지되었을 때 호출될 view 함수 index()
]
