from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingRoomList, BookingList, MeetingRoomViewSet,BookingViewSet

router = DefaultRouter()
router.register(r'meetingroooms', MeetingRoomViewSet)
router.register(r'bookingview',BookingViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/booking/',BookingList.as_view())
]