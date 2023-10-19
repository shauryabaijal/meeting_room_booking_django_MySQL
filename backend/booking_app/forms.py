from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User,Booking,MeetingRoom

## API stuff
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "first_name", "last_name"]
        error_class = "error"

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ["email", "first_name", "last_name"]
        error_class = "error"

## Normal App
from django import forms
from django.core.exceptions import ValidationError

def validate_email(value):
    sec = value.split('@')[1]
    allowed_hosts = ["clovia.com","purplepanda.in"]
    if(sec not in allowed_hosts):
        raise ValidationError((f"{sec} is not proper"))
class SignUpForm(UserCreationForm):
	email = forms.EmailField(validators=[validate_email],label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
		self.fields['email'].label = ''
		self.fields['email'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
      
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

    
class BookingForm(forms.ModelForm):
    start_time = forms.DateTimeField(required=True,input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    end_time = forms.DateTimeField(required=True,input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        }))
    class Meta:
        model = Booking
        fields = ['room']
    
class MeetingRoomForm:
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="name")
    capacity = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"Capacity", "class":"form-control"}), label="capacity")
    location  = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}), label="location")
    description = forms.CharField( widget=forms.widgets.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), label="description")

