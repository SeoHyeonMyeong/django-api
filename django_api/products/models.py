from cgi import print_exception
from django.db import models

class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    active      = models.TextField(default="this is cool!")