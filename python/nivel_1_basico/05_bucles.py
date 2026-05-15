# Ejercicios de bucles en Python
# Nivel 1 - Básico
#
# Objetivo:
# Practicar el uso de bucles while y for, range(), contadores,
# acumuladores, validación de entrada, break, continue y bucles anidados.
#
# Importante:
# - Todavía no uses listas, diccionarios, funciones ni archivos.
# - Resuelve cada ejercicio usando solo variables, input(), print(), if/else
#   y los bucles indicados.
# - Puedes comentar y descomentar tus soluciones a medida que practiques.


# 1. Imprimir números del 1 al 10 con while.
#
# Crea una variable contador que empiece en 1.
# Usa un bucle while para imprimir los números del 1 al 10.
# No olvides aumentar el contador dentro del bucle para evitar un bucle infinito.


# 2. Imprimir números del 1 al 10 con for y range().
#
# Usa un bucle for junto con range() para mostrar los números del 1 al 10.
# Recuerda que el límite superior de range() no se incluye.


# 3. Pedir números hasta que el usuario escriba 0.
#
# Pide números al usuario dentro de un bucle.
# El programa debe seguir pidiendo números mientras el usuario no escriba 0.
# Cuando escriba 0, el bucle debe terminar y se debe mostrar un mensaje final.


# 4. Sumar números del 1 al 100.
#
# Crea una variable acumulador que empiece en 0.
# Recorre los números del 1 al 100 usando while o for.
# En cada vuelta, suma el número actual al acumulador.
# Al final, muestra el resultado total.


# 5. Mostrar una tabla de multiplicar.
#
# Pide al usuario un número entero.
# Muestra su tabla de multiplicar del 1 al 10.
# Ejemplo: si el usuario escribe 5, muestra 5 x 1, 5 x 2, ..., 5 x 10.


# 6. Crear un contador regresivo.
#
# Pide al usuario un número inicial.
# Usa un bucle para mostrar una cuenta regresiva desde ese número hasta 0.
# Al llegar a 0, muestra un mensaje como "¡Despegue!".


# 7. Pedir contraseña hasta que sea correcta.
#
# Guarda una contraseña correcta en una variable.
# Pide al usuario que escriba la contraseña.
# Mientras la contraseña sea incorrecta, vuelve a pedirla.
# Cuando sea correcta, muestra un mensaje de acceso permitido.


# 8. Juego de adivinar número usando intentos.
#
# Guarda un número secreto en una variable.
# Pide al usuario que intente adivinarlo.
# Usa un contador de intentos para limitar la cantidad de oportunidades.
# Si el usuario acierta, muestra un mensaje de victoria y termina el bucle.
# Si se acaban los intentos, muestra un mensaje indicando el número secreto.


# 9. Imprimir solo números pares.
#
# Recorre los números del 1 al 50.
# Imprime solamente los números pares.
# Puedes usar el operador módulo (%) para comprobar si un número es divisible entre 2.


# 10. Saltar múltiplos de 3 usando continue.
#
# Recorre los números del 1 al 30.
# Si un número es múltiplo de 3, usa continue para saltarlo.
# Imprime solo los números que no sean múltiplos de 3.


# 11. Detener un bucle cuando el número sea mayor que 50 usando break.
#
# Pide números al usuario dentro de un bucle.
# Si el usuario escribe un número mayor que 50, usa break para terminar el bucle.
# Después del bucle, muestra un mensaje indicando que el programa terminó.


# 12. Crear un patrón de asteriscos con bucles anidados.
#
# Pide al usuario la cantidad de filas del patrón.
# Usa un bucle externo para controlar las filas.
# Usa un bucle interno para imprimir los asteriscos de cada fila.
# Ejemplo para 5 filas:
# *
# **
# ***
# ****
# *****
