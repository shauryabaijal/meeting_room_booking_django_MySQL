from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .managers import CustomUserManager
# Create your models here.
class User(AbstractUser,PermissionsMixin):
    '''
    User Model
    '''
    first_name = models.CharField('First Name',max_length=20,blank=False)
    last_name = models.CharField('Last Name',max_length=20,blank=False)
    email_id = models.EmailField('Email',max_length=22,blank=False)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()
    def _str_(self):
        return self.first_name +' '+  self.last_name
    

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
