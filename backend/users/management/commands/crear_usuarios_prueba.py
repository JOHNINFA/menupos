"""
Comando para crear usuarios de prueba rápidamente.
Útil para demos y testing.

Uso:
    python manage.py crear_usuarios_prueba
"""

from django.core.management.base import BaseCommand
from users.models import Usuario


class Command(BaseCommand):
    help = 'Crea usuarios de prueba (admin y mesero) si no existen'

    def handle(self, *args, **options):
        # Admin de prueba
        if not Usuario.objects.filter(username='admin').exists():
            Usuario.objects.create_superuser(
                username='admin',
                email='admin@menupos.com',
                password='menupos2024',
                rol=Usuario.Rol.ADMIN
            )
            self.stdout.write(self.style.SUCCESS('✓ Admin creado: admin / menupos2024'))
        else:
            self.stdout.write(self.style.WARNING('⚠ El admin ya existe'))

        # Mesero de prueba
        if not Usuario.objects.filter(username='mesero1').exists():
            Usuario.objects.create_user(
                username='mesero1',
                email='mesero@menupos.com',
                password='demo123',
                rol=Usuario.Rol.MESERO
            )
            self.stdout.write(self.style.SUCCESS('✓ Mesero creado: mesero1 / demo123'))
        else:
            self.stdout.write(self.style.WARNING('⚠ El mesero ya existe'))
