from django import forms
from .models import Author, Book

class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorUpdateForm(forms.ModelForm):
    #form for updating authors
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')

class BookUpdateForm(forms.ModelForm):
    #form for updating books
    class Meta:
        model = Book
        fields = "__all__"


