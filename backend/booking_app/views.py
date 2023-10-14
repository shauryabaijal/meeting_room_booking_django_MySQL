from rest_framework import generics,viewsets,permissions
from .models import MeetingRoom, Booking
from .serializers import MeetingRoomSerializer, BookingSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user to the currently logged-in user
        serializer.save(user=self.request.user)

class MeetingRoomList(generics.ListAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer

class MeetingRoomViewSet(viewsets.ModelViewSet):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer

class BookingViewSet(viewsets.ModelViewSet):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def user_reservations(self, request):
        user = request.user
        reservations = Booking.objects.filter(user=user)
        serializer = BookingSerializer(reservations, many=True)
        return Response(serializer.data)