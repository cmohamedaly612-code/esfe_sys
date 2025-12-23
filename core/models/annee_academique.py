from core.models import *

class AnneeAcademique(models.Model):
    code = models.CharField(
        max_length=9,
        unique=True,
        help_text="Format : 2024-2025"
    )

    debut = models.DateField()
    fin = models.DateField()

    en_cours = models.BooleanField(default=False)

    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-debut"]

    def __str__(self):
        return self.code
