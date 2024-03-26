from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


@login_required
def home(request):
 return render(request, "home.html", {})



def authView(request):
 if request.method == "POST":
  form = SignupForm(request.POST)

  if form.is_valid():
   form.save()
   return redirect("user:login")
 else:
  form = SignupForm()
 return render(request, "registration/signup.html", {"form": form})