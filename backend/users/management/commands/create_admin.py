"""
Comando personalizado para crear un superusuario desde variables de entorno.
Útil para deploy automático en Render/Heroku sin acceso a shell interactivo.

Uso:
    python manage.py create_admin
"""

import os
from django.core.management.base import BaseCommand
from users.models import Usuario


class Command(BaseCommand):
    help = 'Crea un superusuario admin desde variables de entorno'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@menupos.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write(
                self.style.WARNING('⚠️  DJANGO_SUPERUSER_PASSWORD no está configurada. Saltando creación de admin.')
            )
            return

        # Verificar si ya existe
        if Usuario.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS(f'✓ El usuario "{username}" ya existe. Saltando creación.')
            )
            return

        # Crear superusuario
        Usuario.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            rol=Usuario.Rol.ADMIN
        )

        self.stdout.write(
            self.style.SUCCESS(f'✓ Superusuario "{username}" creado exitosamente!')
        )
