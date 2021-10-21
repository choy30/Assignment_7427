from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import DogForm, UpdateDogForm, ActivityForm, UpdateActivityForm
from blog.models import Dog, Activity, Breed


class HomePage(ListView):
    model = Dog
    template_name = 'home.html'
class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"
class AddDog(CreateView):
    model = Dog
    form_class = DogForm
    template_name = 'add_dog.html'
class UpdateDog(UpdateView):
    model = Dog
    form_class = UpdateDogForm
    template_name = 'update_dog.html'
class DeleteDog(DeleteView):
    model = Dog
    template_name = 'delete_dog.html'
    success_url = reverse_lazy('home')
class BreedDetail(ListView):
    model = Breed
    template_name = 'breed/breed_details.html'
class AddBreed(CreateView):
    model = Breed
    template_name = 'breed/add_breed.html'
    fields = ['name']
class UpdateBreed(UpdateView):
    model = Breed
    template_name = 'breed/update_breed.html'
    fields = '__all__'
class DeleteBreed(DeleteView):
    model = Breed
    template_name = 'breed/delete_breed.html'
    success_url = reverse_lazy('home')

class ActivityPage(ListView):
    model = Activity
    template_name = "activity/activity_page.html"
class ActivityDetail(DetailView):
    model = Activity
    template_name = "activity/activity_detail.html"
class CreateActivity(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'activity/create_activity.html'
class UpdateActivity(UpdateView):
    model = Activity
    form_class = UpdateActivityForm
    template_name = 'activity/update_activity.html'
class DeleteActivity(DeleteView):
    model = Activity
    template_name = 'activity/delete_activity.html'
    success_url = reverse_lazy('activity')