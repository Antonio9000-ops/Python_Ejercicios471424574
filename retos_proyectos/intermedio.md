# Retos para nivel intermedio

Estos retos están pensados para estudiantes que ya trabajan con listas, diccionarios, funciones, ciclos, validaciones básicas y, opcionalmente, lectura y escritura de archivos.

## Reto 1: Sistema de notas

### Objetivo
Crear un sistema para registrar estudiantes, guardar sus calificaciones y calcular resultados académicos básicos.

### Requisitos
- Registrar varios estudiantes.
- Guardar varias notas por estudiante.
- Calcular el promedio de cada estudiante.
- Indicar si el estudiante aprueba o reprueba según una nota mínima.
- Mostrar un resumen general del curso.

### Restricciones según nivel
- Usar listas y/o diccionarios para almacenar la información.
- Separar la lógica en funciones.
- No usar bases de datos.
- Si aún no se han visto archivos, los datos pueden perderse al cerrar el programa.

### Extras opcionales
- Guardar y cargar datos desde un archivo `.txt` o `.csv`.
- Mostrar la nota más alta y la más baja.
- Ordenar estudiantes por promedio.

### Criterios de evaluación
- Los datos de estudiantes y notas se almacenan de forma organizada.
- Los promedios se calculan correctamente.
- El programa valida notas fuera del rango permitido.
- Las funciones tienen responsabilidades claras.

## Reto 2: Agenda simple usando listas

### Objetivo
Construir una agenda de contactos cuando el estudiante llegue al tema de listas.

### Requisitos
- Agregar contactos con nombre, teléfono y correo.
- Listar todos los contactos guardados.
- Buscar un contacto por nombre.
- Eliminar un contacto existente.
- Mostrar un menú para navegar por las opciones.

### Restricciones según nivel
- Usar listas como estructura principal.
- No usar bases de datos ni frameworks.
- Si todavía no se han visto diccionarios, representar cada contacto con listas internas.
- Separar el menú de las operaciones principales cuando ya se hayan visto funciones.

### Extras opcionales
- Editar datos de un contacto.
- Evitar contactos duplicados.
- Guardar la agenda en un archivo.

### Criterios de evaluación
- La agenda permite agregar, buscar, listar y eliminar contactos.
- La estructura de listas es comprensible.
- El programa maneja búsquedas sin resultados.
- El menú se repite hasta que el usuario elija salir.

## Reto 3: Inventario simple

### Objetivo
Crear un inventario para administrar productos y cantidades disponibles.

### Requisitos
- Agregar productos con nombre, cantidad y precio.
- Consultar productos existentes.
- Actualizar cantidades después de entradas o salidas.
- Calcular el valor total del inventario.
- Mostrar productos con bajo stock.

### Restricciones según nivel
- Usar listas, diccionarios y funciones.
- No usar bases de datos.
- Validar que cantidades y precios no sean negativos.
- Mantener la lógica separada de los mensajes de consola cuando sea posible.

### Extras opcionales
- Guardar y cargar inventario desde archivo.
- Buscar productos por coincidencia parcial del nombre.
- Generar un reporte ordenado por valor total del producto.

### Criterios de evaluación
- El inventario refleja correctamente entradas y salidas.
- El cálculo del valor total es correcto.
- Las validaciones evitan datos inconsistentes.
- El código está dividido en funciones reutilizables.

## Reto 4: Gestor de tareas

### Objetivo
Desarrollar una aplicación de consola para organizar tareas pendientes y completadas.

### Requisitos
- Crear tareas con título, descripción y estado.
- Listar tareas pendientes y completadas.
- Marcar tareas como completadas.
- Eliminar tareas.
- Filtrar tareas por estado.

### Restricciones según nivel
- Usar listas de diccionarios o una estructura equivalente.
- Implementar funciones para crear, listar, actualizar y eliminar.
- No usar frameworks web.
- La persistencia en archivos es opcional según el avance del curso.

### Extras opcionales
- Agregar fecha límite.
- Asignar prioridad alta, media o baja.
- Guardar los datos en JSON.

### Criterios de evaluación
- El usuario puede administrar el ciclo completo de una tarea.
- Los filtros muestran la información correcta.
- El programa conserva una estructura clara y fácil de ampliar.
- Las opciones inválidas del menú se manejan correctamente.
