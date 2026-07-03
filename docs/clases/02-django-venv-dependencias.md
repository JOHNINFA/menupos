# 📖 Clase 02 — Django, venv y dependencias

> 🎯 **Objetivo**: Entender qué es Django (el framework), qué es un entorno virtual (venv), y cómo gestionamos las "librerías" del backend.
> ⏱️ **Tiempo**: 10 minutos
> 📚 **Pre-requisitos**: Clase [`01-arquitectura.md`](01-arquitectura.md)

---

## 🍳 Recordatorio rápido

Recuerda: **el backend es la cocina** del restaurante. En MenuPOS la cocina la vamos a construir con **Django**.

Pero antes de cocinar, necesitamos:
- 🔧 **Las herramientas** (Django, DRF) → "el equipamiento de la cocina"
- 📦 **Un lugar aislado** (venv) → "una cocina propia, no compartida"
- 📋 **Una lista de ingredientes** (requirements.txt) → "para que cualquier cocinero pueda replicar"

Esto es lo que vamos a aprender hoy.

---

## 🤔 Parte 1: ¿Qué es un framework?

### El problema
Imagina que tienes que construir un restaurante **desde cero**:
- ❌ Construir las paredes
- ❌ Instalar la plomería
- ❌ Comprar refrigeradores
- ❌ Diseñar el menú
- ❌ Contratar al personal
- ❌ Atender a los clientes

Te tomaría **años** antes de servir el primer plato.

### La solución: usar un local "pre-armado"
Un **framework** es como **alquilar un local de restaurante ya armado**:
- ✅ Paredes ya están
- ✅ Plomería ya funciona
- ✅ Refrigeradores ya instalados
- ✅ Solo te concentras en **cocinar y atender**

Eso es **Django** para los backends.

---

## 🍳 Parte 2: ¿Qué es Django?

**Django** = un framework de Python para construir aplicaciones web.

### Lo que Django te da "gratis" (sin que tú lo programes)
- 🔐 Sistema de autenticación (login, registro, sesiones)
- 🗄️ Conexión a bases de datos (PostgreSQL, MySQL, SQLite)
- 🛡️ Protección contra ataques comunes (SQL injection, CSRF, XSS)
- 📋 Administrador web automático (`/admin`)
- 🔧 Sistema de migraciones (cambiar la BD sin romper datos)
- 🌐 Manejo de URLs y peticiones HTTP

> 💡 Si tuvieras que programar todo eso a mano, te demorarías **meses**. Django te lo da en **minutos**.

### ¿Por qué Django y no otra cosa?

| Framework Python | Cuándo usarlo |
|---|---|
| **Django** | Proyectos completos (con BD, auth, admin) → **NUESTRO CASO** |
| Flask | APIs muy simples, microservicios |
| FastAPI | APIs muy rápidas, modernas, con tipos |

Para MenuPOS elegimos Django porque:
- ✅ Tiene admin web automático (útil para que el dueño del restaurante gestione productos)
- ✅ Sistema de autenticación robusto
- ✅ Es estable y muy usado en producción (Instagram, Spotify lo usaron)
- ✅ Comunidad enorme = fácil encontrar ayuda

---

## 🍽️ Parte 3: ¿Qué es DRF (Django REST Framework)?

Django solo, te da páginas web tradicionales (HTML completo).

Pero **nosotros queremos una API REST** (recuerda la Clase 01) que devuelva JSON para que React lo consuma.

**DRF** = una **extensión** que se le pone a Django para crear APIs REST fácilmente.

### Analogía
- 🍳 Django = la cocina completa
- 🧑‍💼 DRF = el sistema de meseros entrenados para comunicarse en JSON

Sin DRF tendrías que escribir manualmente cada respuesta JSON, validación, etc.
Con DRF lo haces en pocas líneas.

---

## 📦 Parte 4: ¿Qué es un entorno virtual (venv)?

### El problema
Tu computador tiene Python instalado **globalmente** (en todo el sistema).

Si instalas Django para MenuPOS:
- ❌ Se instala en TODO el sistema
- ❌ Si otro proyecto necesita una versión DIFERENTE de Django, **conflicto**
- ❌ Si quieres borrar dependencias, afecta a todos los proyectos

### La solución: una "burbuja" por proyecto

Un **venv** (virtual environment) crea una **burbuja aislada** dentro de tu proyecto:

```
🌍 Tu computador (Python global)
│
├── 🫧 proyecto-A (venv) → Django 4
├── 🫧 proyecto-B (venv) → Django 5
└── 🫧 MenuPOS  (venv) → Django 5 + DRF + JWT...
```

Cada burbuja tiene SUS propias librerías, sin afectar a las demás.

### Analogía
- 🌍 Python global = el agua del acueducto público de tu casa
- 🫧 venv = una **botella de agua personal** para cada proyecto

Si una botella se contamina, no afecta al resto.

### Cómo se usa (te lo voy a hacer en el siguiente paso)

```bash
python -m venv venv         # Crear la burbuja
source venv/bin/activate    # Entrar a la burbuja
pip install django          # Instalar SOLO en la burbuja
deactivate                  # Salir de la burbuja
```

> 💡 Cuando entras al venv, verás `(venv)` al inicio de tu terminal. Eso indica "estoy dentro de la burbuja".

---

## 📋 Parte 5: ¿Qué es pip y requirements.txt?

### pip
**pip** = el "instalador de librerías" de Python.
Es como un *App Store* pero para librerías de Python.

```bash
pip install django           # Instala la última versión
pip install django==5.1.3    # Instala UNA versión específica
pip uninstall django         # Desinstala
pip list                     # Ver qué hay instalado
```

### requirements.txt
**requirements.txt** = un archivo de TEXTO con la **lista de todas las librerías** que tu proyecto necesita.

Ejemplo para MenuPOS:
```txt
Django==5.1.3
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
psycopg2-binary==2.9.10
```

### ¿Por qué es importante?
**Sin** `requirements.txt`:
- 🚨 Si otro dev clona tu proyecto, no sabe qué instalar
- 🚨 En producción puede instalar versiones diferentes y romper todo

**Con** `requirements.txt`:
- ✅ Cualquiera hace `pip install -r requirements.txt` y tiene EXACTAMENTE las mismas librerías
- ✅ En producción se instala lo mismo que en tu PC
- ✅ Es como una **receta exacta** de la cocina

### Analogía completa
- 📋 requirements.txt = **receta de cocina** con cantidades exactas
- 🫧 venv = **cocina personal aislada** para no contaminar otras
- 📦 pip = el **mercado** donde compras los ingredientes
- 🍳 Django/DRF = los **electrodomésticos** principales de la cocina

---

## 🎬 Cómo se ve TODO junto en MenuPOS

```
menupos/backend/
│
├── 🫧 venv/                  ← Burbuja aislada (NO sube a Git)
│   └── (Django, DRF, etc.)
│
├── 📋 requirements.txt        ← Receta de qué instalar (SÍ sube a Git)
├── 🐍 manage.py               ← Script principal de Django
├── 📁 menupos_config/         ← Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── 📁 apps/                   ← Nuestras "secciones" del restaurante
    ├── users/
    ├── menu/
    └── sales/
```

> 💡 `venv/` NO se sube a Git (está en `.gitignore`). Lo que sí sube es `requirements.txt` para que otros puedan recrear la burbuja con `pip install -r requirements.txt`.

---

## 🧠 Quiz rápido

1. ¿Qué es un framework, en una frase? un sistem prediseñado
2. ¿Por qué usamos Django y no Flask para MenuPOS? djagno es un framework que trae admin automatico y sistema de autenticacion robusto
3. ¿Para qué sirve un entorno virtual (venv)? para manter un entorno aislado
4. ¿Cuál es la diferencia entre `pip install django` y `pip install -r requirements.txt`? pip install django → instala UNA librería (django)
pip install -r requirements.txt → instala TODAS las de la lista, con sus versiones exactas
5. ¿Por qué NO subimos la carpeta `venv/` a Git? la carpeta venv es un entorno local Pesa mucho (cientos de MB)
Se regenera fácil con pip install -r requirements.txt Subirla sería desperdiciar espacio, cuando cualquiera puede recrearla desde el requirements.txt

> 📝 Respuestas al final del quiz de FASE 2.

---

## ➡️ Qué sigue

Ahora que ya entiendes los conceptos, vamos a:

1. ✅ Crear el `venv` dentro de `backend/`
2. ✅ Crear `requirements.txt` con las librerías que MenuPOS necesita
3. ✅ Hacer `pip install -r requirements.txt`
4. ✅ Generar el proyecto Django con `django-admin startproject`
5. ✅ Verificar que arranca con `python manage.py runserver`

¡Empezamos!

---

## 🔗 Referencias

- [Documentación oficial Django (español)](https://docs.djangoproject.com/es/)
- [Documentación oficial DRF (inglés)](https://www.django-rest-framework.org/)
- [Python venv tutorial](https://docs.python.org/es/3/library/venv.html)
