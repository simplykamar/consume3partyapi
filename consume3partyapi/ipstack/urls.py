from django.urls import path
from ipstack import views
urlpatterns = [
    path('', views.index),
]
