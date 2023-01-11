from django.urls import path 
from . import views

urlpatterns = [
    path('', views.getData),
    path('people', views.getPeople),
    path('add', views.addItem),

]