# 🧠 Quiz FASE 7 — Imágenes en AWS S3

> 📚 **Clase que cubre**: [`12-aws-s3.md`](../clases/12-aws-s3.md)

---

## 📝 Preguntas

1. ¿Por qué NO guardamos las imágenes en el disco del servidor en producción?
2. ¿Qué es un "bucket" de S3?
3. ¿Qué hace el interruptor `USE_S3` en settings.py y por qué es útil?
4. ¿Dónde van las credenciales de AWS y por qué NUNCA en el repositorio?
5. Con la metáfora del restaurante, ¿qué representa S3?
6. ¿Qué librerías instalamos para conectar Django con S3?

---

---

---

## ✅ Respuestas

<br><br><br>

### 1. Porque plataformas como Railway **borran los archivos subidos al redesplegar**, así que las fotos desaparecerían. Además el disco del servidor es limitado y no se comparte bien entre varios servidores.

### 2. Un "bucket" (cubeta) es un **contenedor de archivos** en S3, con un nombre único global. Ahí dentro se guardan las imágenes, cada una con su propia URL.

### 3. Es un **interruptor**: si `USE_S3=false` las imágenes se guardan en el disco local (desarrollo); si `USE_S3=true` (con credenciales) se guardan en S3. Es útil porque **el código no cambia** — activar S3 es solo cambiar variables en `.env`, sin tocar el código.

### 4. Van SOLO en el archivo `.env` (que está en `.gitignore`). Nunca en el repositorio porque si se filtran a GitHub, cualquiera podría usar tu cuenta de AWS y **generarte costos** o acceder a tus datos.

### 5. S3 es la **galería de fotos colgada en la pared** (o un almacén externo de fotos): las imágenes viven ahí, separadas de la cocina (backend), y cualquiera con el link las ve.

### 6. `django-storages` (conecta Django con distintos backends de almacenamiento) y `boto3` (el SDK oficial de AWS para Python).

---

## 🎯 Tu puntaje
- 🟢 **5-6**: Listo para el deploy
- 🟡 **3-4**: Repasa lo fallado
- 🔴 **0-2**: Relee la clase 12

## 🏆 Habilidades de entrevista desbloqueadas
- ✅ "¿Cómo manejas la subida de archivos en tu app?"
- ✅ "¿Por qué no guardas archivos en el servidor de aplicación?"
- ✅ "¿Cómo mantienes tu código igual en desarrollo y producción?"

---

## ➡️ Siguiente
**FASE 8 — Deploy: publicar MenuPOS en internet (Railway + Vercel)**
