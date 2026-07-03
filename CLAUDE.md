# Contexto para Claude — MenuPOS

> **IMPORTANTE**: Lee este archivo COMPLETO antes de responderle a John por primera vez.
> Si vienes de otra sesión o computador, esto te pondrá al día rápidamente.

---

## 👤 Quién es el usuario

- **Nombre**: John Infante (`JOHNINFA`)
- **Idioma**: Español (siempre, sin excepciones)
- **Nivel**: Principiante — necesita explicaciones paso a paso, sin asumir nada
- **Curso actual**: Inmersión Agentes de IA (Oracle Next Education + Alura)
- **Objetivo**: Construir portafolio para aplicar a Workana como freelancer

Para perfil completo ver: `github.com/JOHNINFA/mi-roadmap-dev/PERFIL.md`

---

## 🎯 Qué es MenuPOS

**Sistema POS (punto de venta) para restaurantes pequeños.** Proyecto estrella del portafolio de John.

### MVP (lo mínimo a construir)
- Login con JWT
- Gestión de menú: categorías + productos + imágenes
- Realizar ventas (carrito → cobro → ticket)
- Historial de ventas
- Dashboard básico (ventas del día, productos más vendidos)

### Stack confirmado
```
Backend:    Django 5 + Django REST Framework + PostgreSQL
Frontend:   React + Vite + Tailwind CSS + shadcn/ui
Storage:    AWS S3 (imágenes del menú)
Auth:       JWT (djangorestframework-simplejwt)
Deploy:     Railway (backend + DB) + Vercel (frontend)
Lenguaje:   Python 3.10+ (backend), TypeScript (frontend)
```

---

## 🎓 ESTILO DE ENSEÑANZA — OBLIGATORIO

John eligió el **enfoque "B equilibrado"** para aprender. Esto es **innegociable**:

### Las 3 capas que SIEMPRE debes mantener

1. **CAPA 1 — Código comentado**: cada archivo de código debe tener comentarios en español que expliquen **QUÉ** hace y **POR QUÉ** se hace así (no solo qué hace cada línea — eso ya lo dice el código).

2. **CAPA 2 — Mini-clases por concepto**: ANTES de usar un concepto nuevo (Modelo, Serializer, ViewSet, JWT, S3, etc.), crear o actualizar su mini-clase en `docs/clases/NN-nombre.md`. Formato:
   - 🤔 El problema (qué necesidad resuelve)
   - 🎬 Analogía (usar metáfora del restaurante)
   - 💻 Ejemplo real (código mínimo)
   - 🧠 Quiz rápido (3-5 preguntas)
   - 🔗 Link a documentación oficial

3. **CAPA 3 — Diagramas Mermaid** en `docs/diagramas/`: para arquitectura, modelos (ER), flujos de auth/petición. Mermaid renderiza automático en GitHub.

### Quizzes al final de cada fase
3-5 preguntas en `docs/quizzes/fase-NN.md` para que John responda y verifique aprendizaje.

### Storytelling — Metáfora del restaurante
Usar SIEMPRE estas analogías porque MenuPOS ES un sistema de restaurante:

| Concepto técnico | Analogía restaurante |
|---|---|
| Modelo (Django) | Receta guardada en la cocina |
| Base de datos | El refrigerador / despensa |
| Serializer | Mesero traductor |
| ViewSet | Comedor donde se atiende |
| URL | Puerta del restaurante |
| Migración | Remodelación del local |
| JWT | Pulsera VIP del cliente |
| API REST | Sistema de comandas |
| Frontend | El restaurante físico que ve el cliente |
| Backend | La cocina y administración |

---

## 📐 Reglas innegociables al trabajar con John

1. **Español siempre**, sin excepciones
2. **NO avanzar de fase si no ha confirmado que entendió** — preguntar activamente
3. **NO instalar dependencias sin confirmar primero** y verificar disco (`df -h /`)
4. **Disco limitado**: el PC tiene 71 GB y suele estar al 100%. Vigilar SIEMPRE
5. **NO borrar `node_modules` de ningún proyecto sin confirmación** (él usa `npx`)
6. **Cuando creas código nuevo, explica QUÉ y POR QUÉ**, nunca solo el QUÉ
7. **Una cosa a la vez**: no abrumarlo con 5 conceptos en un mensaje
8. **Si John se ve frustrado o perdido**, parar y aclarar

---

## 📂 Estructura del repo

```
menupos/
├── CLAUDE.md              ← Este archivo (lo lee Claude)
├── README.md              ← Vista pública para visitantes/Workana
├── .gitignore             ← Protege disco (ignora node_modules, venv, .env)
├── .env.example           ← Plantilla de variables de entorno
│
├── backend/               ← Django + DRF (config, apps users/menu/sales)
│   └── requirements.txt   ← Dependencias Python
│
├── frontend/              ← React + Vite + Tailwind
│   ├── src/api/           ← Cliente Axios
│   ├── src/context/       ← AuthContext (sesión de usuario)
│   ├── src/components/    ← Header, ProductoCard, RutaProtegida
│   ├── src/pages/         ← Login, Pos, Dashboard
│   └── package.json
│
└── docs/                  ← MATERIAL DE APRENDIZAJE
    ├── clases/            ← Mini-clases por concepto
    │   ├── 00-bienvenida.md
    │   ├── 01-arquitectura.md
    │   └── ...
    ├── diagramas/         ← Diagramas Mermaid
    │   ├── 01-vision-general.md
    │   └── ...
    └── quizzes/           ← Quizzes al final de cada fase
        ├── fase-01.md
        └── ...
```

---

## 📅 Estado actual

**Fase actual**: FASE 6 completada + rondas 6c/6d/6e de refinamiento del flujo de negocio (a partir de feedback real del usuario probando la app)
**Última actualización**: 2026-07-02
**Próxima fase**: FASE 7 — Imágenes de productos en AWS S3

### Refinamientos post-FASE 6 (rondas 6c/6d/6e)
Surgieron de que el usuario probó la app y notó que no reflejaba un restaurante real:
- **6c**: Gestión de usuarios (admin crea meseros/admins vía `/api/usuarios/`, UsuarioCreateSerializer con password write_only + create_user para hashear). Comanda imprimible (`/comanda/:id`, usa window.print + print:hidden de Tailwind). Botones de estado en Dashboard.
- **6d**: Campo `tipo` en Venta (mesa/llevar). `mesa` ahora nullable (para llevar no tiene). **Cuenta abierta por mesa**: si una mesa con cuenta abierta pide más, VentaSerializer.create() SUMA los productos a la venta existente en vez de crear otra (filtra por estado en ESTADOS_ABIERTOS). Selector Mesa/Para llevar en el POS.
- **6e**: Flujo de 4 estados: **pedido → entregado → pagado** (+ cancelado). Reemplazó el pendiente/pagada/cancelada anterior. Migración de DATOS (0005) convirtió los estados viejos sin perder registros. El mesero marca `entregado`; solo admin marca `pagado`/`cancelado` (chequeo fino dentro de la acción `marcar_estado`, no solo en la permission class). Al agregar productos a una cuenta abierta, vuelve a `pedido`.
- Nuevas páginas frontend: AdminUsuarios, ComandaPrint. Nuevo componente RutaAdmin.
- Bugs reales encontrados y corregidos en estas rondas (documentar en quiz): permiso de lectura sin auth; `disponible` quedaba False por defecto en multipart; `marcar_estado` compartía verbo POST con create (se reforzó usando view.action).

### Decisiones tomadas
- Usuario tiene conocimiento básico de programación → se salta lectura previa de mini-clases, prefiere que Claude construya de corrido y lee la documentación después/en paralelo. Seguir comentando código y creando mini-clases igual, pero sin pausar para confirmar entendimiento en cada paso salvo que el usuario lo pida.
- Base de datos: SQLite en desarrollo (no PostgreSQL/Docker todavía) para avanzar rápido. Migrar a PostgreSQL en fase dedicada futura.
- `AUTH_USER_MODEL = 'users.Usuario'` configurado desde FASE 4 (extiende AbstractUser + campo `rol`: admin/mesero). Requirió resetear db.sqlite3 y migraciones porque se agregó después del primer migrate de FASE 2 (sin pérdida real, BD estaba vacía).
- Superusuario de prueba creado localmente (username `admin`, rol admin) — SOLO para desarrollo local, credenciales NO están en ningún archivo del repo, no usar en producción. También existe `mesero1` de prueba (rol mesero) para probar permisos.
- Datos de prueba sembrados vía shell/API: Categoria, Producto, y un par de Ventas con detalles (útiles para probar el frontend en FASE 6)
- on_delete elegidos deliberadamente: PROTECT en Producto→Categoria, Venta→Usuario y DetalleVenta→Producto (evitar romper historial); CASCADE solo en DetalleVenta→Venta
- Permiso `EsAdminOSoloLectura` (users/permissions.py): cualquier autenticado puede leer menú, solo admin puede escribir. Bug real encontrado y corregido durante pruebas: la versión inicial permitía LEER sin estar logueado (no validaba is_authenticated antes de chequear SAFE_METHODS) — documentado en clases/06 y quiz de fase-05 como caso real de aprendizaje.
- VentaSerializer.create() calcula `precio_unitario` desde `producto.precio` en el servidor (nunca confía en un precio que mande el frontend) y calcula el `total` sumando los detalles.
- Endpoints: `/api/categorias/`, `/api/productos/`, `/api/ventas/` (ModelViewSets vía router), `/api/auth/login/` y `/api/auth/refresh/` (JWT), `/api/users/me/` (info del usuario logueado)

### Plan por fases
- ✅ FASE 1: Estructura + docs base + mini-clases iniciales
- ✅ FASE 2: Setup Django backend (venv, Django+DRF+JWT+CORS instalados, proyecto `config` + apps `users`/`menu`/`sales` creadas, settings.py comentado, migrate y check OK)
- ✅ FASE 3: Setup React frontend (Vite + React 19 + TypeScript + Tailwind v4 + react-router-dom + axios instalados, App.tsx de bienvenida, build verificado sin errores)
- ✅ FASE 4: Modelos (Usuario con rol, Categoria, Producto, Venta, DetalleVenta) + admin.py registrados + migraciones + verificación vía shell
- ✅ FASE 5: API REST (Serializers anidados, ViewSets, Router, permisos por rol, JWT login/refresh, endpoint /me) — probado end-to-end con curl
- ✅ FASE 6: Frontend conectado (AuthContext con localStorage, RutaProtegida, cliente Axios con interceptor JWT, páginas Login/Pos/Dashboard, componentes Header/ProductoCard) — probado con backend+frontend corriendo juntos, CORS verificado
- ✅ 6c/6d/6e: Refinamiento del flujo de negocio (gestión usuarios, comanda imprimible, tipo mesa/llevar, cuenta abierta por mesa, flujo de 4 estados con permisos por rol) — todo probado con curl y en navegador
- ⏳ FASE 7: Imágenes en AWS S3
- ⏳ FASE 8: Deploy (Railway + Vercel)
- ⏳ FASE 9: README final + screenshots + GIF demo

### Notas técnicas de FASE 6
- Token JWT guardado en `localStorage` (limitación XSS conocida y documentada, aceptable para proyecto de portafolio)
- `AuthContext` verifica sesión existente vía `/api/users/me/` al montar la app
- El carrito del POS solo manda `{producto, cantidad}` a `/api/ventas/` — el precio y total se calculan en el backend (nunca se confía en el frontend para dinero)

---

## 💡 Si eres una sesión nueva de Claude

Antes de responderle a John:
1. ✅ Lee este archivo completo (acabas de hacerlo)
2. ✅ Lee el último `docs/quizzes/` para ver qué ya aprendió
3. ✅ Revisa los archivos en `docs/clases/` para conocer las metáforas y conceptos ya vistos
4. ✅ Pregúntale: "¿En qué fase quieres retomar, John?"
5. ✅ Verifica espacio en disco antes de cualquier instalación
