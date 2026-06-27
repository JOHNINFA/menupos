# 🍔 MenuPOS

> Sistema POS (Punto de Venta) para restaurantes pequeños.
> Proyecto de portafolio de **John Infante** ([@JOHNINFA](https://github.com/JOHNINFA)).

---

## 📍 Estado del proyecto

🚧 **En desarrollo activo** — Fase 1: Estructura y documentación.

Última actualización: **2026-06-26**

---

## 🎯 Qué hace

MenuPOS permite a un restaurante pequeño:

- 🔐 Login seguro para meseros y administradores
- 🍽️ Gestionar el menú (categorías, productos, imágenes)
- 💳 Realizar ventas con interfaz tipo POS (toca el producto → arma el pedido → cobra)
- 📜 Ver historial de ventas
- 📊 Dashboard con métricas (ventas del día, productos más vendidos)
- 🖼️ Subir imágenes de productos (almacenadas en AWS S3)

---

## 🛠️ Stack técnico

| Capa | Tecnología |
|---|---|
| **Backend** | Django 5 + Django REST Framework |
| **Base de datos** | PostgreSQL |
| **Autenticación** | JWT (`djangorestframework-simplejwt`) |
| **Frontend** | React + Vite + TypeScript |
| **Estilos** | Tailwind CSS + shadcn/ui |
| **Almacenamiento** | AWS S3 (imágenes) |
| **Deploy backend** | Railway |
| **Deploy frontend** | Vercel |

---

## 📚 Aprendizaje guiado incluido

Este repo NO es solo código. Incluye material de aprendizaje completo en [`docs/`](docs/):

- 📖 **Mini-clases** por concepto en [`docs/clases/`](docs/clases/) — explicaciones simples con analogías
- 📊 **Diagramas Mermaid** en [`docs/diagramas/`](docs/diagramas/) — visualización de arquitectura y flujos
- 🧠 **Quizzes** en [`docs/quizzes/`](docs/quizzes/) — para reforzar lo aprendido

> 💡 Si estás aprendiendo Django + React, empieza por [`docs/clases/00-bienvenida.md`](docs/clases/00-bienvenida.md)

---

## 🚀 Cómo ejecutar (próximamente)

Esta sección se llenará cuando el backend y frontend estén configurados.

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

# Frontend (en otra terminal)
cd frontend
npm install
npm run dev
```

---

## 📂 Estructura del proyecto

```
menupos/
├── backend/        ← Django + DRF
├── frontend/       ← React + Vite
├── docs/           ← Material de aprendizaje
│   ├── clases/
│   ├── diagramas/
│   └── quizzes/
├── README.md       ← Este archivo
├── CLAUDE.md       ← Contexto para Claude AI
└── .env.example    ← Plantilla de variables
```

---

## 👨‍💻 Autor

**John Infante**
📧 johningonzalez2021@gmail.com
🐙 [github.com/JOHNINFA](https://github.com/JOHNINFA)
🗺️ [Mi roadmap dev](https://github.com/JOHNINFA/mi-roadmap-dev)

---

## 📄 Licencia

Proyecto educativo de portafolio. Libre uso con atribución.
