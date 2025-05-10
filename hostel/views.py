from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Room, Student
from django.http import HttpResponse

# Create a room
def create_room(request):
    if request.method == 'POST':
        room_number = request.POST['room_number']
        capacity = request.POST['capacity']
        Room.objects.create(room_number=room_number, capacity=capacity)
        return HttpResponse("Room created successfully!")
    return render(request, 'create_room.html')

# Register student to a room
def register_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        room_id = request.POST['room']
        room = Room.objects.get(id=room_id)
        Student.objects.create(name=name, roll_number=roll_number, room=room)
        return HttpResponse("Student registered successfully!")
    rooms = Room.objects.all()
    return render(request, 'register_student.html', {'rooms': rooms})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid credentials!")
    return render(request, 'login.html')
