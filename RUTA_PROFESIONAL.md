# Ruta profesional hacia empleabilidad con Python

Esta ruta transforma ejercicios aislados en una trayectoria de aprendizaje orientada a entrevistas, proyectos y trabajo real. Está pensada para avanzar por capas: fundamentos sólidos, calidad de código, testing, colaboración y especialización.

## Principios de la ruta

- **Progresión estricta:** no usar conceptos antes de estudiarlos.
- **Código explicable:** cada solución debe poder defenderse en voz alta.
- **Evidencia pública:** commits, README, retos y tests muestran madurez técnica.
- **Calidad incremental:** primero funciona, luego se limpia, luego se prueba.
- **Aprendizaje complementario:** Python se potencia con SQL y JavaScript/TypeScript.

## Fase 0: fundamentos de programación

**Objetivo:** comprender cómo piensa un programa.

Temas:

- Variables y tipos básicos.
- Entrada y salida con `input()` y `print()`.
- Operadores aritméticos, comparación y lógica.
- Condicionales.
- Bucles `while` y `for`.
- Strings básicos.

Evidencia esperada:

- Ejercicios resueltos sin copiar.
- Comentarios que expliquen intención, no obviedades.
- Primeros commits con mensajes claros.

## Fase 1: Python básico sólido

**Objetivo:** escribir programas pequeños con control de flujo claro.

Temas:

- Listas y recorridos.
- Funciones simples.
- Validación de datos.
- Separación de responsabilidades.
- Lectura de errores comunes.

Buenas prácticas:

- Nombres descriptivos.
- Evitar duplicación.
- Usar docstrings en archivos y funciones cuando correspondan.
- Mantener scripts pequeños y enfocados.

## Fase 2: Clean Code aplicado

**Objetivo:** que el código sea fácil de leer, modificar y revisar.

Temas:

- Funciones con una sola responsabilidad.
- Parámetros y valores de retorno claros.
- Separación entre lógica y entrada/salida.
- Constantes para valores significativos.
- Refactorización segura.

Criterio profesional:

> Si otra persona puede leer tu solución, ejecutar pruebas y extenderla sin preguntarte cómo funciona, vas por buen camino.

## Fase 3: testing con pytest

**Objetivo:** demostrar que el código funciona y que sabes prevenir regresiones.

Temas:

- Instalación y ejecución de `pytest`.
- Tests unitarios.
- Casos normales, límites y errores.
- Organización `tests/test_*.py`.
- Cobertura como guía, no como fin.

Comandos base:

```bash
python -m pytest
python -m pytest -q
```

Evidencia para entrevistas:

- Tests legibles.
- Casos de borde documentados.
- Bugs corregidos con test previo o posterior.

## Fase 4: control de versiones con Git

**Objetivo:** trabajar como en un equipo profesional.

Temas:

- `git status`, `git add`, `git commit`.
- Ramas por funcionalidad.
- Pull requests con descripción clara.
- Commits pequeños y reversibles.
- Uso de `.gitignore`.

Convención sugerida:

```text
feat: añade ejercicios de bucles
fix: corrige validación de entrada
 docs: actualiza roadmap profesional
test: agrega pruebas de estructura
```

## Fase 5: proyectos de portafolio

**Objetivo:** integrar conocimientos en proyectos demostrables.

Tipos de proyectos:

- Calculadoras y validadores CLI.
- Gestores de tareas en terminal.
- Analizadores de texto.
- Automatizaciones de archivos.
- APIs simples.
- Dashboards o scripts de análisis de datos.

Cada proyecto debe incluir:

- README propio.
- Instrucciones de ejecución.
- Decisiones técnicas.
- Tests cuando aplique.
- Capturas o ejemplos de uso.

## Fase 6: SQL para complementar Python

**Objetivo:** trabajar con datos de forma profesional.

Temas estratégicos:

- Modelo relacional.
- `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`.
- Joins.
- Agregaciones.
- Diseño básico de tablas.
- Integración Python + SQLite/PostgreSQL.

Proyectos sugeridos:

- Registro de gastos con SQLite.
- Sistema de inventario.
- Reportes automáticos desde una base de datos.

## Fase 7: JavaScript/TypeScript como expansión

**Objetivo:** complementar Python con desarrollo web moderno.

Ruta recomendada:

- JavaScript moderno: variables, funciones, arrays, objetos y módulos.
- TypeScript: tipos, interfaces y modelos de dominio.
- Frontend: HTML, CSS y consumo de APIs.
- Backend: Node.js básico o integración con APIs Python.

Estrategia:

- Usa Python para lógica, automatización, datos y backend.
- Usa TypeScript para interfaces web y aplicaciones cliente.
- Usa SQL como idioma común para persistencia.

## Fase 8: preparación de entrevistas

**Objetivo:** convertir aprendizaje en empleabilidad.

Practica:

- Explicar decisiones técnicas.
- Resolver ejercicios en voz alta.
- Leer código ajeno.
- Depurar errores sin pánico.
- Hablar de trade-offs.

Checklist antes de postular:

- Perfil de GitHub ordenado.
- 2 a 4 proyectos con README profesional.
- Tests en proyectos principales.
- Commits claros.
- Capacidad de explicar Python básico, funciones, estructuras, archivos, APIs, SQL y Git.

## Métrica de avance

No midas progreso por horas ni cantidad de tutoriales. Mídelo por evidencia:

- ¿Qué construiste?
- ¿Qué puedes explicar?
- ¿Qué errores sabes diagnosticar?
- ¿Qué pruebas respaldan tu código?
- ¿Qué proyecto demuestra que puedes aportar valor?
