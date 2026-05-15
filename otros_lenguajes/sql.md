# SQL

## SELECT

`SELECT` permite consultar datos de una o varias tablas. Es la base para filtrar, ordenar, limitar y proyectar columnas.

Conceptos clave:

- Selección de columnas.
- Filtros con `WHERE`.
- Ordenamiento con `ORDER BY`.
- Límites con `LIMIT`.
- Alias con `AS`.

## JOIN

Los `JOIN` combinan filas de distintas tablas usando columnas relacionadas. Son esenciales para trabajar con modelos relacionales normalizados.

Tipos comunes:

- `INNER JOIN`.
- `LEFT JOIN`.
- `RIGHT JOIN`.
- `FULL OUTER JOIN`.
- `CROSS JOIN`.

## GROUP BY

`GROUP BY` agrupa filas para calcular métricas con funciones de agregación.

Funciones frecuentes:

- `COUNT`.
- `SUM`.
- `AVG`.
- `MIN`.
- `MAX`.

También conviene practicar `HAVING` para filtrar grupos después de la agregación.

## Subconsultas

Las subconsultas permiten usar el resultado de una consulta dentro de otra. Pueden aparecer en `SELECT`, `FROM`, `WHERE` o `HAVING`.

Usos habituales:

- Filtrar por valores calculados.
- Comparar contra agregaciones.
- Crear tablas derivadas.
- Resolver consultas por pasos.

## Índices

Los índices aceleran búsquedas, ordenamientos y uniones, aunque aumentan el coste de escritura y ocupan espacio adicional.

Puntos importantes:

- Índices sobre claves primarias y foráneas.
- Índices compuestos.
- Selectividad.
- Análisis de planes de ejecución.
- Equilibrio entre lectura y escritura.

## Modelado relacional

El modelado relacional define cómo representar entidades, relaciones y restricciones en tablas.

Conceptos recomendados:

- Entidades y atributos.
- Claves primarias.
- Claves foráneas.
- Relaciones uno a uno, uno a muchos y muchos a muchos.
- Normalización.
- Restricciones de integridad.

## PostgreSQL

PostgreSQL es un sistema de bases de datos relacional avanzado y muy usado en producción. Además de SQL estándar, ofrece características potentes para aplicaciones modernas.

Temas útiles:

- Tipos de datos avanzados.
- `SERIAL` e identidades.
- JSON y JSONB.
- Vistas.
- Transacciones.
- Extensiones.
- Herramientas como `psql` y `EXPLAIN`.
