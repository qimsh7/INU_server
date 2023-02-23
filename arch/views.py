from django.shortcuts import render
from arch.models import Post
from django.views import generic

def index(request):
    context = {
        "Posts": Post.objects.all()
    }
    return render(request, "index.html", context=context)