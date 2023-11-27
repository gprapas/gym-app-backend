from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    sex_choices =(('M', 'MALE'), ('F', 'FEMALE'))
    email = models.EmailField(unique = True)
    sex = models.CharField(choices =sex_choices, max_length = 1)

    def __str__(self):
        return self.username
