"""Ejercicios progresivos de bucles para Nivel 1 básico.

Objetivo:
    Practicar `while`, `for`, `range()`, contadores, acumuladores,
    `break` y `continue` usando únicamente temas ya estudiados.

Restricciones del nivel:
    - Permitido: variables, `input()`, `print()`, operadores,
      condicionales, strings básicos y bucles.
    - No usar todavía: listas, tuplas, diccionarios, sets, funciones
      propias, clases, archivos, módulos externos ni comprensión de datos.

Cómo usar este archivo:
    1. Lee cada enunciado antes de mirar la demostración.
    2. Comenta o descomenta bloques dentro de `if __name__ == "__main__"`.
    3. Reescribe cada solución desde cero en tu editor.
    4. Ejecuta desde la raíz del repositorio con:
       `python python/nivel_1_basico/05_bucles.py`.

Nota didáctica:
    Este script contiene ejemplos ejecutables y enunciados guiados. Evita
    adelantar estructuras de datos para que el foco esté en controlar el
    flujo del programa paso a paso.
"""

# =============================================================================
# GUÍA DE EJERCICIOS
# =============================================================================
# Los ejercicios están ordenados de menor a mayor dificultad. En este punto del
# camino todavía se busca dominar el razonamiento con contadores, acumuladores y
# condiciones de parada antes de usar estructuras de datos más avanzadas.

EJERCICIO_01 = "Muestra los números del 1 al 10 usando un bucle while."
EJERCICIO_02 = "Muestra los números del 1 al 10 usando for y range()."
EJERCICIO_03 = "Muestra los números del 10 al 1 usando while."
EJERCICIO_04 = "Pide una palabra e imprime cada carácter en una línea."
EJERCICIO_05 = "Suma los números del 1 al 100 usando un acumulador."
EJERCICIO_06 = "Pide un número y muestra su tabla de multiplicar."
EJERCICIO_07 = "Pide números hasta que el usuario escriba 0 y suma todo."
EJERCICIO_08 = "Pide una contraseña hasta que sea correcta."
EJERCICIO_09 = "Imprime los pares del 2 al 20 y salta los impares."
EJERCICIO_10 = "Cuenta cuántas vocales tiene una palabra."
EJERCICIO_11 = "Calcula el factorial de un número positivo."
EJERCICIO_12 = "Crea un patrón de asteriscos con bucles anidados."
RETO_FINAL = "Mini proyecto: juego de adivinanza con máximo de intentos."


if __name__ == "__main__":
    print("Nivel 1 básico - 05 Bucles")
    print("================================")
    print("Este archivo muestra soluciones guiadas para practicar bucles.")
    print("No usa listas, tuplas ni diccionarios por regla pedagógica.")
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 1: while con contador ascendente.
    # Un contador necesita tres partes: valor inicial, condición y actualización.
    # -------------------------------------------------------------------------
    print("Ejercicio 1: números del 1 al 10 con while")
    contador = 1
    while contador <= 10:
        print(contador)
        contador = contador + 1
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 2: for con range().
    # range(1, 11) produce valores desde 1 hasta 10. El 11 no se incluye.
    # -------------------------------------------------------------------------
    print("Ejercicio 2: números del 1 al 10 con for")
    for numero in range(1, 11):
        print(numero)
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 3: while descendente.
    # En cuentas regresivas la actualización debe restar para acercarse al final.
    # -------------------------------------------------------------------------
    print("Ejercicio 3: números del 10 al 1 con while")
    contador = 10
    while contador >= 1:
        print(contador)
        contador = contador - 1
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 4: recorrer un string.
    # Una cadena puede recorrerse carácter por carácter sin usar listas.
    # -------------------------------------------------------------------------
    print("Ejercicio 4: caracteres de una palabra fija")
    palabra = "python"
    for caracter in palabra:
        print(caracter)
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 5: acumulador.
    # Un acumulador guarda un resultado parcial que crece en cada vuelta.
    # -------------------------------------------------------------------------
    print("Ejercicio 5: suma del 1 al 100")
    suma_total = 0
    for numero in range(1, 101):
        suma_total = suma_total + numero
    print("Resultado:", suma_total)
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 6: tabla de multiplicar.
    # Cambia este valor por input() cuando quieras practicar entrada del usuario.
    # Ejemplo: numero_tabla = int(input("Número para la tabla: "))
    # -------------------------------------------------------------------------
    print("Ejercicio 6: tabla de multiplicar")
    numero_tabla = 5
    multiplicador = 1
    while multiplicador <= 10:
        resultado = numero_tabla * multiplicador
        print(numero_tabla, "x", multiplicador, "=", resultado)
        multiplicador = multiplicador + 1
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 7: suma con centinela.
    # Un valor centinela indica cuándo detener el bucle. Aquí el centinela es 0.
    # La versión interactiva queda comentada para que el script sea fácil de
    # ejecutar completo durante revisiones automáticas.
    # -------------------------------------------------------------------------
    print("Ejercicio 7: estructura de suma hasta escribir 0")
    print("Practica cambiando numero_ingresado por int(input(...)).")
    suma_total = 0
    numero_ingresado = 3
    while numero_ingresado != 0:
        suma_total = suma_total + numero_ingresado
        print("Suma parcial:", suma_total)
        numero_ingresado = numero_ingresado - 1
    print("Suma final de demostración:", suma_total)
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 8: contraseña con while.
    # En una práctica real, reemplaza intento por input("Contraseña: ").
    # -------------------------------------------------------------------------
    print("Ejercicio 8: validación de contraseña")
    password_correcto = "python123"
    intento = "python123"
    while intento != password_correcto:
        print("Contraseña incorrecta. Intenta otra vez.")
        intento = password_correcto
    print("Acceso permitido")
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 9: continue para saltar valores.
    # continue termina la vuelta actual y pasa al siguiente ciclo.
    # -------------------------------------------------------------------------
    print("Ejercicio 9: números pares del 2 al 20")
    for numero in range(1, 21):
        if numero % 2 != 0:
            continue
        print(numero)
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 10: contar vocales.
    # Se evita usar colecciones. Por eso se compara cada vocal explícitamente.
    # -------------------------------------------------------------------------
    print("Ejercicio 10: contador de vocales")
    palabra = "arquitectura"
    vocales = 0
    for caracter in palabra:
        if caracter == "a":
            vocales = vocales + 1
        elif caracter == "e":
            vocales = vocales + 1
        elif caracter == "i":
            vocales = vocales + 1
        elif caracter == "o":
            vocales = vocales + 1
        elif caracter == "u":
            vocales = vocales + 1
    print("La palabra", palabra, "tiene", vocales, "vocales.")
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 11: factorial.
    # El factorial multiplica todos los enteros positivos desde 1 hasta n.
    # -------------------------------------------------------------------------
    print("Ejercicio 11: factorial")
    numero_factorial = 5
    factorial = 1
    contador = 1
    while contador <= numero_factorial:
        factorial = factorial * contador
        contador = contador + 1
    print("Factorial de", numero_factorial, "=", factorial)
    print()

    # -------------------------------------------------------------------------
    # Ejercicio 12: bucles anidados.
    # El bucle externo controla filas; el interno construye el contenido visual.
    # -------------------------------------------------------------------------
    print("Ejercicio 12: patrón de asteriscos")
    filas = 5
    fila_actual = 1
    while fila_actual <= filas:
        columna_actual = 1
        linea = ""
        while columna_actual <= fila_actual:
            linea = linea + "*"
            columna_actual = columna_actual + 1
        print(linea)
        fila_actual = fila_actual + 1
    print()

    # -------------------------------------------------------------------------
    # Reto final: juego de adivinanza.
    # Para practicarlo de verdad, sustituye intento_actual por input() y conserva
    # la condición de intentos máximos para evitar bucles infinitos.
    # -------------------------------------------------------------------------
    print("Reto final: juego de adivinanza")
    numero_secreto = 7
    intento_actual = 7
    intentos_usados = 0
    maximo_intentos = 5
    adivinado = False

    while intentos_usados < maximo_intentos:
        intentos_usados = intentos_usados + 1

        if intento_actual == numero_secreto:
            print("¡Victoria! Adivinaste en", intentos_usados, "intento.")
            adivinado = True
            break

        if intento_actual < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

    if not adivinado:
        print("Fin del juego. El número secreto era", numero_secreto)
