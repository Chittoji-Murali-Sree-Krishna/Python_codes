from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme/', views.aboutme , name='aboutme'),
    path('myprojects/',views.myprojects, name='myprojects'),
    path('todo/', views.todo, name='todo'),
]