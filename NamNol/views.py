from django.shortcuts import render
from rest_framework import viewsets
from NamNol.models import Post
from NamNol.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Create your views here.
