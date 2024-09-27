# calculator/models.py
from django.db import models

class AppCategory(models.Model):
    name = models.CharField(max_length=100)

class AppFeature(models.Model):
    category = models.ForeignKey(AppCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    hours = models.IntegerField()
