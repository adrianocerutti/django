from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def domingo(request):
    return HttpResponse("Ler Livro sobre Django")

def segunda(request):
    return HttpResponse("Assistir Série Breaking Bad")

def terca(request):
    return HttpResponse("Estudar sobre programação em Python")