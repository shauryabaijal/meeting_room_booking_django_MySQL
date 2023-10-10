from django.contrib import admin
from .models import User,MeetingRoom,Booking


class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room','start_time','end_time')


admin.site.register(User)

admin.site.register(MeetingRoom, MeetingRoomAdmin)

admin.site.register(Booking, BookingAdmin)