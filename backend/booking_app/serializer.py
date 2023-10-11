from rest_framework import serializers
from .models import User,MeetingRoom,Booking


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','email')


class MeetingRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeetingRoom
        fields = ('id', 'capacity', 'location', 'description')

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    room = MeetingRoomSerializer(many=False,read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'user', 'room', 'start_time','end_time','purpose')