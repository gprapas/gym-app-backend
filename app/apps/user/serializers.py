from rest_framework import serializers
from apps.user.models import User
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        exclude = ['password']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        exclude = ['password', 'last_login', 'is_staff', 'is_active', 'is_superuser']


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','password','sex')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
