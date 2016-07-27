from django.contrib.auth.models import User
from rest_framework import serializers
from dashboard.models import Room, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room


class MessageSerializer(serializers.ModelSerializer):
    snd = serializers.ReadOnlyField(source='sender.username')
    rcv = serializers.ReadOnlyField(source='receiver.username')
    class Meta:
        model = Message
        fields = ('id', 'content', 'snd', 'rcv', 'is_read', 'created_at')
