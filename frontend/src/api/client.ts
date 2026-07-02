// Cliente Axios centralizado. Ver mini-clase:
// docs/clases/10-consumir-api-axios.md

import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

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
