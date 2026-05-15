"""Pruebas del generador de plantillas de ejercicios."""

from pathlib import Path

import pytest

from scripts.generar_ejercicio import create_exercise, normalize_exercise_path


def test_create_exercise_from_simple_name(tmp_path):
    """Un nombre simple debe crear un ejercicio en nivel 1 básico."""
    exercise_path = create_exercise("08_funciones", tmp_path)

    expected_path = tmp_path / "python" / "nivel_1_basico" / "08_funciones.py"
    content = expected_path.read_text(encoding="utf-8")

    assert exercise_path == expected_path
    assert expected_path.is_file()
    assert '"""08 Funciones.' in content
    assert 'if __name__ == "__main__"' in content


def test_create_exercise_from_nested_level_path(tmp_path):
    """Una ruta por nivel debe quedar dentro de la carpeta python."""
    exercise_path = create_exercise("nivel_2_intermedio/01_funciones.py", tmp_path)

    expected_path = tmp_path / "python" / "nivel_2_intermedio" / "01_funciones.py"

    assert exercise_path == expected_path
    assert expected_path.is_file()


def test_create_exercise_from_full_python_path(tmp_path):
    """Una ruta que ya inicia con python debe respetarse."""
    exercise_path = create_exercise(
        "python/nivel_3_avanzado/01_modulos.py",
        tmp_path,
    )

    expected_path = tmp_path / "python" / "nivel_3_avanzado" / "01_modulos.py"

    assert exercise_path == expected_path
    assert expected_path.is_file()


def test_create_exercise_does_not_overwrite_existing_file(tmp_path):
    """El generador debe proteger ejercicios existentes."""
    create_exercise("08_funciones", tmp_path)

    with pytest.raises(FileExistsError):
        create_exercise("08_funciones", tmp_path)


def test_normalize_exercise_path_rejects_unsafe_paths(tmp_path):
    """El generador debe rechazar rutas absolutas y navegación hacia atrás."""
    with pytest.raises(ValueError):
        normalize_exercise_path("../secreto", tmp_path)

    with pytest.raises(ValueError):
        normalize_exercise_path(str(Path("/") / "tmp" / "ejercicio.py"), tmp_path)
