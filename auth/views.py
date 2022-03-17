from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


class AppLoginView(LoginView):
    template_name = 'auth/login.html'
