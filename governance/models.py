from django.db import models
from django.contrib.auth.models import User

class DataResource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class AccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(DataResource, on_delete=models.CASCADE)
    access_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} accessed {self.resource}"


class ComplianceRule(models.Model):
    rule_name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)


class Violation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rule = models.ForeignKey(ComplianceRule, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)