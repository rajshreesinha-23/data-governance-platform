from django.db import models
from django.contrib.auth.models import User

class DataResource(models.Model):
    SENSITIVITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    sensitivity = models.CharField(max_length=10, choices=SENSITIVITY_CHOICES)
    allowed_roles = models.CharField(
        max_length=100,
        help_text="Comma-separated roles e.g. admin,auditor"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_allowed_roles(self):
        return [r.strip() for r in self.allowed_roles.split(',')]


class AccessLog(models.Model):
    STATUS_CHOICES = [
        ('granted', 'Granted'),
        ('denied', 'Denied'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(DataResource, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} → {self.resource.name} [{self.status}]"