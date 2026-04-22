from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resources/', views.resources, name='resources'),
    path('logs/', views.logs, name='logs'),
    path('compliance/', views.compliance, name='compliance'),
]