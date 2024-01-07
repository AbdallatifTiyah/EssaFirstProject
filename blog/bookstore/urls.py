from django.urls import path
from bookstore import views

urlpatterns = [
    path('', views.home),
    path('users/', views.users),
    path('about/', views.about),
]