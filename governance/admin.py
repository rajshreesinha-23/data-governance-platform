from django.contrib import admin
from .models import DataResource, AccessLog, ComplianceRule, Violation

admin.site.register(DataResource)
admin.site.register(AccessLog)
admin.site.register(ComplianceRule)
admin.site.register(Violation)