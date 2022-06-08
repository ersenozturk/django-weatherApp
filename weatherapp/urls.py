from django.urls import path
from .views import home ,delete_city

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:id>', delete_city, name="delete"),
]