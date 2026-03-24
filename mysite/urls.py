"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pages/", include("pages.urls")),# new
    path("vetoffice/", include("vetoffice.urls")),
    path("library/",include("library.urls")),
    path("carehome/", include("carehome.urls")),
    path("BikeRentalApp/", include("BikeRentalApp.urls")),
    path("news/", include("news.urls")),
    path("blog/", include("blog.urls")),
    path("tasks/", include ("tasks.urls")),
    path("products/", include("products.urls")),
    path("EventApp/" , include("EventApp.urls")),
    path("polls/", include("polls.urls")),
    path("solo1/", include("solo1.urls")),
    path("vetoffice2/", include("vetoffice2.urls")),
    path("tourist_attractions/", include("tourist_attractions.urls")),
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('libraryapp/',include("libraryapp.urls")),
]
