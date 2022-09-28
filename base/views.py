from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from .models import Room, Topic, Message
from .forms import RoomForm


response = {
    "unauthorized": "Unauthorized action",
    "signup_error": "Unhandled error occurred while user registration"
}


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Username or password does not exist")
        except:
            messages.error(request, "User does not  exist")

    context = {'page': page}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, response["signup_error"])
    # form = MyUserCreationForm()

    # if request.method == "POST":
    #     username = request.POST.get('signupUsername')
    #     password1 = request.POST.get('signupPassword1')
    #     password2 = request.POST.get('signupPassword2')
    #     form = MyUserCreationForm(
    #         username=username, password1=password1, password2=password2)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username.lower()
    #         user.save()

    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, r["signup_error"])

    context = {"page": page, "form": form}
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q)
    )

    topics = Topic.objects.all()
    messages = Message.objects.filter(
        Q(room__topic__name__icontains=q))

    room_count = rooms.count()

    context = {"rooms": rooms, "topics": topics,
               "room_count": room_count, "room_messages": messages}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {"room": room, 'room_messages': messages,
               "participants": participants}
    return render(request, "base/room.html", context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    messages = user.message_set.all()
    topics = Topic.objects.all()

    context = {"user": user, "rooms": rooms,
               'room_messages': messages, "topics": topics}
    return render(request, 'base/profile.html', context)


@ login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "base/room_form.html", context)


@ login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse(response["unauthorized"])

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, "base/room_form.html", context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse(response["unauthorized"])

    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, "base/delete.html", {"obj": room})


@ login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse(response["unauthorized"])

    if request.method == "POST":
        message.delete()
        return redirect('home')
    return render(request, "base/delete.html", {"obj": message})
