from django.db import models

class Annex(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True,
        help_text="Code court de l'annexe (MORI, KATI, BAM)"
    )

    nom = models.CharField(max_length=150)

    ville = models.CharField(max_length=100)
    adresse = models.TextField(blank=True)

    actif = models.BooleanField(default=True)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.nom}"
