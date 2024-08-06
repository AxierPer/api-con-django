from django.db import models

# Create your models here.

class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  technologies = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)