from django.http import HttpResponse
from django.shortcuts import render
from .models import Weather

# Create your views here.
def home_news(request):
    return HttpResponse("Home news")

def home(request):
    return render (request, "news/base.html")

def weather_list(request):
    weather = Weather.objects.all()
    return render(request,"news/weather_list.html",{"weather":weather})
