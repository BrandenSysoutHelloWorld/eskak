# Imports
from django.db import models
from django.contrib.auth.models import User

# START OF FILE: [users]: 'models.py'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

'''CODE IMPLEMENTED & CONTRIBUTED BY: BRANDEN VAN STADEN'''
