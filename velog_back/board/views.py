from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from .filters import PostFilter
from .pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all().order_by('-created_at')
  serializer_class = PostSerializer
  filter_backends = (DjangoFilterBackend, )
  filterset_class = PostFilter
  pagination_class = CustomPageNumberPagination

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user, post=Post.objects.get(id=self.kwargs['post_id']))


class SeriesViewSet(viewsets.ModelViewSet):
  queryset = Series.objects.all()
  serializer_class = SeriesSerializer


class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

  
# Create your views here.
