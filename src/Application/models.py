from django.db import models

class WorkExperience(models.Model):
    company_photo = models.ImageField(upload_to='media')
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.company_name

class FeaturedProject(models.Model):
    project_photo = models.ImageField(upload_to='media')
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.project_name