from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    '''
    User Model
    '''
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    date_joined =  models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    

class MeetingRoom(models.Model):
    '''
    Meeting Model
    '''
    name = models.CharField(max_length=100,blank=False)
    capacity = models.PositiveIntegerField(blank=False)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.name

class Booking(models.Model):
    '''
    Booking Model
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE,blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    purpose = models.TextField()

    def __str__(self):
        return f"Booking for {self.user} in {self.room} from {self.start_time} to {self.end_time}"