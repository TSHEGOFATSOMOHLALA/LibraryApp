from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Import logout below:
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("vetoffice:home")
  template_name = "vetoffice/signup.html"

def logout_view(request):
  logout(request)
  return redirect("vetoffice:home")


def home(request):
     return render(request, "vetoffice/home.html")

class OwnerList(ListView):
   model = Owner
   template_name = "vetoffice/owner_list.html"

class PatientList(ListView):
    model = Patient
    template_name = "vetoffice/patient_list.html"

class OwnerCreate(LoginRequiredMixin, CreateView):
   model = Owner
   template_name = "vetoffice/owner_create_form.html"
   form_class = OwnerCreateForm
   success_url = reverse_lazy("vetoffice:ownerlist")

class PatientCreate(LoginRequiredMixin, CreateView):
    model=Patient
    template_name = "vetoffice/patient_create_form.html"
    form_class = PatientCreateForm
    success_url = reverse_lazy("vetoffice:patientlist")

class OwnerUpdate(LoginRequiredMixin, UpdateView):
   model = Owner
   template_name = "vetoffice/owner_update_form.html"
   form_class = OwnerUpdateForm
   success_url = reverse_lazy("vetoffice:ownerlist")

class PatientUpdate(LoginRequiredMixin, UpdateView):
   model = Patient
   template_name = "vetoffice/patient_update_form.html"
   form_class = PatientUpdateForm
   success_url = reverse_lazy("vetoffice:patientlist")

class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"
    success_url = reverse_lazy("vetoffice:ownerlist")

class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"
    success_url = reverse_lazy("vetoffice:patientlist")









