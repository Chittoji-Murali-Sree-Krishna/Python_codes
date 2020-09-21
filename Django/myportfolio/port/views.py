from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'port/home.html')

def aboutme(request):
    return render(request, 'port/aboutme.html')

def myprojects(request):
    return render(request, 'port/myprojects.html')

def todo(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo/')
    context = {'tasks':tasks, 'form':form}
    return render(request, 'port/todo.html', context)
