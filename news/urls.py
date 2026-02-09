from django.urls import path

from . import views

urlpatterns = [
             path("", views.home, name = "home"),
             path("weather/", views.weather_list , name = "weather_list"),
              path("weather_list", views.weather_list, name="weather_list"),
    ]
