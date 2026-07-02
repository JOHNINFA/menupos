"""
Serializer del Usuario. Ver mini-clase: docs/clases/05-serializers.md
"""

from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # NUNCA incluir 'password' aquí: expondría el hash en la API.
        fields = ['id', 'username', 'first_name', 'last_name', 'rol']
