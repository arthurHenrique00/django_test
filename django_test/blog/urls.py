from django.urls import path

from . import views

urlspatterns = [
    path('', views.PostView.as_view(), name='home'),
]