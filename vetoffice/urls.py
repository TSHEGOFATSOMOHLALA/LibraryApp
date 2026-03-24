from django.urls import path, include

from . import views

app_name = "vetoffice"

urlpatterns = [
   path('', views.home, name="home"),
   path("signup/", views.SignUp.as_view(), name="signup"),
   path("logout/", views.logout_view, name="logout"),
   path('owner/list/', views.OwnerList.as_view(), name="ownerlist"),
   path('owner/create/', views.OwnerCreate.as_view(), name="ownercreate"),
   path('owner/update/<pk>', views.OwnerUpdate.as_view(), name="ownerupdate"),
   path('owner/delete/<pk>', views.OwnerDelete.as_view(), name="ownerdelete"),
   path('patient/list/', views.PatientList.as_view(), name="patientlist"),
   path('patient/create/', views.PatientCreate.as_view(), name="patientcreate"),
   path('patient/update/<pk>', views.PatientUpdate.as_view(), name="patientupdate"),
   path('patient/delete/<pk>', views.PatientDelete.as_view(), name="patientdelete"),
]