from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
  user = serializers.CharField(read_only=True)
  post = serializers.CharField(read_only=True)
  reply = serializers.CharField(read_only=True)

  class Meta:
    model = Comment
    fields = [
      'id', 
      'content', 
      'created_at', 
      'user', 
      'reply', 
      'post'
    ]


class PostSerializer(serializers.ModelSerializer):
  user = serializers.CharField(read_only=True)
  comments = CommentSerializer(many=True, read_only=True)
  

  class Meta:
    model = Post
    fields = [
      'id', 
      'title', 
      'content', 
      'created_at', 
      'updated_at', 
      'series', 
      'user', 
      'comments', 
      'tags'
    ]
    extra_kwargs= {'tags': {'required': False}}

class TagSerializer(serializers.ModelSerializer):
  posts = PostSerializer(many=True, read_only=True)
  class Meta:
    model = Tag
    fields = ['id', 'name', 'posts']
    extra_kwargs = {'posts': {'required': False}}


class SeriesSerializer(serializers.ModelSerializer):
  posts = PostSerializer(many=True, read_only=True)

  class Meta:
    model = Series
    fields = [
      'id',
      'name',
      'last_updated',
      'posts'
    ]