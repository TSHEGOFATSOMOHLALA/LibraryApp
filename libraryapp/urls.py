from django.urls import path, include
from . import views

app_name = "libraryapp"

urlpatterns = [
   path('', views.home, name="home"),
   path("signup/", views.SignUp.as_view(), name="signup"),
   path("logout/", views.logout_view, name="logout"),
   path('author/list/', views.AuthorList.as_view(), name="authorlist"),
   path('author/create/', views.AuthorCreate.as_view(), name="authorcreate"),
   path('author/update/<pk>', views.AuthorUpdate.as_view(), name="authorupdate"),
   path('author/delete/<pk>', views.AuthorDelete.as_view(), name="authordelete"),
   path('book/list/', views.BookList.as_view(), name="booklist"),
   path('book/create/', views.BookCreate.as_view(), name="bookcreate"),
   path('book/update/<pk>', views.BookUpdate.as_view(), name="bookupdate"),
   path('book/delete/<pk>', views.BookDelete.as_view(), name="bookdelete"),
]