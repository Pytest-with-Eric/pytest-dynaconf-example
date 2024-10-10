from django.urls import path
from .views import index

urlpatterns = [
    path("", index),  # Route for the index view
]
