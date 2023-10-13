from django.urls import path
from .views import UserView,MeetingRoomView, BookingView

urlpatterns = [
    path('users',UserView.as_view()),
    path('rooms',MeetingRoomView.as_view()),
    path('booking',BookingView.as_view()),
]