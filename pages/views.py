from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return HttpResponse('Homepage')

def about_page_view(request): # new
    context = {
        "name": "TSHEGOFATSO",
         "age": 23,  # new
    }
    return render(request, "pages/about.html",context)
