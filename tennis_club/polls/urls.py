from django.urls import path

from . import views

urlpatterns = [
    path('poller/', views.index, name='index'),
]
