"""Small arithmetic utility functions."""

from typing import Any


def add(a: Any, b: Any) -> Any:
    """Return the result of applying Python's addition operator to ``a`` and ``b``.

    The operands may be any values that support the ``+`` operator. Python's
    normal behavior and exceptions are preserved for unsupported operands.
    """
    return a + b


def subtract(a: Any, b: Any) -> Any:
    """Return the result of applying Python's subtraction operator to ``a`` and ``b``.

    The operands may be any values that support the ``-`` operator. Python's
    normal behavior and exceptions are preserved for unsupported operands.
    """
    return a - b