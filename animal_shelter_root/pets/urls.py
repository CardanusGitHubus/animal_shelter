from django.urls import path
from . import views

urlpatterns = [
    path('display_pets', views.index, name='index'),
    path('upload_pet', views.uploadView, name='upload_pet'),
]
