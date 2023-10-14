from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from .models import MeetingRoom,Booking
from rest_framework import serializers

User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']

class MeetingRoomSerializer(serializers.ModelSerializer):

    class Meta():
        model = MeetingRoom
        fields = ['id', 'name' ,'capacity', 'location', 'description']

class BookingSerializer(serializers.ModelSerializer):
    

    class Meta():
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)  