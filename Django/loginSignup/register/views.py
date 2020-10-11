from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def signup(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = RegisterForm()
    form = RegisterForm()
    return render(response, "register/signup.html", {"form":form})