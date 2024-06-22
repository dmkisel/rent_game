from django.shortcuts import render
from django.views.generic import CreateView
from .models import AppUser

# Create your views here.

class RegisterView(CreateView):
    model = AppUser
    fields = '__all__'
    template_name = 'users/register.html'

