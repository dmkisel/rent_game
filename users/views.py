from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView,LogoutView
from .models import AppUser

# Create your views here.

class RegisterView(CreateView):
    model = AppUser
    fields = ('username', 'name', 'telegram', 'password1', 'password2')
    template_name = 'users/register.html'
    success_url = 'users/profile.html'
class AuthLoginView(LoginView):
    template_name = 'users/login.html'
