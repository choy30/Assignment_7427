from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from members.forms import RegisterForm


class UserRegister(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')