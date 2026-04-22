from django.contrib import admin
from .models import DataResource, AccessLog

admin.site.register(DataResource)
admin.site.register(AccessLog)