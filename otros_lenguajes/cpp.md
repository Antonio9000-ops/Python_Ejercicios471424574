# C++

## Memoria

C++ permite controlar la memoria con mucho detalle. Esa flexibilidad ofrece rendimiento, pero también exige responsabilidad para evitar fugas, accesos inválidos y errores difíciles de depurar.

Temas clave:

- Stack y heap.
- Duración de vida de variables.
- Asignación dinámica.
- RAII (Resource Acquisition Is Initialization).
- Smart pointers (`std::unique_ptr`, `std::shared_ptr`).

## Punteros

Los punteros almacenan direcciones de memoria. Son una herramienta poderosa para trabajar con estructuras dinámicas, arreglos, recursos y APIs de bajo nivel.

Aspectos importantes:

- Operadores `&` y `*`.
- Punteros nulos.
- Referencias vs. punteros.
- Aritmética de punteros.
- Punteros inteligentes como alternativa segura.

## Estructuras de datos

C++ incluye la STL (Standard Template Library), que ofrece contenedores eficientes y reutilizables.

Estructuras comunes:

- `std::vector`.
- `std::array`.
- `std::list`.
- `std::map`.
- `std::unordered_map`.
- `std::set`.
- `std::queue` y `std::stack`.

## Algoritmos

La biblioteca estándar incluye algoritmos genéricos que funcionan con iteradores y contenedores.

Algoritmos recomendados:

- Ordenamiento con `std::sort`.
- Búsqueda con `std::find` y `std::binary_search`.
- Transformaciones con `std::transform`.
- Acumulación con `std::accumulate`.
- Uso de lambdas como predicados.

## Rendimiento

C++ es muy usado cuando el rendimiento es crítico. Para escribir código eficiente conviene comprender el coste de copias, asignaciones, caché, complejidad algorítmica y elección de estructuras de datos.

Buenas prácticas:

- Medir antes de optimizar.
- Evitar copias innecesarias con referencias y move semantics.
- Elegir contenedores adecuados.
- Usar compiladores y flags de optimización.
- Analizar complejidad temporal y espacial.
