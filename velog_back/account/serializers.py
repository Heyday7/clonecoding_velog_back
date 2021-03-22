from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
class UserSerializer(serializers.ModelSerializer):
  confirm = serializers.CharField(max_length=100, write_only=True)
  email = serializers.EmailField(required=True)

  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'email', 'confirm']

  def validate(self, data):
    if data['password'] != data['confirm']:
      raise serializers.ValidationError('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
    return data

  def create(self, validated_data):
    validated_data.pop('confirm')
    user = User.objects.create(**validated_data)
    user.set_password(validated_data['password'])
    user.save()

    return user

  def update(self, instance, validated_data):
    instance.username = validated_data['username']
    instance.password = validated_data['password']
    instance.email = validated_data['email']
    instance.save()

    return instance

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=100, required=True)
  password = serializers.CharField(max_length=100, required=True)

  def validate(self, data):
    user = authenticate(username=data['username'], password=data['password'])
    if user is None:
      raise serializers.ValidationError('username 혹은 password가 일치하지 않습니다.')
    
    return data

  def perform_login(self, request):
    user = authenticate(username=request.data['username'], password=request.data['password'])
    login(request, user)
    return user

