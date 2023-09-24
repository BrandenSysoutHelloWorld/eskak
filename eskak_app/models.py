# Define Imports
from django.db import models
from django.contrib.auth.models import User

# START OF FILE: [eskak]: 'models.py'

# ENTRY MODEL
class Entry(models.Model):
    date = models.DateField()
    time = models.TimeField()
    units = models.IntegerField()
    username = models.CharField(max_length=255)


