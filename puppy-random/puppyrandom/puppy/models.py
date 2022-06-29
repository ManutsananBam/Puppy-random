from pyexpat import model
from django.db import models

# Create your models here.
class Puppy(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()