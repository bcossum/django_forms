from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages

def index(request): 
  form = UserForm()
  context = {
    "regForm": form,
    "all_users": User.objects.all()
    }  
  if request.method == "POST":
    bound_form = UserForm(request.POST)
    if bound_form.isvalid():
      User.objects.create(bound_form)
    else messages

  return render(request, 'index.html', context)

def success(request):
  return render(request, 'success.html')
  