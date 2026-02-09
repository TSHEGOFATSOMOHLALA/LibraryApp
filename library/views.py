from django.shortcuts import render
from .models import Book,Author
# Create your views here.

def home(request):
    return render(request , "library/home.html")

def book_list(request):
    books = Book.objects.all()
    return render(request,"library/book_list.html",{"books":books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, "library/author_list.html" , {"authors":authors})