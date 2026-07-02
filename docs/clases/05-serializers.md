# 📖 Clase 05 — Serializers (el mesero traductor)

> 🎯 **Objetivo**: Entender cómo Django convierte objetos Python ↔ JSON.
> ⏱️ **Tiempo**: 8 minutos
> 📚 **Pre-requisitos**: Clase [`04-modelos-django.md`](04-modelos-django.md)

---

## 🤔 El problema

Un objeto `Producto` en Python se ve así internamente:

```python
<Producto: Hamburguesa Clásica>
```

Pero React necesita JSON:

```json
{"id": 1, "nombre": "Hamburguesa Clásica", "precio": "15000.00"}
```

¿Quién hace esa traducción? El **Serializer**.

## 🧑‍💼 La solución: Serializer

```python
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'categoria']
```

Con esto DRF ya sabe:
- **Serializar** (Python → JSON): para responder peticiones `GET`
- **Deserializar y validar** (JSON → Python): para peticiones `POST`/`PUT`

## 🎬 Analogía

El Serializer es el **mesero traductor**: la cocina (modelo) habla en "objetos Python", el cliente (React) habla en "JSON". El mesero traduce en ambas direcciones y además **revisa que el pedido tenga sentido** (validación) antes de llevarlo a la cocina.

---

## 🔗 Campos calculados y relaciones

A veces queremos mostrar datos de una tabla relacionada, sin exponer TODO el objeto:

```python
class ProductoSerializer(serializers.ModelSerializer):
    # Trae SOLO el nombre de la categoría, no el objeto completo
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'categoria', 'categoria_nombre']
```

Resultado en JSON:
```json
{"id": 1, "nombre": "Hamburguesa", "precio": "15000.00", "categoria": 3, "categoria_nombre": "Hamburguesas"}
```

## ✍️ Serializers anidados (nested) — el caso de Venta

Una Venta tiene VARIOS DetalleVenta. Queremos crear todo **en una sola petición**:

```python
class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True)  # ← lista anidada

    class Meta:
        model = Venta
        fields = ['id', 'mesero', 'fecha', 'total', 'estado', 'detalles']

    def create(self, validated_data):
        # Sobreescribimos create() para manejar la lógica especial:
        # crear la Venta Y todos sus DetalleVenta juntos, calculando el total.
        detalles_data = validated_data.pop('detalles')
        venta = Venta.objects.create(**validated_data)
        for detalle in detalles_data:
            DetalleVenta.objects.create(venta=venta, **detalle)
        return venta
```

> 💡 Sobreescribir `create()` es como decirle al mesero: "para ESTE pedido especial (una venta completa), sigue estos pasos extra antes de mandarlo a cocina".

---

## 🧠 Quiz rápido

1. ¿Qué hace un Serializer, en una frase?
2. ¿Qué significa "deserializar"?
3. ¿Para qué sirve `source='categoria.nombre'`?
4. ¿Por qué sobreescribimos `create()` en `VentaSerializer`?

> 📝 Respuestas en el quiz de FASE 5.

## 🔗 Referencias
- [DRF Serializers (oficial)](https://www.django-rest-framework.org/api-guide/serializers/)
