from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PostSerializer, PostImageSerializer
from .models import Post, PostImage
from  .open_api_params import get_params, post_params
from django.views import generic


def index(request):
    context = {
        "Posts": Post.objects.all(),
        "PostImages": PostImage.objects.all(),
    }
    return render(request, "index.html", context=context)

class PostListAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(manual_parameters=get_params)
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=post_params)
    def post(self, request):
        return Response("Swagger Schema")

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().oreder_by("-created_at")
#     serializer_class = PostSerializer
#     filter_backends = [DjangoFilterBackend]