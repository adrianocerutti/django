from django.urls import path
from . import views

urlpatterns = [
    path('domingo', views.domingo),
]
