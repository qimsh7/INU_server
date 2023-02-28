from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from django.views import generic

def index(request):
    context = {
        "Posts": Post.objects.all()
    }
    return render(request, "index.html", context=context)

class PostListAPI(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)