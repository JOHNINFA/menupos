# 🧠 Quiz FASE 2 — Django, venv y backend inicial

> 📚 **Clase que cubre**: [`02-django-venv-dependencias.md`](../clases/02-django-venv-dependencias.md)
> 🎯 **Objetivo**: Verificar que entiendes cómo se armó el esqueleto del backend.

---

## 📝 Preguntas

1. ¿Qué es un framework, en una frase?
2. ¿Por qué usamos Django y no Flask para MenuPOS?
3. ¿Para qué sirve un entorno virtual (venv)?
4. ¿Cuál es la diferencia entre `pip install django` y `pip install -r requirements.txt`?
5. ¿Por qué NO subimos la carpeta `venv/` a Git?
6. ¿Por qué decidimos usar SQLite en vez de PostgreSQL en esta fase?
7. ¿Qué hace el comando `python manage.py migrate`?
8. ¿Para qué sirve `django-cors-headers` en nuestro proyecto?
9. ¿Qué representa `SIMPLE_JWT` en `settings.py`, con la metáfora del restaurante?
10. ¿Por qué el `SECRET_KEY` va en `.env` y no directo en `settings.py`?

---

---

---

## ✅ Respuestas

<br><br><br>

### 1. Un framework es un **"kit de herramientas pre-armado"** para no construir todo desde cero.

### 2. Porque Django trae admin web automático, sistema de autenticación robusto, y es ideal para proyectos completos con base de datos — justo lo que necesita un POS. Flask es mejor para APIs muy simples/microservicios.

### 3. Un venv crea una **burbuja aislada** de librerías para el proyecto, evitando conflictos entre versiones de diferentes proyectos en la misma máquina.

### 4. `pip install django` instala **una** librería específica. `pip install -r requirements.txt` instala **TODAS** las librerías listadas en el archivo, con las versiones exactas — así cualquiera puede recrear el mismo entorno.

### 5. Porque `venv/` puede pesar cientos de MB y se **regenera fácilmente** con `pip install -r requirements.txt`. Subirlo a Git sería un desperdicio de espacio y ancho de banda.

### 6. Para avanzar rápido sin depender de Docker Compose (que aún no configuramos). SQLite es un solo archivo, cero configuración. Migraremos a PostgreSQL en una fase dedicada, porque en producción real se necesita un motor de BD más robusto.

### 7. Aplica los **cambios pendientes** a la base de datos: crea las tablas que Django necesita (usuarios, sesiones, permisos, etc.) basándose en las migraciones generadas.

### 8. Permite que el **frontend en React** (que corre en otro puerto/dominio, ej: `localhost:5173`) pueda hacer peticiones a la **API en Django** (`localhost:8000`) sin que el navegador las bloquee por seguridad (política de mismo origen).

### 9. `SIMPLE_JWT` es la configuración de la **"pulsera VIP"**: define cuánto dura el access token (la pulsera activa) y cuánto dura el refresh token (el comprobante para pedir una pulsera nueva sin hacer fila de nuevo).

### 10. Porque `SECRET_KEY` es información **sensible** — si se sube a un repo público, cualquiera podría falsificar sesiones o tokens. Guardarlo en `.env` (que está en `.gitignore`) evita que quede expuesto en GitHub.

---

## 🎯 Tu puntaje

- 🟢 **8-10**: Perfecto, sigues a FASE 3
- 🟡 **5-7**: Bien, repasa lo que fallaste
- 🔴 **0-4**: Relee la clase 02 con calma

---

## 🏆 Habilidades de entrevista desbloqueadas

- ✅ "¿Por qué elegiste Django para tu backend?"
- ✅ "¿Cómo manejas los secretos/variables de entorno?"
- ✅ "¿Qué es CORS y por qué lo necesitaste configurar?"
- ✅ "¿Cómo funcionan las migraciones en Django?"

---

## ➡️ Siguiente

**FASE 3 — Setup React + Vite + Tailwind (frontend)**
