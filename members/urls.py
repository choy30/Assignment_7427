from django.urls import path

from members.views import UserRegister

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
]