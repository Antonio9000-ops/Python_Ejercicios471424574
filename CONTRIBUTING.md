# Guía de contribución

Gracias por mejorar este repositorio de aprendizaje profesional. El objetivo es mantener una ruta clara, progresiva y fácil de revisar.

## Flujo recomendado

1. Crea o actualiza ejercicios respetando las restricciones del nivel.
2. Ejecuta los tests antes de confirmar cambios:

   ```bash
   make test
   ```

3. Revisa qué cambió:

   ```bash
   git status
   git diff
   ```

4. Crea commits pequeños y descriptivos.

## Conventional Commits

Usa el formato:

```text
tipo: descripción breve en imperativo
```

Tipos recomendados:

- `feat`: añade una funcionalidad, ejercicio, reto o automatización nueva.
- `fix`: corrige un bug, error de contenido o comportamiento incorrecto.
- `docs`: actualiza documentación, README o guías.
- `test`: añade o modifica pruebas automatizadas.
- `refactor`: mejora estructura interna sin cambiar comportamiento.
- `chore`: tareas de mantenimiento, configuración o dependencias.

Ejemplos:

```text
feat: añade generador de ejercicios
docs: documenta flujo de contribución
test: valida restricciones del generador
chore: configura GitHub Actions para pytest
```

## Estándares mínimos

- No adelantes temas en ejercicios básicos.
- Incluye docstrings claros en scripts y módulos.
- Prefiere nombres descriptivos sobre abreviaturas.
- Mantén los cambios enfocados para facilitar revisión.
- Si agregas automatización o estructura nueva, añade o actualiza tests.
