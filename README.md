# 🍔 MenuPOS — Sistema de Punto de Venta para Restaurantes

Sistema **full-stack** de punto de venta (POS) para restaurantes pequeños: los meseros toman pedidos por mesa o para llevar, la cocina recibe la comanda, y el cajero cobra desde un panel de administración. Con roles, autenticación segura y flujo de pedidos real.

**🌐 Demo en vivo: [menupos.vercel.app](https://menupos.vercel.app)**

> 🔑 Credenciales de prueba disponibles a solicitud (por seguridad no se publican).

<!-- Reemplaza esta línea por una captura del POS cuando la tengas:
![MenuPOS - Punto de Venta](docs/screenshots/pos.png) -->

---

## ✨ Características

- 🔐 **Autenticación por roles** (JWT): administrador y mesero, cada uno con permisos distintos
- 🍽️ **Toma de pedidos** por mesa o para llevar, con carrito interactivo
- 🧾 **Cuenta abierta por mesa**: si una mesa pide más, se suma a su cuenta en curso
- 🔄 **Flujo de pedido real**: Pedido → Entregado → Pagado (o Cancelado)
- 🖨️ **Comanda imprimible** para llevar a cocina
- 👥 **Gestión de usuarios**: el admin crea meseros y otros administradores
- 📋 **Gestión de menú**: categorías, productos, precios, disponibilidad e imágenes
- 📊 **Dashboard** con pedidos pendientes y total cobrado

---

## 🛠️ Stack técnico

| Capa | Tecnología |
|---|---|
| **Backend** | Django 5 + Django REST Framework |
| **Base de datos** | PostgreSQL (producción) / SQLite (desarrollo) |
| **Autenticación** | JWT (`djangorestframework-simplejwt`) |
| **Frontend** | React 19 + Vite + TypeScript |
| **Estilos** | Tailwind CSS v4 |
| **Peticiones HTTP** | `fetch` nativo (sin dependencias externas) |
| **Imágenes** | Cloudinary / AWS S3 (configurable por variable de entorno) |
| **Deploy backend** | Render |
| **Deploy frontend** | Vercel |

---

## 🏗️ Arquitectura

```
┌─────────────────┐      HTTPS / JSON       ┌──────────────────┐
│  Frontend React │  ───────────────────▶   │  API REST Django │
│    (Vercel)     │  ◀───────────────────   │     (Render)     │
└─────────────────┘   JWT en cada petición  └────────┬─────────┘
                                                      │
                                             ┌────────▼─────────┐
                                             │   PostgreSQL     │
                                             │    (Render)      │
                                             └──────────────────┘
```

📊 Diagramas detallados (arquitectura, modelo de datos, flujo de autenticación) en [`docs/diagramas/`](docs/diagramas/).

---

## 💡 Decisiones técnicas destacadas

Cosas que hacen este proyecto más que un CRUD básico:

- **Seguridad del dinero en el servidor**: el precio y el total de cada venta se calculan en el backend tomando el precio real del producto — nunca se confía en lo que envía el frontend (evita manipulación de precios).
- **Permisos por acción, no solo por endpoint**: el mesero puede marcar un pedido como "entregado", pero solo el admin puede "cobrar" o "cancelar".
- **Máquina de estados** para el ciclo de vida del pedido, con transiciones controladas.
- **Cuenta abierta por mesa**: lógica que agrupa varios pedidos de la misma mesa en una sola cuenta mientras no esté pagada.
- **Almacenamiento de imágenes intercambiable**: un interruptor por variable de entorno permite usar disco local, Cloudinary o AWS S3 sin cambiar el código.

---

## 🚀 Cómo ejecutar en local

### Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate          # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # crea tu usuario admin
python manage.py runserver        # http://localhost:8000
```

### Frontend (React)

```bash
cd frontend
npm install
npm run dev                       # http://localhost:5173
```

> El frontend usa `http://localhost:8000/api` por defecto. Para apuntar a otro backend, define `VITE_API_URL` en un archivo `.env.local`.

---

## 📂 Estructura del proyecto

```
menupos/
├── backend/            ← Django + DRF
│   ├── config/         ← Configuración (settings, urls)
│   ├── users/          ← Usuarios y permisos por rol
│   ├── menu/           ← Categorías y productos
│   └── sales/          ← Ventas y detalle de venta
├── frontend/           ← React + Vite + TypeScript
│   └── src/
│       ├── api/        ← Cliente HTTP (fetch)
│       ├── context/    ← Contexto de autenticación
│       ├── components/ ← Componentes reutilizables
│       └── pages/      ← Login, POS, Dashboard, Gestión
├── docs/               ← Material de aprendizaje (clases, diagramas, quizzes)
└── render.yaml         ← Configuración de despliegue
```

---

## 📚 Bonus: material de aprendizaje

Este repo incluye documentación educativa en [`docs/`](docs/): mini-clases por concepto, diagramas Mermaid y quizzes. Útil si estás aprendiendo Django + React. Empieza por [`docs/clases/00-bienvenida.md`](docs/clases/00-bienvenida.md).

---

## 👨‍💻 Autor

**John Infante** — Desarrollador Full-Stack

📧 johningonzalez2021@gmail.com
🐙 [github.com/JOHNINFA](https://github.com/JOHNINFA)

---

## 📄 Licencia

Proyecto de portafolio. Libre uso con atribución.
