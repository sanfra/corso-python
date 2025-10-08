"""
Questo file importa tutti i modelli e li rende disponibili.
Django cerca i modelli in models/__init__.py
"""

from .software import Software
from .azienda import Azienda

# Rendi disponibili quando fai: from api.models import Software
__all__ = ['Software', 'Azienda']