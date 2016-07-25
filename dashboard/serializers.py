from django.contrib.auth.models import User
from rest_framework import serializers
from dashboard.models import Room, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
