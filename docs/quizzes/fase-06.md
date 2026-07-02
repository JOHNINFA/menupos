# 🧠 Quiz FASE 6 — UI del POS en React

> 📚 **Clases que cubre**: [`08-componentes-props.md`](../clases/08-componentes-props.md), [`09-estado-efectos.md`](../clases/09-estado-efectos.md), [`10-consumir-api-axios.md`](../clases/10-consumir-api-axios.md)

---

## 📝 Preguntas

1. ¿En qué dirección fluyen las props, de padre a hijo o al revés?
2. ¿Cómo le "avisa" un componente hijo algo a su componente padre?
3. ¿Por qué no se debe modificar el estado (`useState`) directamente?
4. ¿Qué significa pasar un array vacío `[]` como segundo argumento de `useEffect`?
5. ¿Qué hace el interceptor de Axios en `api/client.ts`?
6. ¿Por qué guardamos el JWT en `localStorage`, y cuál es la limitación conocida de eso?
7. ¿Para qué sirve el `AuthContext` en vez de pasar el usuario como prop en cada componente?
8. En `Pos.tsx`, ¿por qué el precio final se recalcula en el backend en vez de confiar en el total que arma el carrito del frontend?
9. ¿Qué hace `RutaProtegida` cuando `loading` es `true`?
10. ¿Qué pasa si un usuario visita `/dashboard` sin haber iniciado sesión?

---

---

---

## ✅ Respuestas

<br><br><br>

### 1. De **padre a hijo únicamente**. El hijo nunca modifica las props que recibió directamente.

### 2. El padre le pasa una **función** como prop (ej: `onAgregar`), y el hijo la **llama** cuando ocurre el evento — el padre decide qué hacer con esa información.

### 3. Porque React necesita **detectar el cambio** para volver a pintar la pantalla. Si mutas el estado directamente (ej: `carrito.push(x)`), React no se entera y la interfaz no se actualiza.

### 4. Que el efecto se ejecute **solo UNA vez**, cuando el componente aparece en pantalla por primera vez (equivalente a "cuando se abre la puerta del restaurante, pregunta el menú del día").

### 5. **Inyecta automáticamente** el header `Authorization: Bearer <token>` en cada petición, tomando el token guardado en `localStorage`, para no repetirlo manualmente en cada llamada a la API.

### 6. Es simple de implementar para un proyecto de portafolio, pero es **vulnerable a ataques XSS** (si un script malicioso se ejecuta en la página, puede leer `localStorage`). En producción real se recomienda usar cookies `httpOnly`.

### 7. Evita el **"prop drilling"**: pasar el usuario manualmente a través de muchos componentes intermedios que ni siquiera lo usan, solo para que llegue al componente que sí lo necesita. El Context lo hace disponible directamente donde se necesite.

### 8. Porque el frontend **no es confiable**: un usuario malicioso podría modificar el JavaScript en su navegador y mandar un total falso. El backend SIEMPRE recalcula el precio real desde `producto.precio` (ver FASE 5), sin importar lo que diga el frontend.

### 9. Muestra una pantalla de **"Cargando..."** en vez de decidir prematuramente si redirigir a `/login` o mostrar el contenido — evita el parpadeo de mostrar el login brevemente incluso cuando SÍ hay una sesión válida guardada.

### 10. `RutaProtegida` detecta que `user` es `null` (no hay sesión) y usa `<Navigate to="/login" />` para redirigirlo automáticamente a la pantalla de login.

---

## 🎯 Tu puntaje

- 🟢 **8-10**: Excelente, tu POS está funcionando de punta a punta
- 🟡 **5-7**: Bien, repasa lo fallado
- 🔴 **0-4**: Relee las 3 clases de esta fase

---

## 🏆 Habilidades de entrevista desbloqueadas

- ✅ "¿Cómo manejas el estado global (usuario logueado) en tu app?"
- ✅ "¿Cómo proteges rutas que requieren autenticación?"
- ✅ "¿Dónde guardas el token y qué riesgos tiene esa decisión?"
- ✅ "¿Cómo evitas que el cliente manipule precios en el checkout?"

---

## ➡️ Siguiente

**FASE 7 — Subir imágenes de productos a AWS S3**
