from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# Create your views here.
