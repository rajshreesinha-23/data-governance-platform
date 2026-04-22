from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('governance.urls')),
    path('', include('accounts.urls')),
]