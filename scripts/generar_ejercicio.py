"""Generador de plantillas para nuevos ejercicios del repositorio.

El script solicita una ruta o nombre de ejercicio y crea automáticamente la
carpeta necesaria junto con un archivo `.py` que incluye un docstring inicial,
comentarios guía y un bloque `if __name__ == "__main__"`.

Ejemplos de entrada válidos:
    - 08_funciones
    - nivel_1_basico/08_funciones
    - python/nivel_2_intermedio/01_funciones.py

Por seguridad, el generador rechaza rutas absolutas y rutas con `..` para evitar
crear archivos fuera del repositorio.
"""

from pathlib import Path

DEFAULT_BASE_DIRECTORY = Path("python") / "nivel_1_basico"
DEFAULT_EXTENSION = ".py"


def normalize_exercise_path(raw_name, repository_root):
    """Convierte la entrada del usuario en una ruta segura dentro del repo."""
    cleaned_name = raw_name.strip().replace("\\", "/")

    if not cleaned_name:
        raise ValueError("El nombre del ejercicio no puede estar vacío.")

    candidate = Path(cleaned_name)

    if candidate.is_absolute():
        raise ValueError("Usa una ruta relativa, no una ruta absoluta.")

    if ".." in candidate.parts:
        raise ValueError("La ruta no puede contener '..'.")

    if candidate.suffix != DEFAULT_EXTENSION:
        candidate = candidate.with_suffix(DEFAULT_EXTENSION)

    if candidate.parts and candidate.parts[0] == "python":
        relative_path = candidate
    elif len(candidate.parts) > 1:
        relative_path = Path("python") / candidate
    else:
        relative_path = DEFAULT_BASE_DIRECTORY / candidate

    final_path = (repository_root / relative_path).resolve()
    resolved_root = repository_root.resolve()

    if resolved_root not in final_path.parents:
        raise ValueError("La ruta final debe permanecer dentro del repositorio.")

    return final_path


def build_template(exercise_path):
    """Construye el contenido base de un archivo de ejercicio nuevo."""
    title = exercise_path.stem.replace("_", " ").title()

    return f'''"""{title}.

Objetivo:
    Describe aquí el concepto principal que se practicará en este ejercicio.

Restricciones:
    Usa únicamente los temas permitidos para el nivel correspondiente.

Cómo ejecutar:
    python {exercise_path.as_posix()}
"""

# Escribe instrucciones claras antes de implementar la solución.
# Mantén nombres descriptivos y comentarios que expliquen decisiones.


if __name__ == "__main__":
    print("Ejercicio: {title}")
    print("Completa este archivo siguiendo las reglas del nivel.")
'''


def create_exercise(raw_name, repository_root):
    """Crea la carpeta y el archivo base del nuevo ejercicio."""
    exercise_path = normalize_exercise_path(raw_name, repository_root)

    if exercise_path.exists():
        raise FileExistsError(f"El archivo ya existe: {exercise_path}")

    exercise_path.parent.mkdir(parents=True, exist_ok=True)
    relative_path = exercise_path.relative_to(repository_root.resolve())
    exercise_path.write_text(build_template(relative_path), encoding="utf-8")

    return exercise_path


def main():
    """Solicita el nombre del ejercicio y crea la plantilla correspondiente."""
    repository_root = Path(__file__).resolve().parents[1]
    raw_name = input("Nombre o ruta del nuevo ejercicio: ")

    try:
        exercise_path = create_exercise(raw_name, repository_root)
    except (ValueError, FileExistsError) as error:
        print(f"No se pudo crear el ejercicio: {error}")
        raise SystemExit(1) from error

    relative_path = exercise_path.relative_to(repository_root)
    print(f"Ejercicio creado correctamente: {relative_path}")


if __name__ == "__main__":
    main()
