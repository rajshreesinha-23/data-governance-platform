from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('resource/<int:id>/', views.access_resource, name='access_resource'),
    path('logs/', views.logs, name='logs'),
]