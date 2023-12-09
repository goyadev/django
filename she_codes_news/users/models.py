
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

# # Started to make class User Profile
# from django.db import models
# from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank = True, null = True)
    
    
    
    
    def __str__(self):
        return self.username

