from django.db import models

class Article(models.Model):
    user        = models.CharField(max_length=20)
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    pictures    = models.TextField(blank=True, null=True)