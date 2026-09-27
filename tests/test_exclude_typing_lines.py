"""Tests for the script that filters the typing coverage report."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import re

import pytest

tomllib = pytest.importorskip('tomllib')

ROOT = Path(__file__).parent.parent
_spec = importlib.util.spec_from_file_location(
    'exclude_typing_lines', ROOT / '.github' / 'exclude_typing_lines.py'
)
assert _spec is not None
assert _spec.loader is not None
exclude_typing_lines = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(exclude_typing_lines)

PATTERNS = [
    re.compile(p, re.MULTILINE)
    for p in tomllib.loads((ROOT / 'pyproject.toml').read_text())['tool']['coverage']['report'][
        'exclude_also'
    ]
]

def excluded(source: str) -> list[int]:
    """Return the sorted line numbers the project patterns exclude from ``source``."""
    return sorted(exclude_typing_lines.excluded_lines(source, PATTERNS))


def test_one_line_overload():
    source = 'x = 1\n\n@overload\ndef f(a: int) -> int: ...\ndef f(a): return a\n'
    assert excluded(source) == [3, 4]


def test_multi_line_overload():
    source = '@overload\ndef f(\n    a: int,\n) -> int: ...\ndef f(a):\n    return a\n'
    assert excluded(source) == [1, 2, 3, 4]


def test_type_checking_block():
    source = 'if TYPE_CHECKING:\n    import a\n\n    import b\nelse:\n    a = 1\n'
    assert excluded(source) == [1, 2, 3, 4]


def test_type_checking_block_with_comment():
    source = 'if TYPE_CHECKING:  # typing only\n    import a\nx = 1\n'
    assert excluded(source) == [1, 2]
