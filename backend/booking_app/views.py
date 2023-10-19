from rest_framework import generics,viewsets,permissions
from .models import MeetingRoom, Booking
from .serializers import MeetingRoomSerializer, BookingSerializer


## API Stuff
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
    
## Simple ORM app
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,BookingForm,MeetingRoomForm
def home(request):
    records = None
    if request.user.is_authenticated:
        user = request.user
        records = Booking.objects.filter(user=user)
        print(records)
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']

        #Authentoication
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "Wrong Credentials!")
            return redirect('home')
    return render(request, 'home.html', {'records':records})

def login_user(request):
    return

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			# Authenticate and login
			username = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def booking_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		record = Booking.objects.get(id=pk)
		return render(request, 'bookings.html', {'record':record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
     
def delete_booking(request, pk):
	if request.user.is_authenticated:
		delete_it = Booking.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')
    
def add_record(request):
	form = BookingForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'addbooking.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_booking(request, pk):
	if request.user.is_authenticated:
		current_record = Booking.objects.get(id=pk)
		form = BookingForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'updatebooking.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')