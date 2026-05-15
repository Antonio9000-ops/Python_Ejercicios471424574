# Retos para nivel profesional

Estos retos están pensados para estudiantes que ya pueden estructurar aplicaciones completas y quieren practicar patrones cercanos al desarrollo profesional.

## Reto 1: Proyecto final de plataforma de tareas

### Objetivo
Desarrollar una aplicación completa de gestión de tareas con base de datos, autenticación, pruebas automatizadas y despliegue.

### Requisitos
- Implementar registro e inicio de sesión de usuarios.
- Proteger rutas para que cada usuario gestione solo sus tareas.
- Guardar usuarios y tareas en una base de datos relacional.
- Permitir crear, listar, actualizar, completar y eliminar tareas.
- Incluir pruebas unitarias y/o de integración para los flujos principales.
- Preparar instrucciones de despliegue en un servicio cloud o plataforma similar.

### Restricciones según nivel
- No guardar contraseñas en texto plano; usar hashing seguro.
- Usar variables de entorno para configuración sensible.
- Separar capas como rutas, modelos, servicios y pruebas.
- Incluir migraciones o instrucciones claras para crear la base de datos.
- Mantener dependencias registradas en un archivo como `requirements.txt` o `pyproject.toml`.

### Extras opcionales
- Agregar roles de usuario, por ejemplo administrador y usuario estándar.
- Implementar recuperación de contraseña simulada.
- Añadir integración continua para ejecutar tests automáticamente.
- Crear documentación interactiva de la API.
- Contenerizar la aplicación con Docker.

### Criterios de evaluación
- La autenticación funciona y protege correctamente los recursos privados.
- La base de datos mantiene relaciones correctas entre usuarios y tareas.
- Los tests cubren casos exitosos y errores frecuentes.
- La aplicación puede desplegarse siguiendo instrucciones reproducibles.
- El código evita duplicación y sigue una arquitectura coherente.

## Reto 2: API REST profesional con usuarios e inventario

### Objetivo
Crear una API REST de inventario preparada para escenarios reales con autenticación, permisos, base de datos y pruebas.

### Requisitos
- Implementar autenticación con tokens o sesiones.
- Crear endpoints CRUD para productos, categorías y movimientos de stock.
- Registrar qué usuario realiza cada movimiento importante.
- Guardar la información en PostgreSQL, MySQL, SQLite u otra base de datos soportada por el curso.
- Incluir pruebas automatizadas para endpoints críticos.
- Documentar instalación, configuración, ejecución, pruebas y despliegue.

### Restricciones según nivel
- Usar migraciones o scripts versionados para la estructura de la base de datos.
- Validar permisos antes de modificar recursos.
- Centralizar el manejo de errores.
- No exponer secretos en el repositorio.
- Usar respuestas HTTP consistentes.

### Extras opcionales
- Agregar auditoría de cambios.
- Implementar paginación, ordenamiento y filtros combinables.
- Generar documentación OpenAPI.
- Configurar Docker Compose para API y base de datos.
- Medir cobertura de pruebas.

### Criterios de evaluación
- La API cumple operaciones CRUD de forma segura.
- Los permisos impiden acciones no autorizadas.
- Las pruebas verifican autenticación, validación y persistencia.
- El despliegue está documentado y puede repetirse.
- La estructura del proyecto es mantenible para un equipo.
