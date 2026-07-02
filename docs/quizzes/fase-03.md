# 🧠 Quiz FASE 3 — React, Vite y Tailwind

> 📚 **Clase que cubre**: [`03-react-vite-tailwind.md`](../clases/03-react-vite-tailwind.md)

---

## 📝 Preguntas

1. ¿Qué es un componente en React? Da un ejemplo de MenuPOS.
2. ¿Cuál es la ventaja principal de Vite frente a herramientas más viejas (como Webpack)?
3. ¿Qué significa HMR?
4. ¿Cómo se aplican estilos con Tailwind, en una frase?
5. ¿Qué hace `npm run build` a diferencia de `npm run dev`?
6. ¿Por qué no hay `tailwind.config.js` en este proyecto?
7. ¿Para qué instalamos `react-router-dom`?
8. ¿Para qué instalamos `axios`?
9. ¿Qué archivo es el "punto de entrada" que monta `<App />` en el HTML?
10. En la metáfora del restaurante, ¿React representa qué parte?

---

---

---

## ✅ Respuestas

<br><br><br>

### 1. Un componente es una **pieza reutilizable de interfaz**. Ejemplo: `<ProductoCard />` representa UN producto del menú y se repite tantas veces como productos haya.

### 2. Vite arranca y recompila **casi instantáneamente**, mientras que herramientas más viejas podían tardar segundos o minutos en cada cambio.

### 3. **Hot Module Replacement** — actualiza solo la parte del código que cambió en el navegador, sin recargar toda la página.

### 4. Se combinan **clases utilitarias ya hechas** (ej: `p-4`, `bg-white`, `rounded-lg`) directo en el JSX, en vez de escribir CSS personalizado.

### 5. `npm run dev` levanta un servidor de **desarrollo** con recarga en caliente. `npm run build` genera los archivos **optimizados y minificados** listos para producción (en la carpeta `dist/`).

### 6. Porque estamos usando **Tailwind CSS v4**, que simplificó su configuración: ahora se activa con una sola línea en el CSS (`@import "tailwindcss";`) en vez de un archivo de configuración JS separado.

### 7. Para manejar **rutas** dentro de la aplicación (ej: `/login`, `/pos`, `/dashboard`) sin recargar la página completa — se usará en FASE 6.

### 8. Para hacer **peticiones HTTP** desde React hacia la API de Django (ej: pedir la lista de productos, enviar una venta) — se usará en FASE 5-6.

### 9. `main.tsx` — usa `createRoot(...).render(<App />)` para "inyectar" React dentro del `<div id="root">` de `index.html`.

### 10. React representa el **salón del restaurante**: la parte visual e interactiva que el cliente (usuario) ve y usa directamente.

---

## 🎯 Tu puntaje

- 🟢 **8-10**: Perfecto, sigues a FASE 4
- 🟡 **5-7**: Bien, repasa lo fallado
- 🔴 **0-4**: Relee la clase 03

---

## 🏆 Habilidades de entrevista desbloqueadas

- ✅ "¿Por qué elegiste React en vez de otra librería?"
- ✅ "¿Qué ventajas tiene Vite sobre Create React App / Webpack?"
- ✅ "¿Cómo manejas los estilos en tu proyecto?"

---

## ➡️ Siguiente

**FASE 4 — Modelos de base de datos (users, menu, sales)**
