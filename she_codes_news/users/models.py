
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

# # Started to make class User Profile
# from django.db import models
# from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    pass
def __str__(self):
    return self.username



# Extending User Model Using a One-To-One Link
# class UserProfile(AbstractUser):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # bio = models.TextField()

    # def __str__(self):
    #     return self.user.username