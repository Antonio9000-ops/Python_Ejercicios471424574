# Retos para nivel principiante

Estos retos están pensados para estudiantes que ya conocen variables, tipos básicos, entrada por teclado, salida por consola, operadores, condicionales y ciclos simples.

## Reto 1: Calculadora de consola

### Objetivo
Crear una calculadora que permita realizar operaciones matemáticas básicas desde la terminal.

### Requisitos
- Mostrar un menú con las operaciones: suma, resta, multiplicación y división.
- Pedir dos números al usuario.
- Mostrar el resultado de la operación seleccionada.
- Permitir realizar varias operaciones hasta que el usuario decida salir.

### Restricciones según nivel
- Usar solo variables, condicionales, ciclos y operaciones aritméticas.
- No usar funciones si todavía no se han estudiado.
- No usar librerías externas.
- Validar como mínimo la división entre cero.

### Extras opcionales
- Agregar potencia y módulo.
- Mostrar un historial simple durante la ejecución.
- Aceptar números decimales.

### Criterios de evaluación
- El menú es claro y fácil de usar.
- Cada operación devuelve el resultado correcto.
- El programa no se rompe al dividir entre cero.
- El usuario puede salir del programa de forma controlada.

## Reto 2: Conversor de monedas ficticio

### Objetivo
Construir un conversor que transforme una cantidad entre monedas inventadas usando tasas fijas definidas en el programa.

### Requisitos
- Definir al menos tres monedas ficticias, por ejemplo: Solarios, Lunarios y Estrellas.
- Mostrar las monedas disponibles.
- Pedir moneda de origen, moneda de destino y cantidad.
- Calcular y mostrar el valor convertido.

### Restricciones según nivel
- Usar tasas de conversión fijas escritas directamente en el código.
- Usar condicionales para decidir qué conversión aplicar.
- No consultar APIs reales ni archivos externos.
- No usar diccionarios si todavía no se han estudiado.

### Extras opcionales
- Permitir varias conversiones en una misma ejecución.
- Rechazar cantidades negativas.
- Mostrar la tasa usada en la conversión.

### Criterios de evaluación
- Las monedas disponibles se entienden claramente.
- El cálculo coincide con las tasas definidas.
- El programa maneja opciones inválidas sin cerrarse inesperadamente.
- La salida muestra cantidad original, moneda origen, resultado y moneda destino.

## Reto 3: Juego de adivinanza

### Objetivo
Crear un juego en el que el usuario intente adivinar un número secreto.

### Requisitos
- Generar o definir un número secreto.
- Pedir intentos al usuario hasta que acierte.
- Indicar si el número ingresado es mayor o menor que el secreto.
- Mostrar la cantidad de intentos usados al finalizar.

### Restricciones según nivel
- Si aún no se han visto módulos, el número secreto puede estar escrito en el código.
- Si ya se vio `random`, se puede usar para generar el número.
- Usar ciclos y condicionales simples.
- No usar interfaces gráficas.

### Extras opcionales
- Limitar la cantidad de intentos.
- Agregar niveles de dificultad con rangos diferentes.
- Preguntar si el usuario quiere jugar otra partida.

### Criterios de evaluación
- El juego da pistas correctas después de cada intento.
- El programa detecta correctamente cuando el usuario gana.
- El contador de intentos es correcto.
- El flujo de inicio, juego y finalización es claro.
