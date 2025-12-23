from datetime import datetime
from user.models import User


def generer_matricule(role_code: str, annex_code: str) -> str:
    """
    Format :
    ANNEXE-ROLE-ANNEE-XXXX
    ex : MORI-ETU-2025-0042
    """

    annee = datetime.now().year

    prefix = f"{annex_code}-{role_code}-{annee}"

    compteur = (
        User.objects
        .filter(matricule__startswith=prefix)
        .count() + 1
    )

    return f"{prefix}-{compteur:04d}"
