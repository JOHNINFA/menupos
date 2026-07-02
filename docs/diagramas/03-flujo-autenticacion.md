# 📊 Diagrama 03 — Flujo de autenticación JWT

> 📖 **Clase asociada**: [`../clases/07-jwt-autenticacion.md`](../clases/07-jwt-autenticacion.md)

---

## 🔐 Login → petición autenticada → renovación

```mermaid
sequenceDiagram
    participant M as 🧑‍💼 Mesero (React)
    participant API as 🌐 Django API

    M->>API: POST /api/auth/login/ {username, password}
    alt Credenciales correctas
        API-->>M: 200 {access, refresh}
        Note over M: Guarda ambos tokens
    else Credenciales incorrectas
        API-->>M: 401 Unauthorized
    end

    M->>API: GET /api/productos/<br/>Header: Authorization: Bearer access
    alt Token válido
        API-->>M: 200 + datos
    else Sin token o token inválido
        API-->>M: 401 Unauthorized
    end

    Note over M: Access token expira (60 min)

    M->>API: POST /api/auth/refresh/ {refresh}
    API-->>M: 200 {access nuevo}
    Note over M: Sigue trabajando sin re-loguearse
```

---

## 🛡️ Permisos por rol dentro de la API

```mermaid
flowchart TD
    R[Petición entrante] --> AUTH{¿Tiene token<br/>válido?}
    AUTH -->|No| E401[401 Unauthorized]
    AUTH -->|Sí| METHOD{¿Qué verbo HTTP?}

    METHOD -->|GET| OK1[200 OK<br/>cualquier usuario autenticado]
    METHOD -->|POST/PUT/PATCH/DELETE| ROL{¿rol == admin?}

    ROL -->|Sí, en /productos o /categorias| OK2[200/201 OK]
    ROL -->|No, en /productos o /categorias| E403[403 Forbidden]

    METHOD -->|POST en /ventas| OK3[201 Created<br/>cualquier usuario autenticado]

    style E401 fill:#fecaca,stroke:#dc2626,color:#000
    style E403 fill:#fecaca,stroke:#dc2626,color:#000
    style OK1 fill:#bbf7d0,stroke:#16a34a,color:#000
    style OK2 fill:#bbf7d0,stroke:#16a34a,color:#000
    style OK3 fill:#bbf7d0,stroke:#16a34a,color:#000
```

> 💡 Nota: cualquier usuario autenticado (mesero o admin) puede **leer** el menú y **crear** ventas. Solo un **admin** puede crear/editar/borrar categorías y productos.
