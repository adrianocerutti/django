from django.urls import path
from . import views

urlpatterns = [
    path('domingo', views.domingo),
    path('segunda', views.segunda),
    path('terca', views.terca),
]
