# 📖 Clase 12 — Imágenes en AWS S3

> 🎯 **Objetivo**: Entender qué es S3, por qué guardamos las imágenes ahí (y no en el servidor), y cómo activarlo.
> ⏱️ **Tiempo**: 8 minutos
> 📚 **Pre-requisitos**: Clase [`02-django-venv-dependencias.md`](02-django-venv-dependencias.md)

---

## 🤔 El problema

Cuando el admin sube la foto de una hamburguesa, ¿dónde se guarda?

En desarrollo la guardamos en el disco del servidor (carpeta `media/`). Pero eso tiene un problema grave en producción:

- 🚨 **Railway (donde desplegaremos) borra los archivos subidos cada vez que se redespliega.** Las fotos desaparecerían.
- 🚨 Si tuvieras varios servidores, cada uno tendría fotos distintas.
- 🚨 El disco del servidor es limitado y caro.

---

## ☁️ La solución: AWS S3

**S3** (Simple Storage Service) es el servicio de **almacenamiento de archivos en la nube** de Amazon. Es como un "Google Drive para aplicaciones":

- Guardas archivos (imágenes, PDFs, videos) en "buckets" (cubetas)
- Cada archivo tiene una URL pública
- Es barato, escalable y no se borra al redesplegar

### Analogía
Si el backend es la **cocina** del restaurante, S3 es la **galería de fotos colgada en la pared** (o un almacén externo de fotos): las imágenes viven ahí, separadas de la cocina, y cualquiera con el link las puede ver.

---

## 🔀 Cómo lo dejamos preparado (interruptor USE_S3)

En `settings.py` pusimos un **interruptor**:

```python
USE_S3 = config('USE_S3', default=False, cast=bool)

if USE_S3:
    # ... configura S3 como almacenamiento de imágenes ...
    STORAGES = {
        'default': {'BACKEND': 'storages.backends.s3.S3Storage'},
        ...
    }
```

- `USE_S3=false` (por defecto) → imágenes en disco local. **Así trabajamos ahora.**
- `USE_S3=true` + credenciales → imágenes en el bucket de S3.

> 💡 Lo bueno: **el código de MenuPOS no cambia**. Django, gracias a `django-storages`, guarda el `ImageField` en un lugar u otro según el interruptor. El modelo `Producto.imagen` funciona igual en ambos modos.

---

## 🛠️ Cómo activar S3 cuando tengas cuenta AWS (paso a paso)

> Guárdate esto para cuando crees tu cuenta de AWS (tiene capa gratuita).

### 1. Crear un bucket
1. Entra a la consola de AWS → busca **S3**
2. **Create bucket**
3. Nombre único global (ej: `menupos-imagenes-john`)
4. Región: `us-east-1` (o la más cercana)
5. Desmarca "Block all public access" (las fotos del menú son públicas) y confirma

### 2. Crear un usuario IAM (credenciales)
1. Consola AWS → busca **IAM** → **Users** → **Create user**
2. Nombre: `menupos-app`
3. Adjunta la política **AmazonS3FullAccess** (o una más restringida al bucket)
4. Crea una **Access Key** → guarda el `Access Key ID` y el `Secret Access Key`

### 3. Llenar el .env
En `backend/.env` (NO en `.env.example`):
```env
USE_S3=true
AWS_ACCESS_KEY_ID=tu_access_key
AWS_SECRET_ACCESS_KEY=tu_secret_key
AWS_STORAGE_BUCKET_NAME=menupos-imagenes-john
AWS_S3_REGION_NAME=us-east-1
```

### 4. Probar
- Reinicia el servidor Django
- Sube una imagen de producto desde "Gestión de Menú"
- La URL de la imagen ahora apunta a `https://menupos-imagenes-john.s3.amazonaws.com/...`

> ⚠️ **Seguridad**: las credenciales AWS van SOLO en `.env` (que está en `.gitignore`). Si se filtran a GitHub, alguien podría usar tu cuenta AWS y generarte costos. Nunca las subas.

---

## 🧠 Quiz rápido

1. ¿Por qué no guardamos las imágenes en el disco del servidor en producción?
2. ¿Qué es un "bucket" de S3?
3. ¿Qué hace el interruptor `USE_S3` y por qué es útil?
4. ¿Dónde van las credenciales de AWS y por qué NO en el repositorio?

> 📝 Respuestas en el quiz de FASE 7.

---

## 🔗 Referencias
- [AWS S3 (documentación oficial, español)](https://docs.aws.amazon.com/es_es/s3/)
- [django-storages — Amazon S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
