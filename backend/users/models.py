"""
Modelo de Usuario para MenuPOS.

Extendemos el Usuario que YA trae Django (AbstractUser) en vez de crear
uno desde cero, porque así heredamos gratis: contraseñas encriptadas,
sistema de permisos, login/logout, y compatibilidad con el Admin.

Solo le agregamos lo que MenuPOS necesita de más: el campo `rol`.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """
    Representa a una persona que puede iniciar sesión en MenuPOS.

    Hereda de AbstractUser: ya trae username, password, email,
    first_name, last_name, is_active, is_staff, etc.
    """

    class Rol(models.TextChoices):
        # TextChoices crea un "enum": solo se permiten estos 2 valores.
        # Formato: NOMBRE_PYTHON = 'valor_guardado_en_bd', 'Etiqueta legible'
        ADMIN = 'admin', 'Administrador'
        MESERO = 'mesero', 'Mesero'

    rol = models.CharField(
        max_length=10,
        choices=Rol.choices,
        default=Rol.MESERO,
        help_text='Define qué puede hacer este usuario dentro de MenuPOS.'
    )

    def __str__(self):
        # __str__ define cómo se ve este objeto cuando Python lo imprime
        # (ej: en el Admin de Django, en el shell, en logs).
        return f'{self.username} ({self.get_rol_display()})'
