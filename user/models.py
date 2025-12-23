from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import Annex  # sera créé dans core



class User(AbstractBaseUser, PermissionsMixin):
    matricule = models.CharField(
        max_length=30,
        unique=True,
        db_index=True,
        help_text="Matricule institutionnel de connexion"
    )

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_creation = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "matricule"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.matricule} - {self.nom} {self.prenom}"


class Role(models.Model):
    code = models.CharField(
        max_length=20,
        unique=True,
        help_text="Code court du rôle (ETU, ENS, DE, DG, etc.)"
    )
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Profil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profil"
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT
    )

    annex = models.ForeignKey(
        Annex,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text="Annexe de rattachement (null pour DG / SuperAdmin)"
    )

    actif = models.BooleanField(default=True)

    date_affectation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.matricule} ({self.role.code})"
