from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomerUser
from django.contrib.auth import login, authenticate, logout
# Create your views here.

page = 'login'


class Profiles(View):
    def get(self, request):
        profiles = Profile.objects.all()
        context = {'profiles': profiles}
        return render(request, 'users/profiles.html', context)


class UserProfile(View):
    def get(self, request, pk):
        profiles = Profile.objects.get(id=pk)
        context = {'profiles': profiles}
        return render(request, 'users/user_profiles.html', context)


class LoginPage(View):

    def get(self, request):
        page = 'login'
        if request.user.is_authenticated:
            return redirect('profiles')
        return render(request, 'users/login_register.html')

    def post(self, request):
        username = request.POST['user']
        password = request.POST['pass']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username dose not exist')
            return redirect('LoginPage')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('LoginPage')


class loginoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('LoginPage')


class registerUser(View):
    def get(self, request):
        page = 'register'
        form = CustomerUser()
        context = {'page': page, 'form': form}
        return render(request, 'users/login_register.html', context)

    def post(self, request):
        form = CustomerUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "successful")
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "An error")
            return redirect('register')
