# 📖 Clase 13 — Imágenes en Cloudinary

> 🎯 **Objetivo**: Entender por qué las imágenes no funcionaban en producción y cómo Cloudinary lo resuelve.
> ⏱️ **Tiempo**: 7 minutos
> 📚 **Pre-requisitos**: Clase [`12-aws-s3.md`](12-aws-s3.md) (mismo concepto, otro proveedor)

---

## 🤔 El problema (real, lo vimos en vivo)

Desplegamos MenuPOS y al crear un producto, **la imagen no aparecía**. ¿Por qué?

### 2 razones que se juntan

1. **El disco de Render es efímero** 🗑️
   Cada vez que Render redespliega tu app, **borra los archivos que subiste**. Las fotos guardadas en `media/` desaparecen.

2. **En producción no servíamos media** 🚫
   Nuestro `urls.py` sirve imágenes solo en desarrollo (`if settings.DEBUG`). En producción (`DEBUG=false`), Django no las entrega.

> Conclusión: en producción **necesitamos un servicio externo** que guarde las imágenes de forma permanente y las sirva. Ese es el trabajo de Cloudinary (o S3).

---

## ☁️ ¿Qué es Cloudinary?

**Cloudinary** es un servicio en la nube **especializado en imágenes y videos**. Guarda tus archivos, los sirve por un CDN rápido, e incluso puede transformarlos (redimensionar, comprimir) al vuelo.

### ¿Por qué Cloudinary y no AWS S3?
Para MenuPOS elegimos Cloudinary porque:
- ✅ **Gratis y sin tarjeta de crédito** (AWS pide tarjeta aunque el uso sea gratis)
- ✅ Integración con Django **muy simple** (una librería, 3 variables)
- ✅ Pensado para imágenes (nuestro caso exacto: fotos de productos)
- ✅ CDN global incluido

### Analogía
Igual que S3, Cloudinary es la **galería de fotos** del restaurante, colgada en una pared externa (la nube). Las fotos viven ahí, separadas de la cocina (backend), y cualquiera con el link las ve — pero Cloudinary además es como tener un **fotógrafo** que puede ajustar el tamaño de la foto según se necesite.

---

## 🔀 Cómo lo integramos (mismo patrón que S3)

Usamos `django-cloudinary-storage`. En `settings.py` hay un interruptor: si existen las credenciales de Cloudinary, las imágenes van ahí; si no, al disco local (desarrollo).

```python
CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME', default='')

if CLOUDINARY_CLOUD_NAME:
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': CLOUDINARY_CLOUD_NAME,
        'API_KEY': config('CLOUDINARY_API_KEY'),
        'API_SECRET': config('CLOUDINARY_API_SECRET'),
    }
    STORAGES = {
        'default': {'BACKEND': 'cloudinary_storage.storage.MediaCloudinaryStorage'},
        'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
    }
```

> 💡 Lo bonito: **el modelo `Producto.imagen` no cambia**. Django, gracias a `django-cloudinary-storage`, guarda el `ImageField` en Cloudinary en vez del disco. El código de la app es idéntico.

---

## 🛠️ Cómo activarlo (paso a paso)

### 1. Crear cuenta en Cloudinary
1. Ve a **https://cloudinary.com** → **Sign Up** (gratis, sin tarjeta)
2. Confirma tu correo

### 2. Copiar las credenciales
En el **Dashboard** de Cloudinary verás:
- **Cloud Name**
- **API Key**
- **API Secret**

### 3. Ponerlas en Render (backend)
En el servicio `menupos-backend` → **Environment**:
```
CLOUDINARY_CLOUD_NAME = tu_cloud_name
CLOUDINARY_API_KEY = tu_api_key
CLOUDINARY_API_SECRET = tu_api_secret
```
Guardar → Render redespliega solo.

### 4. Probar
- Entra a "Gestión de Menú" → crea un producto con imagen
- La imagen ahora se guarda en Cloudinary y **sí aparece** (y no se borra al redesplegar)

> ⚠️ **Seguridad**: el `API_SECRET` es como una contraseña. Va SOLO en las variables de entorno de Render, NUNCA en el código ni en el repo.

---

## 🧠 Quiz rápido

1. ¿Por qué las imágenes no aparecían en producción (2 razones)?
2. ¿Qué ventaja tiene Cloudinary sobre AWS S3 para empezar?
3. ¿Cambia el modelo `Producto` al usar Cloudinary? ¿Por qué sí/no?
4. ¿Dónde van las credenciales de Cloudinary y por qué NO en el repo?

> 📝 Respuestas en el quiz de FASE 8.

## 🔗 Referencias
- [Cloudinary (sitio oficial)](https://cloudinary.com/)
- [django-cloudinary-storage](https://github.com/klis87/django-cloudinary-storage)
