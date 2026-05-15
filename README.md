# Python Ejercicios: ruta profesional de aprendizaje

Repositorio de práctica diseñado para aprender Python de forma progresiva y demostrar competencia técnica en entrevistas. El objetivo no es acumular archivos sueltos, sino construir una evidencia clara de crecimiento: ejercicios con restricciones explícitas, retos de portafolio, tests automatizados y documentación profesional.

## Objetivos del repositorio

- Aprender Python por niveles, sin adelantar temas antes de dominarlos.
- Practicar Clean Code desde el primer día: nombres claros, comentarios útiles y archivos ordenados.
- Preparar una base para entrevistas técnicas mediante ejercicios, retos y documentación.
- Introducir testing con `pytest` y control de versiones con Git como hábitos profesionales.
- Conectar Python con rutas complementarias de JavaScript/TypeScript y SQL.

## Estructura principal

```text
.
├── python/
│   ├── nivel_0_fundamentos/
│   ├── nivel_1_basico/
│   ├── nivel_2_intermedio/
│   ├── nivel_3_avanzado/
│   ├── nivel_4_especializaciones/
│   └── nivel_5_profesional/
├── proyectos_retos/
├── tests/
├── RUTA_PROFESIONAL.md
└── README.md
```

## Cómo estudiar los ejercicios

1. Lee el docstring inicial de cada archivo para entender objetivo, restricciones y forma de ejecución.
2. Resuelve los ejercicios en orden. Si un concepto no aparece todavía en la ruta, no lo uses.
3. Ejecuta cada script desde la raíz del repositorio. Por ejemplo:

   ```bash
   python python/nivel_1_basico/05_bucles.py
   ```

4. Convierte cada ejercicio en evidencia: guarda soluciones limpias, mensajes de commit claros y notas de aprendizaje.
5. Cuando termines un bloque, pasa a un reto de `proyectos_retos/` para integrar lo aprendido.

## Regla de no adelantar temas

Este repositorio prioriza la progresión. Por ejemplo, en `python/nivel_1_basico/05_bucles.py` solo se permiten variables, entrada/salida, operadores, condicionales y bucles. No se usan listas, tuplas, diccionarios, funciones propias, archivos, módulos externos ni POO.

La regla existe para que puedas explicar cada línea en una entrevista y evitar soluciones que dependen de herramientas que todavía no han sido estudiadas.

## Tests automatizados

La carpeta `tests/` contiene verificaciones iniciales de calidad. Para ejecutarlas:

```bash
python -m pytest
```

Los tests actuales validan estructura, documentación y restricciones del material básico. A medida que el repositorio crezca, añade pruebas para funciones, proyectos y casos de borde.

## Cómo abordar los retos

Cada reto debe resolverse como un mini proyecto profesional:

- Define el problema con tus palabras.
- Escribe una versión mínima funcional antes de añadir extras.
- Refactoriza nombres, duplicación y estructura.
- Documenta decisiones importantes.
- Añade pruebas cuando el nivel ya permita funciones y módulos.
- Crea commits pequeños: uno por mejora o funcionalidad.

## Uso de IA como tutor, no como sustituto

Puedes usar IA para acelerar el aprendizaje, pero mantén el control técnico:

- Pide pistas antes de pedir soluciones completas.
- Solicita revisión de tu código con foco en legibilidad, bugs y estilo.
- Pregunta por casos de prueba que no hayas considerado.
- Pide explicaciones línea por línea cuando algo no sea claro.
- Evita copiar código que no puedas explicar sin ayuda.

Prompt útil:

> Estoy aprendiendo Python en nivel básico. No me des la solución completa. Dame una pista para resolver este ejercicio usando solo variables, input, print, operadores, condicionales y bucles.

## Flujo profesional recomendado

```bash
git status
git add .
git commit -m "Añade ejercicios de bucles y ruta profesional"
python -m pytest
```

Consulta `RUTA_PROFESIONAL.md` para ver el roadmap completo hacia empleabilidad.
