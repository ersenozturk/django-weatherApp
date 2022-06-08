from django.urls import path
from .views import base ,delete_city

urlpatterns = [
    path('', base, name="base"),
    path('delete/<int:id>', delete_city, name="delete"),
]