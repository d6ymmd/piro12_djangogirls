from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_lsit, name='post_list'),
]