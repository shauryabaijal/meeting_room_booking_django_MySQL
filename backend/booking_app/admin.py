from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,MeetingRoom,Booking
from .forms import CustomUserChangeForm, CustomUserCreationForm

class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display =  ('first_name','last_name','email','is_admin')
    list_display_links = ['email']
    list_filter = ('first_name','last_name','email','is_admin')
    search_fields = ('first_name','last_name','email')



class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room','start_time','end_time')


admin.site.register(User,UserAdmin)

admin.site.register(MeetingRoom, MeetingRoomAdmin)

admin.site.register(Booking, BookingAdmin)