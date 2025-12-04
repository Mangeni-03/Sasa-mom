from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_mother, name='register'),
    path('mother/<int:pk>/', views.motherPage, name='motherPage'),
]