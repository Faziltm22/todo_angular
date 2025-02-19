from rest_framework import serializers
from .models import Todo,User

class TodoSerialaizer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}