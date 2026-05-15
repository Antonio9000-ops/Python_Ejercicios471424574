"""Pruebas de calidad para la estructura educativa del repositorio."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_expected_learning_directories_exist():
    """Comprueba que la ruta de aprendizaje principal exista."""
    expected_directories = [
        "python/nivel_0_fundamentos",
        "python/nivel_1_basico",
        "python/nivel_2_intermedio",
        "python/nivel_3_avanzado",
        "python/nivel_4_especializaciones",
        "python/nivel_5_profesional",
        "proyectos_retos",
        "tests",
    ]

    for directory in expected_directories:
        assert (ROOT / directory).is_dir(), f"Falta el directorio {directory}"


def test_core_documentation_files_exist():
    """Verifica documentación mínima para uso profesional del repositorio."""
    expected_files = [
        "README.md",
        "RUTA_PROFESIONAL.md",
        ".gitignore",
        "python/README.md",
        "proyectos_retos/README.md",
        "CONTRIBUTING.md",
        "requirements.txt",
        "Makefile",
        ".github/workflows/python-app.yml",
        "scripts/generar_ejercicio.py",
    ]

    for file_path in expected_files:
        assert (ROOT / file_path).is_file(), f"Falta el archivo {file_path}"
