from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PostSerializer, PostImageSerializer
from .models import Post, PostImage


def index(request):
    context = {
        "Posts": Post.objects.all(),
        "PostImages": PostImage.objects.all(),
    }
    return render(request, "index.html", context=context)

class PostListAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response("Swagger Schema")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]