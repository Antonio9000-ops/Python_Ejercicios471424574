"""Pruebas de restricciones para el módulo básico de bucles."""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUCLES_FILE = ROOT / "python" / "nivel_1_basico" / "05_bucles.py"


def parse_bucles_file():
    """Devuelve el árbol sintáctico del archivo de bucles."""
    return ast.parse(BUCLES_FILE.read_text(encoding="utf-8"))


def test_bucles_file_has_module_docstring():
    """El archivo debe explicar objetivo, restricciones y uso."""
    tree = parse_bucles_file()

    assert ast.get_docstring(tree)


def test_bucles_file_avoids_future_data_structures():
    """Nivel 1 no debe adelantar listas, tuplas ni diccionarios."""
    tree = parse_bucles_file()
    forbidden_nodes = (ast.List, ast.Tuple, ast.Dict, ast.Set, ast.ListComp)

    for node in ast.walk(tree):
        assert not isinstance(node, forbidden_nodes), (
            "05_bucles.py no debe usar listas, tuplas, diccionarios ni sets"
        )


def test_bucles_file_uses_loops_and_guard():
    """El material debe practicar bucles y poder importarse sin interacción."""
    source = BUCLES_FILE.read_text(encoding="utf-8")
    tree = parse_bucles_file()

    has_for = any(isinstance(node, ast.For) for node in ast.walk(tree))
    has_while = any(isinstance(node, ast.While) for node in ast.walk(tree))

    assert has_for
    assert has_while
    assert 'if __name__ == "__main__"' in source
