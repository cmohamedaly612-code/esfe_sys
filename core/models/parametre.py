from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import *


class Parametre(models.Model):
    cle = models.CharField(max_length=100, unique=True)
    valeur = models.TextField()

    description = models.TextField(blank=True)

    modifiable = models.BooleanField(default=True)

    date_maj = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cle
