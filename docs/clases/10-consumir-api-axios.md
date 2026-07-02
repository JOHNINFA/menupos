# 📖 Clase 10 — Consumir la API con Axios

> 🎯 **Objetivo**: Conectar React con la API de Django usando Axios, incluyendo el token JWT automáticamente.
> ⏱️ **Tiempo**: 8 minutos
> 📚 **Pre-requisitos**: Clase [`09-estado-efectos.md`](09-estado-efectos.md), [`07-jwt-autenticacion.md`](07-jwt-autenticacion.md)

---

## 🤔 El problema

Cada petición a la API protegida necesita el header:
```
Authorization: Bearer <access_token>
```

Escribir eso a mano en cada petición sería repetitivo y propenso a errores.

## 🧑‍💼 La solución: un cliente Axios con interceptor

```ts
// src/api/client.ts
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

// El interceptor se ejecuta ANTES de CADA petición que hagamos con `api`.
// Aquí "inyectamos" el token automáticamente, sin repetir código.
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api
```

Ahora en cualquier parte de la app:

```ts
import api from './api/client'

// Ya trae el token automáticamente incluido
const res = await api.get('/productos/')
console.log(res.data)
```

### Analogía
El interceptor es como un **asistente que siempre revisa que llevas puesta la pulsera VIP (token)** antes de dejarte entrar a cualquier sección del restaurante — sin que tú tengas que acordarte de mostrarla cada vez.

---

## 🔐 ¿Dónde guardamos el token?

Usamos `localStorage`: una "cajita" del navegador que persiste incluso si recargas la página.

```ts
localStorage.setItem('access', token)   // Guardar
localStorage.getItem('access')          // Leer
localStorage.removeItem('access')       // Borrar (logout)
```

> ⚠️ **Simplificación consciente para el MVP**: guardar JWT en `localStorage` es vulnerable a ataques XSS en apps de producción reales (se recomiendan cookies `httpOnly`). Para MenuPOS (proyecto de portafolio/aprendizaje) es aceptable y mucho más simple de implementar — pero es importante **saber la limitación** para poder explicarla en una entrevista.

---

## 🌐 El Contexto de Autenticación (Context API)

Necesitamos que **TODA la app** sepa quién está logueado, sin pasar props manualmente de componente en componente ("prop drilling"). Para eso usamos el **Context API** de React:

```tsx
// AuthContext "envuelve" toda la app y comparte user/login/logout
// con cualquier componente que lo necesite, sin importar cuán anidado esté.
const AuthContext = createContext<AuthContextType | null>(null)

export function useAuth() {
  return useContext(AuthContext)!  // hook para consumir el contexto fácil
}
```

### Analogía
El Context es como el **altavoz del restaurante**: en vez de que el mesero (componente) tenga que caminar y avisarle personalmente a cada empleado quién es el cliente VIP en la mesa 5, lo anuncia UNA vez por el altavoz y todos lo escuchan al instante.

---

## 🧠 Quiz rápido
1. ¿Qué hace un interceptor de Axios?
2. ¿Por qué usamos `localStorage` para el token, y cuál es su limitación conocida?
3. ¿Para qué sirve el Context API en vez de pasar props manualmente?

> 📝 Respuestas en el quiz de FASE 6.

## 🔗 Referencias
- [Axios Interceptors](https://axios-http.com/docs/interceptors)
- [React Context (docs, español)](https://es.react.dev/learn/passing-data-deeply-with-context)
