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


class UsuarioCreateSerializer(serializers.ModelSerializer):
    """
    Serializer SOLO para que un admin cree meseros/otros admins.

    Se separa de UsuarioSerializer porque crear un usuario SÍ necesita
    recibir una contraseña (en texto plano, solo en esta petición) y
    guardarla correctamente encriptada — algo que ModelSerializer no
    hace solo, por eso sobreescribimos create().
    """
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'rol']

    def create(self, validated_data):
        # create_user() es el método de Django que ENCRIPTA la contraseña
        # antes de guardarla (nunca se guarda en texto plano en la BD).
        return Usuario.objects.create_user(**validated_data)
