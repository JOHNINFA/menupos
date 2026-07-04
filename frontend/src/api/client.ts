// Cliente HTTP centralizado usando fetch NATIVO del navegador.
// Antes usábamos axios; migramos a fetch para no depender de librerías
// externas (cero dependencias = menor superficie de ataque).
// Ver mini-clase: docs/clases/10-consumir-api.md
//
// Mantenemos la misma "forma" que tenía axios (api.get/post/patch/delete
// devuelven { data }) para no reescribir todas las páginas.

// La URL del backend cambia según el entorno:
// - Desarrollo: http://localhost:8000/api (valor por defecto)
// - Producción (Vercel): se lee de VITE_API_URL, que apunta a Railway.
//   Las variables de Vite deben empezar con VITE_ para verse en el navegador.
const baseURL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'

interface Respuesta<T> {
  data: T
}

async function request<T>(
  method: string,
  path: string,
  body?: unknown
): Promise<Respuesta<T>> {
  const headers: Record<string, string> = {}

  // Inyectamos el token JWT automáticamente (como hacía el interceptor
  // de axios), tomándolo de localStorage.
  const token = localStorage.getItem('access')
  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }

  let payload: BodyInit | undefined
  if (body instanceof FormData) {
    // Para subir archivos (imágenes) NO ponemos Content-Type a mano:
    // el navegador lo pone solo con el "boundary" correcto de multipart.
    payload = body
  } else if (body !== undefined) {
    headers['Content-Type'] = 'application/json'
    payload = JSON.stringify(body)
  }

  const res = await fetch(`${baseURL}${path}`, { method, headers, body: payload })

  // fetch NO lanza error en respuestas 4xx/5xx (a diferencia de axios).
  // Lo lanzamos nosotros para que los try/catch y .catch existentes sigan
  // funcionando igual que antes.
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}`)
  }

  // Algunas respuestas (ej: DELETE con 204) no traen cuerpo.
  const texto = await res.text()
  const data = texto ? JSON.parse(texto) : null
  return { data }
}

const api = {
  get: <T,>(path: string) => request<T>('GET', path),
  post: <T,>(path: string, body?: unknown) => request<T>('POST', path, body),
  patch: <T,>(path: string, body?: unknown) => request<T>('PATCH', path, body),
  delete: <T,>(path: string) => request<T>('DELETE', path),
}

export default api
