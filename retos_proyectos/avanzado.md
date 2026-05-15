# Retos para nivel avanzado

Estos retos están pensados para estudiantes que ya conocen funciones, módulos, entornos virtuales, manejo de errores, archivos, paquetes y conceptos básicos de HTTP.

## Reto 1: API REST de tareas

### Objetivo
Crear una API REST para administrar tareas desde clientes HTTP como navegador, Postman, Insomnia o `curl`.

### Requisitos
- Crear endpoints para listar, crear, consultar, actualizar y eliminar tareas.
- Representar cada tarea con identificador, título, descripción, estado y fecha de creación.
- Responder con JSON.
- Usar códigos de estado HTTP adecuados.
- Documentar cómo ejecutar el proyecto y probar los endpoints.

### Restricciones según nivel
- Usar un framework ligero como Flask o FastAPI si ya fue presentado en el curso.
- Mantener rutas, modelos y lógica de negocio en archivos separados cuando el proyecto crezca.
- Validar datos de entrada antes de guardarlos.
- La persistencia puede ser en memoria, archivo JSON o SQLite según el avance del grupo.

### Extras opcionales
- Agregar paginación o filtros por estado.
- Agregar validación con esquemas.
- Crear una colección de pruebas para Postman o ejemplos con `curl`.
- Añadir logs básicos de solicitudes y errores.

### Criterios de evaluación
- Los endpoints cumplen el comportamiento esperado para operaciones CRUD.
- Las respuestas JSON tienen una estructura consistente.
- Los errores comunes devuelven mensajes claros y códigos HTTP correctos.
- El proyecto puede ejecutarse siguiendo las instrucciones del README.

## Reto 2: Inventario con persistencia y reportes

### Objetivo
Evolucionar el inventario simple para convertirlo en una herramienta con almacenamiento persistente y reportes útiles.

### Requisitos
- Registrar productos con nombre, categoría, cantidad, precio y proveedor.
- Guardar los datos en archivo JSON, CSV o SQLite.
- Actualizar entradas y salidas de stock.
- Generar reportes de bajo stock y valor total por categoría.
- Manejar errores de lectura, escritura y datos inválidos.

### Restricciones según nivel
- Separar el proyecto en módulos.
- Usar excepciones para controlar errores esperados.
- No duplicar lógica entre operaciones similares.
- Documentar el formato de datos usado.

### Extras opcionales
- Exportar reportes a CSV.
- Crear pruebas unitarias para cálculos principales.
- Agregar búsqueda por categoría o proveedor.

### Criterios de evaluación
- Los datos se conservan entre ejecuciones.
- Los reportes son correctos y fáciles de interpretar.
- El manejo de errores evita pérdidas de información.
- La estructura del proyecto permite agregar nuevas funcionalidades.

## Reto 3: Gestor de notas con interfaz web básica

### Objetivo
Crear una aplicación web sencilla para gestionar notas personales o académicas.

### Requisitos
- Crear, listar, editar y eliminar notas.
- Guardar título, contenido, categoría y fecha de creación.
- Mostrar formularios HTML para interactuar con la aplicación.
- Validar campos obligatorios.
- Persistir la información en archivo o SQLite.

### Restricciones según nivel
- Usar plantillas HTML si el framework elegido lo permite.
- Mantener separadas las rutas, plantillas y funciones auxiliares.
- No implementar autenticación todavía si no se ha estudiado.
- Evitar guardar datos sensibles en texto plano.

### Extras opcionales
- Agregar búsqueda por texto.
- Filtrar por categoría.
- Añadir estilos CSS simples.
- Crear pruebas para las funciones de persistencia.

### Criterios de evaluación
- La aplicación permite administrar notas desde el navegador.
- Los formularios validan datos requeridos.
- La persistencia funciona después de reiniciar el servidor.
- La organización del proyecto es clara.
