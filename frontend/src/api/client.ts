// Cliente Axios centralizado. Ver mini-clase:
// docs/clases/10-consumir-api-axios.md

import axios from 'axios'

// La URL del backend cambia según el entorno:
// - En desarrollo: http://localhost:8000/api (valor por defecto)
// - En producción (Vercel): se lee de la variable VITE_API_URL, que
//   apuntará al backend en Railway. Las variables de Vite deben empezar
//   con VITE_ para que el navegador pueda verlas.
const baseURL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'

const api = axios.create({ baseURL })

// Interceptor: se ejecuta ANTES de cada petición. Inyecta el token
// automáticamente, para no repetir el header en cada llamada.
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api
