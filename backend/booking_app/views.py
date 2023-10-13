from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializers import MeetingRoomSerializer, UserSerializer, BookingSerializer
from .models import User,MeetingRoom, Booking

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    

class MeetingRoomView(generics.CreateAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    

class BookingView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer