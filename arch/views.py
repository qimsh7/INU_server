from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PostSerializer, PostImageSerializer
from .models import Post, PostImage
from django.views import generic


def index(request):
    context = {
        "Posts": Post.objects.all(),
        "PostImages": PostImage.objects.all(),
    }
    return render(request, "index.html", context=context)

class PostListAPI(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().oreder_by("-created_at")
#     serializer_class = PostSerializer
#     filter_backends = [DjangoFilterBackend]