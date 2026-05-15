# Ruta de Python por niveles

Esta carpeta organiza el aprendizaje de Python con una regla central: cada archivo solo puede usar los temas ya estudiados. La progresión evita atajos y obliga a construir soluciones que puedas explicar en una entrevista técnica.

## Estructura

```text
python/
├── nivel_0_fundamentos/
├── nivel_1_basico/
├── nivel_2_intermedio/
├── nivel_3_avanzado/
├── nivel_4_especializaciones/
└── nivel_5_profesional/
```

## Reglas generales

- Cada archivo practica un concepto principal.
- No adelantes estructuras o herramientas que todavía no pertenecen al nivel.
- Prioriza nombres descriptivos y comentarios que expliquen intención.
- Mantén cada script ejecutable desde la raíz del repositorio.
- Usa docstrings para documentar objetivo, restricciones y forma de uso.

## Dependencias por tema en Nivel 1

| Archivo | Tema principal | Conceptos permitidos |
| --- | --- | --- |
| `01_variables_tipos.py` | Variables y tipos | Asignación, enteros, flotantes, booleanos y strings básicos. |
| `02_entrada_salida.py` | Entrada/salida | Conceptos anteriores, `print()` e `input()`. |
| `03_operadores.py` | Operadores | Conceptos anteriores, operadores aritméticos, comparación y lógica. |
| `04_condicionales.py` | Condicionales | Conceptos anteriores, `if`, `elif` y `else`. |
| `05_bucles.py` | Bucles | Conceptos anteriores, `while`, `for`, `range()`, contadores, acumuladores, `break` y `continue`. |
| `06_strings.py` | Cadenas de texto | Conceptos anteriores y operaciones básicas con strings. |
| `07_listas.py` | Listas | Conceptos anteriores y listas. |

## Restricción especial para `05_bucles.py`

En el archivo de bucles todavía no se deben usar:

- Listas.
- Tuplas.
- Diccionarios.
- Sets.
- Funciones propias.
- Clases.
- Archivos.
- Módulos externos.

Esta restricción permite concentrarse en la lógica de repetición sin mezclar temas futuros.

## Niveles futuros

- `nivel_2_intermedio`: funciones, módulos simples, manejo de errores, archivos y estructuras de datos con más profundidad.
- `nivel_3_avanzado`: programación orientada a objetos, iteradores, comprensión de datos, APIs y automatización.
- `nivel_4_especializaciones`: datos, backend, scripting profesional y automatización avanzada.
- `nivel_5_profesional`: arquitectura, testing avanzado, empaquetado, CI/CD, documentación y proyectos listos para portafolio.
