# 📖 Clase 10 — Consumir la API con fetch

> 🎯 **Objetivo**: Conectar React con la API de Django usando `fetch` nativo, incluyendo el token JWT automáticamente.
> ⏱️ **Tiempo**: 8 minutos
> 📚 **Pre-requisitos**: Clase [`09-estado-efectos.md`](09-estado-efectos.md), [`07-jwt-autenticacion.md`](07-jwt-autenticacion.md)

---

## 🤔 El problema

Cada petición a la API protegida necesita el header:
```
Authorization: Bearer <access_token>
```

Escribir eso a mano en cada petición sería repetitivo y propenso a errores.

## 🌐 ¿Por qué fetch y no axios?

Empezamos usando **axios** (una librería popular para peticiones HTTP), pero migramos a **`fetch`**, que viene **integrado en el navegador**:

- ✅ **Cero dependencias externas** → menor superficie de ataque (menos librerías de terceros que puedan tener vulnerabilidades)
- ✅ Es un estándar web: funciona en todos los navegadores modernos
- ✅ Un dev que domina `fetch` nativo demuestra fundamentos sólidos

> 💡 Lección de seguridad: cada librería que agregas es código de otra persona corriendo en tu app. Menos dependencias = menos riesgo de "supply chain attacks" (cuando comprometen una librería para infectar a quien la usa).

---

## 🧑‍💼 La solución: un "envoltorio" (wrapper) de fetch

`fetch` es potente pero un poco verboso. Creamos un pequeño envoltorio que:
1. Agrega la URL base automáticamente
2. Inyecta el token JWT en cada petición
3. Convierte el cuerpo a JSON (o deja FormData para subir archivos)
4. Lanza error si la respuesta no es exitosa

```ts
// src/api/client.ts (simplificado)
const baseURL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'

async function request(method, path, body) {
  const headers = {}
  const token = localStorage.getItem('access')
  if (token) headers['Authorization'] = `Bearer ${token}`

  let payload
  if (body instanceof FormData) {
    payload = body                 // el navegador pone el Content-Type
  } else if (body !== undefined) {
    headers['Content-Type'] = 'application/json'
    payload = JSON.stringify(body)
  }

  const res = await fetch(`${baseURL}${path}`, { method, headers, body: payload })
  if (!res.ok) throw new Error(`HTTP ${res.status}`)  // fetch NO lanza solo

  const texto = await res.text()
  return { data: texto ? JSON.parse(texto) : null }
}

const api = {
  get:    (path) => request('GET', path),
  post:   (path, body) => request('POST', path, body),
  patch:  (path, body) => request('PATCH', path, body),
  delete: (path) => request('DELETE', path),
}
```

Ahora en cualquier parte de la app:

```ts
import api from './api/client'
const res = await api.get('/productos/')  // ya trae el token incluido
console.log(res.data)
```

### ⚠️ Diferencia clave: fetch NO lanza error en 4xx/5xx

Con axios, un `401` o `500` lanzaba una excepción automáticamente. **`fetch` NO** — considera "exitosa" cualquier respuesta que llegó, aunque sea un error. Por eso nuestro wrapper revisa `res.ok` y lanza el error nosotros mismos, para que los `try/catch` funcionen igual.

### Analogía
El wrapper es como un **asistente que siempre revisa que llevas puesta la pulsera VIP (token)** antes de dejarte entrar a cualquier sección — sin que tú tengas que acordarte de mostrarla cada vez.

---

## 🔐 ¿Dónde guardamos el token?

Usamos `localStorage`: una "cajita" del navegador que persiste incluso si recargas la página.

```ts
localStorage.setItem('access', token)   // Guardar
localStorage.getItem('access')          // Leer
localStorage.removeItem('access')       // Borrar (logout)
```

> ⚠️ **Simplificación consciente para el MVP**: guardar JWT en `localStorage` es vulnerable a ataques XSS en apps de producción reales (se recomiendan cookies `httpOnly`). Para MenuPOS (proyecto de portafolio/aprendizaje) es aceptable y más simple — pero saber la limitación te sirve para explicarla en una entrevista.

---

## 🌐 El Contexto de Autenticación (Context API)

Necesitamos que **TODA la app** sepa quién está logueado, sin pasar props manualmente de componente en componente ("prop drilling"). Para eso usamos el **Context API** de React:

```tsx
const AuthContext = createContext<AuthContextType | null>(null)

export function useAuth() {
  return useContext(AuthContext)!  // hook para consumir el contexto fácil
}
```

### Analogía
El Context es como el **altavoz del restaurante**: en vez de que el mesero (componente) camine avisándole a cada empleado quién es el cliente VIP, lo anuncia UNA vez por el altavoz y todos lo escuchan.

---

## 🧠 Quiz rápido
1. ¿Por qué migramos de axios a fetch?
2. ¿Cuál es la diferencia CLAVE entre cómo fetch y axios manejan un error 401?
3. ¿Por qué usamos `localStorage` para el token, y cuál es su limitación conocida?
4. ¿Para qué sirve el Context API en vez de pasar props manualmente?

> 📝 Respuestas en el quiz de FASE 6.

## 🔗 Referencias
- [fetch (MDN, español)](https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Using_Fetch)
- [React Context (docs, español)](https://es.react.dev/learn/passing-data-deeply-with-context)
