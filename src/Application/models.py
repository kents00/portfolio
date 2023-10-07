from django.utils import timezone
from django.db import models


class WorkExperience(models.Model):
    company_photo = models.ImageField(upload_to='media')
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f"Company: {self.company_name}, Role: {self.role}"


class FeaturedProject(models.Model):
    project_photo = models.ImageField(upload_to='media')
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField(max_length=1000)
    publish = models.DateTimeField(default=timezone.now().strftime('%Y-%m-%d'))

    def __str__(self):
        return f"Project: {self.project_name}, Publish Date: {self.publish}"