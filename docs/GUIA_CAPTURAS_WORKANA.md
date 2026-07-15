# 📸 Guía: Capturas de pantalla para Workana

> Esto es un checklist de qué capturar y cómo hacerlo para que el proyecto se vea profesional en Workana.

---

## 📷 Capturas que necesitas

### 1. **Imagen de Portada** (1200x630px recomendado)
**Lo que debe mostrar:** El login del POS o dashboard en acción

**Cómo capturarlo:**
```bash
# 1. Inicia el servidor local
cd backend
python manage.py runserver

# 2. En otra terminal, inicia el frontend
cd frontend
npm run dev

# 3. Abre http://localhost:5173 en Chrome
# 4. Limpia la sesión: Ctrl+Shift+Delete → localStorage
# 5. Captura la pantalla de LOGIN (se ve profesional y atrae)
```

**Qué incluir en la captura:**
- Logo/título "MenuPOS"
- Campos de login visibles
- Logo de restaurant o icono
- Colores de Tailwind (azul/morado)

**Herramienta:** PrintScreen o Chrome DevTools (F12 → Ctrl+Shift+P → "Screenshot")

---

### 2. **Galería - Imagen 1: Dashboard**
**Lo que debe mostrar:** Panel principal con ventas del día

**Cómo capturarlo:**
```bash
# 1. Loguéate como admin:
#    Usuario: admin
#    Contraseña: [tu contraseña local]

# 2. Espera a que cargue el Dashboard
# 3. Captura mostrando:
#    - Cards con "Total Vendido", "Pedidos Pendientes"
#    - Tabla de últimas ventas
#    - Gráfico/listado de productos
```

**Qué resaltar en la captura:**
- Números/datos visibles (total, cantidad pedidos)
- Interfaz limpia y moderna
- Sin datos sensibles (borra nombres si es necesario)

---

### 3. **Galería - Imagen 2: POS (Punto de Venta)**
**Lo que debe mostrar:** El carrito de compra en acción

**Cómo capturarlo:**
```bash
# 1. Loguéate como mesero
#    Usuario: mesero1
#    Contraseña: [tu contraseña local]

# 2. Ve a "Punto de Venta"
# 3. Haz clic en "Nueva Venta"
# 4. Selecciona una mesa (ej: Mesa 1)
# 5. Agrega 2-3 productos al carrito
# 6. Captura mostrando:
#    - Productos disponibles a la izquierda
#    - Carrito con detalles a la derecha
#    - Botón "Cobrar" visible
```

---

### 4. **Galería - Imagen 3: Comanda Imprimible**
**Lo que debe mostrar:** La comanda que va a cocina

**Cómo capturarlo:**
```bash
# 1. Después de crear una venta (paso anterior)
# 2. Ve al Dashboard
# 3. Haz clic en "Ver Comanda" (o icono de impresora)
# 4. Captura la pantalla de comanda mostrando:
#    - Número de mesa
#    - Lista de productos
#    - Hora
#    - Botón de imprimir
```

---

## 🎨 Especificaciones técnicas

| Elemento | Especificación |
|---|---|
| **Resolución** | 1200x630px (portada), 1024x768px (galerías) |
| **Formato** | JPG o PNG |
| **Tamaño máximo** | 5 MB cada una |
| **Sin datos sensibles** | Reemplaza emails/teléfonos con [nombre] |
| **Colores claros** | Evita screenshots en oscuridad |

---

## ✅ Checklist antes de subir

- [ ] Portada capturada (login o dashboard)
- [ ] Dashboard capturada (con datos visibles)
- [ ] POS capturada (carrito en acción)
- [ ] Comanda capturada (o gestión de menú alternativo)
- [ ] Todas en buena resolución (no pixeladas)
- [ ] Sin errores/bugs visibles
- [ ] Sin datos sensibles (emails, contraseñas)
- [ ] Nombradas así:
  - `menupos-portada.jpg`
  - `menupos-dashboard.jpg`
  - `menupos-pos.jpg`
  - `menupos-comanda.jpg`

---

## 💡 Pro Tips

1. **Si el servidor local no arranca**, verifica:
   ```bash
   cd backend
   python manage.py migrate
   python manage.py check
   ```

2. **Si no puedes loguear**, crea un usuario de prueba:
   ```bash
   python manage.py shell
   >>> from users.models import Usuario
   >>> Usuario.objects.create_user(username='mesero1', password='test123', rol='mesero')
   ```

3. **Para eliminar fondo blanco en PNG**, usa:
   - [remove.bg](https://remove.bg) (gratis)
   - O guárdalo como JPG directamente

4. **Para agregar logo/nombre**, edita las capturas en Canva.com (gratis) antes de subirlas

---

## 🎯 Orden recomendado en Workana

1. **Portada**: La captura más atractiva (login o dashboard)
2. **Galería 1**: Dashboard (muestra profesionalismo)
3. **Galería 2**: POS (muestra funcionalidad principal)
4. **Galería 3**: Comanda o menú (muestra completitud)

¡Listo! Con esto tienes todo para subirlo a Workana. 🚀
