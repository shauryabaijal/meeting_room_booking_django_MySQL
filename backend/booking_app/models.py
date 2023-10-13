from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.
class User(AbstractUser,PermissionsMixin):
    '''
    User Model
    '''
    first_name = models.CharField('First Name',max_length=20)
    last_name = models.CharField('Last Name',max_length=20)
    email = models.EmailField('Email Address',max_length=22,unique=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()
    def _str_(self):
        return self.first_name +' '+  self.last_name
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

class MeetingRoom(models.Model):
    '''
    Meeting Model
    '''
    name = models.CharField(max_length=100,blank=False)
    capacity = models.PositiveIntegerField(blank=False)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.title

class Booking(models.Model):
    '''
    Booking Model
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE,blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    purpose = models.TextField()
