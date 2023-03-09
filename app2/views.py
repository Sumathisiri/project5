from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def abc(request):
    return HttpResponse('<h1>hello</h1>')
def suresh(request):
    return HttpResponse('<h1>suresh.....</h1>')

def sumathi(request):
    return HttpResponse('<h1><marquee>sumathi....</marquee></h1>')
