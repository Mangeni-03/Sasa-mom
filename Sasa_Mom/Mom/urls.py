from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_mother, name='register'),
    path('register/success/', views.register_success, name='register_success'),
    path('dashboard/<int:mother_id>/', views.mother_dashboard, name='dashboard'),
]