from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *
from django.contrib.auth import logout

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# Create your views here.

class LoginView(views.APIView):
  def post(self, request, *args, **kwargs):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.perform_login(request)
    return Response(serializer.data)

class LogoutView(views.APIView):
  def post(self, request, *args, **kwargs):
    logout(request)
    return Response() 