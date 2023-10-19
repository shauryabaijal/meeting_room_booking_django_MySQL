from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingRoomList, BookingList, MeetingRoomViewSet,BookingViewSet
from django.contrib import admin
from django.urls import path, include

# API defination
router = DefaultRouter()
router.register(r'meetingroooms', MeetingRoomViewSet)
router.register(r'bookingview',BookingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api/booking/',BookingList.as_view())
]


# Simple App 
from .views import home,logout_user,register_user,booking_record,delete_booking,update_booking,add_record
urlpatterns += [
    path('',home,name='home'),
    # path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/', register_user, name='register'),
    path('bookings/<int:pk>',booking_record , name='booking_record'),
    path('delete_record/<int:pk>', delete_booking, name='delete_record'),
    path('update_record/<int:pk>', update_booking, name='update_record'),
    path('add_record/', add_record, name='add_record'),
]