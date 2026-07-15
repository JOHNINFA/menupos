# 🍔 MenuPOS — Sistema de Punto de Venta para Restaurantes

**Desarrollador:** John Infante  
**Email:** johningonzalez2021@gmail.com  
**GitHub:** [github.com/JOHNINFA](https://github.com/JOHNINFA)  
**Demo en vivo:** [menupos.vercel.app](https://menupos.vercel.app)

---

## 📋 Descripción del Proyecto

MenuPOS es un **sistema completo de punto de venta (POS)** diseñado específicamente para restaurantes pequeños y medianos. Permite a los meseros tomar pedidos por mesa o para llevar, gestionar cuentas abiertas, y al administrador controlar todo el menú, usuarios y ventas desde un dashboard centralizado.

### ✨ Características Principales

#### 🔐 Autenticación y Roles
- Sistema de login seguro con JWT (JSON Web Tokens)
- Dos roles claramente diferenciados:
  - **Administrador**: control total del sistema
  - **Mesero**: solo toma pedidos y marca entregas
- Permisos granulares por acción (no solo por endpoint)

#### 🍽️ Gestión de Pedidos
- Toma de pedidos por **mesa** o **para llevar**
- **Cuenta abierta por mesa**: si una mesa pide más, se suma a su cuenta actual
- Carrito interactivo con cálculo automático de totales
- Flujo de 4 estados: **Pedido → Entregado → Pagado** (+ Cancelado)
- El mesero marca "entregado", solo el admin puede "cobrar" o "cancelar"

#### 🖨️ Comanda Imprimible
- Comanda para cocina con todos los detalles del pedido
- Información clara: mesa, productos, cantidades, hora
- Función de impresión directa desde el navegador

#### 👥 Gestión de Usuarios
- El administrador crea y gestiona usuarios (meseros y otros admins)
- Contraseñas encriptadas con hash seguro (nunca en texto plano)
- Endpoint dedicado: `/api/usuarios/`

#### 📋 Gestión Completa de Menú
- Categorías organizadas (Entradas, Platos Fuertes, Bebidas, Postres)
- Productos con: nombre, descripción, precio, imagen, disponibilidad
- Control de disponibilidad en tiempo real
- Subida de imágenes (soporte para múltiples servicios de almacenamiento)

#### 📊 Dashboard Administrativo
- Vista de pedidos pendientes
- Total vendido del día
- Historial completo de ventas
- Acciones rápidas sobre pedidos (ver comanda, cambiar estado)

---

## 🛠️ Stack Tecnológico

### Backend
- **Framework:** Django 5 + Django REST Framework
- **Base de datos:** PostgreSQL (producción) / SQLite (desarrollo)
- **Autenticación:** JWT con `djangorestframework-simplejwt`
- **Servidor:** Gunicorn
- **Almacenamiento:** django-storages (soporte para AWS S3, Cloudinary, Azure Blob)

### Frontend
- **Framework:** React 19 + TypeScript
- **Build:** Vite 8
- **Estilos:** Tailwind CSS v4
- **Routing:** React Router DOM 7
- **HTTP Client:** Fetch API nativo (cero dependencias externas)

### DevOps
- **Deploy Backend:** Render (con PostgreSQL incluido)
- **Deploy Frontend:** Vercel
- **CI/CD:** Deploy automático desde GitHub
- **Configuración:** Blueprint (render.yaml) para deploy reproducible

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

### Principios de Diseño

1. **Seguridad primero**: 
   - Precios y totales calculados siempre en el servidor
   - Nunca se confía en datos del cliente para operaciones financieras
   - Tokens JWT con tiempo de expiración controlado

2. **Permisos granulares**:
   - Control fino por acción, no solo por endpoint
   - Verificación en dos niveles: permission classes + lógica de negocio

3. **Máquina de estados**:
   - Transiciones controladas entre estados de pedido
   - Previene estados inválidos o inconsistencias

4. **Separación de responsabilidades**:
   - Frontend solo presenta datos y captura intención del usuario
   - Backend contiene toda la lógica de negocio

---

## 📂 Estructura del Proyecto

```
menupos/
├── backend/                  ← Django + DRF
│   ├── config/               ← Configuración (settings, urls)
│   ├── users/                ← Usuarios y autenticación
│   │   ├── models.py         ← Usuario con rol (admin/mesero)
│   │   ├── serializers.py    ← Validación y transformación
│   │   ├── views.py          ← Endpoints de usuarios
│   │   └── permissions.py    ← Permisos personalizados
│   ├── menu/                 ← Categorías y productos
│   │   ├── models.py         ← Categoria, Producto
│   │   ├── serializers.py    ← Anidación: Productos con Categoría
│   │   └── views.py          ← CRUD completo
│   └── sales/                ← Ventas y detalles
│       ├── models.py         ← Venta, DetalleVenta
│       ├── serializers.py    ← Cálculo de precios en servidor
│       └── views.py          ← Lógica de cuenta abierta + estados
│
├── frontend/                 ← React + TypeScript
│   └── src/
│       ├── api/              ← Cliente HTTP con interceptor JWT
│       ├── context/          ← AuthContext (sesión global)
│       ├── components/       ← Componentes reutilizables
│       │   ├── Header.tsx    ← Navegación con datos del usuario
│       │   ├── ProductoCard.tsx ← Card de producto con imagen
│       │   ├── RutaProtegida.tsx ← HOC para rutas privadas
│       │   └── RutaAdmin.tsx ← HOC solo para admins
│       └── pages/            ← Páginas principales
│           ├── Login.tsx     ← Autenticación
│           ├── Pos.tsx       ← Punto de venta (carrito)
│           ├── Dashboard.tsx ← Vista de ventas
│           ├── AdminMenu.tsx ← Gestión de productos
│           ├── AdminUsuarios.tsx ← Gestión de usuarios
│           └── ComandaPrint.tsx ← Comanda imprimible
│
└── docs/                     ← Documentación educativa
    ├── clases/               ← Mini-clases por concepto
    ├── diagramas/            ← Diagramas Mermaid (arquitectura, ER)
    └── quizzes/              ← Evaluaciones de aprendizaje
```

---

## 🎯 Decisiones Técnicas Destacadas

### 1. Cálculo de precios en el servidor
**Problema:** Un cliente malicioso podría modificar el precio en el navegador.  
**Solución:** El frontend solo envía `{producto_id, cantidad}`. El backend consulta el precio actual de la BD y calcula el total.

```python
# VentaSerializer.create()
precio_unitario = detalle['producto'].precio  # Del servidor, no del cliente
subtotal = precio_unitario * cantidad
```

### 2. Cuenta abierta por mesa
**Problema:** En un restaurante real, una mesa puede pedir varias veces antes de pagar.  
**Solución:** Al crear una venta, si existe una cuenta abierta para esa mesa, se agregan los productos a la venta existente en vez de crear una nueva.

```python
if tipo == 'mesa' and mesa:
    venta_abierta = Venta.objects.filter(
        mesa=mesa,
        estado__in=ESTADOS_ABIERTOS
    ).first()
    if venta_abierta:
        # Agregar a la venta existente
        for detalle in detalles_validados:
            DetalleVenta.objects.create(venta=venta_abierta, ...)
        venta_abierta.estado = 'pedido'
        venta_abierta.save()
        return venta_abierta
```

### 3. Permisos por acción
**Problema:** Un mesero debería poder marcar "entregado" pero no "pagado".  
**Solución:** Dentro de la acción `marcar_estado`, verificamos el rol antes de permitir ciertas transiciones.

```python
@action(detail=True, methods=['post'])
def marcar_estado(self, request, pk=None):
    nuevo_estado = request.data.get('estado')
    
    # Solo admin puede marcar como pagado o cancelado
    if nuevo_estado in ['pagado', 'cancelado']:
        if request.user.rol != 'admin':
            return Response({'error': 'Solo admin puede realizar esta acción'}, 
                          status=403)
```

### 4. Almacenamiento intercambiable
**Problema:** En desarrollo usamos disco local, en producción necesitamos almacenamiento permanente.  
**Solución:** Interruptor `USE_S3` en settings.py + django-storages permite cambiar entre local/S3/Cloudinary/Azure sin tocar código.

```python
if USE_S3:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🔒 Seguridad

- **Contraseñas hasheadas:** Django usa PBKDF2 por defecto
- **JWT con expiración:** Access token de 60 min, refresh de 7 días
- **CORS configurado:** Solo el frontend autorizado puede llamar a la API
- **SQL injection:** Protegido por ORM de Django
- **XSS:** React escapa por defecto, sanitización en inputs
- **CSRF:** No aplica en API REST con JWT (no usa cookies de sesión)
- **Variables de entorno:** Secretos nunca en código, siempre en `.env` (excluido de Git)

---

## 📊 Modelo de Datos

### Usuario
- `username` (único)
- `password` (hash)
- `rol` (admin/mesero)
- `email`, `first_name`, `last_name`

### Categoria
- `nombre`

### Producto
- `nombre`
- `descripcion`
- `precio` (Decimal)
- `imagen` (URL o archivo)
- `disponible` (Boolean)
- `categoria` (FK → Categoria, PROTECT)

### Venta
- `usuario` (FK → Usuario, PROTECT)
- `tipo` ('mesa' / 'llevar')
- `mesa` (nullable)
- `estado` ('pedido' / 'entregado' / 'pagado' / 'cancelado')
- `total` (Decimal, calculado)
- `fecha_creacion` (DateTime)

### DetalleVenta
- `venta` (FK → Venta, CASCADE)
- `producto` (FK → Producto, PROTECT)
- `cantidad` (Integer)
- `precio_unitario` (Decimal, snapshot del precio al momento de venta)

---

## 🚀 Deploy

### Backend (Render)
1. Conectado a GitHub para CI/CD automático
2. Blueprint (`render.yaml`) define toda la infraestructura
3. PostgreSQL gratuito incluido
4. Variables de entorno sensibles en panel de Render
5. Build automático: `pip install` → `migrate` → `collectstatic`

### Frontend (Vercel)
1. Conectado a GitHub, deploy automático en cada push
2. Variable `VITE_API_URL` apunta al backend en Render
3. Build: `npm run build` → Vite optimiza producción
4. Dominio HTTPS gratuito + CDN global

---

## 📈 Escalabilidad Futura

- **Cache con Redis:** Para menú y categorías (datos que casi no cambian)
- **WebSockets:** Notificaciones en tiempo real a cocina
- **Reportes:** Gráficos con Chart.js, exportación a PDF/Excel
- **Multi-restaurante:** Agregar modelo `Restaurante` y filtrar por contexto
- **Inventario:** Control de stock, alertas de productos por acabarse
- **Propinas:** Campo en Venta para registro de propinas

---

## 🎓 Documentación Adicional

Este proyecto incluye **material educativo completo** en la carpeta `docs/`:

- **Mini-clases** por concepto (Django, DRF, JWT, React Context, etc.)
- **Diagramas** Mermaid (arquitectura, modelo ER, flujos)
- **Quizzes** al final de cada fase para verificar aprendizaje

Ideal para:
- Developers junior que quieren entender un proyecto full-stack real
- Estudiantes de bootcamps
- Equipos que necesitan onboarding estructurado

---

## 📞 Contacto

**John Infante**  
Desarrollador Full-Stack  

📧 johningonzalez2021@gmail.com  
🐙 [github.com/JOHNINFA](https://github.com/JOHNINFA)  
🌐 [Demo MenuPOS](https://menupos.vercel.app)

---

## 📄 Licencia

Proyecto de portafolio. Uso libre con atribución.

---

**Última actualización:** Julio 2026
