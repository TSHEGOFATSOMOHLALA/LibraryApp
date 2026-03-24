from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from .models import  Author, Book
from .forms import AuthorCreateForm, AuthorUpdateForm, BookCreateForm, BookUpdateForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Import logout below:
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("libraryapp:home")
  template_name = "libraryapp/signup.html"

def logout_view(request):
  logout(request)
  return redirect("libraryapp:home")


def home(request):
     return render(request, "libraryapp/home.html")

class AuthorList(ListView):
   model = Author
   template_name = "libraryapp/author_list.html"

class BookList(ListView):
    model = Book
    template_name = "libraryapp/book_list.html"

class AuthorCreate(LoginRequiredMixin, CreateView):
   model = Author
   template_name = "libraryapp/author_create_form.html"
   form_class = AuthorCreateForm
   success_url = reverse_lazy("libraryapp:authorlist")

class BookCreate(LoginRequiredMixin, CreateView):
    model=Book
    template_name = "libraryapp/book_create_form.html"
    form_class = BookCreateForm
    success_url = reverse_lazy("libraryapp:booklist")

class AuthorUpdate(LoginRequiredMixin, UpdateView):
   model = Author
   template_name = "libraryapp/author_update_form.html"
   form_class = AuthorUpdateForm
   success_url = reverse_lazy("libraryapp:authorlist")

class BookUpdate(LoginRequiredMixin, UpdateView):
   model = Book
   template_name = "libraryapp/book_update_form.html"
   form_class = BookUpdateForm
   success_url = reverse_lazy("libraryapp:booklist")

class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = "libraryapp/author_delete_form.html"
    success_url = reverse_lazy("libraryapp:authorlist")

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "libraryapp/book_delete_form.html"
    success_url = reverse_lazy("libraryapp:booklist")










