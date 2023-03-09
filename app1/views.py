from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Siri(request):
    return HttpResponse('<h1>Siriii......</h1>')

def srujana(request):
    return HttpResponse('<h1>srujana...</h1>')
