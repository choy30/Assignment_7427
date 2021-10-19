from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import HomePage, DogDetail, AddDog, UpdateDog, DeleteDog, ActivityDetail, CreateActivity, \
    UpdateActivity, DeleteActivity, ActivityPage

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('dog/<int:pk>', DogDetail.as_view(), name="dog-detail"),
    path('add_dog/', AddDog.as_view(), name='add-dog'),
    path('dog/update/<int:pk>', UpdateDog.as_view(), name='update-dog'),
    path('dog/delete/<int:pk>', DeleteDog.as_view(), name='delete-dog'),
    path('activity', ActivityPage.as_view(), name='activity'),
    path('activity/<int:pk>', ActivityDetail.as_view(), name='activity-detail'),
    path('create_activity/', CreateActivity.as_view(), name='create-activity'),
    path('activity/update/<int:pk>', UpdateActivity.as_view(), name='update-activity'),
    path('activity/delete/<int:pk>', DeleteActivity.as_view(), name='delete-activity'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)