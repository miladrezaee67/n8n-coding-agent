"""Small wrappers around Python's addition and subtraction operators.

The functions delegate directly to Python's native operator dispatch, including
custom and reflected operator methods.
"""

from typing import Any

__all__ = ["add", "subtract"]


def add(a: Any, b: Any) -> Any:
    """Return the result of applying ``+`` to two operands.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The value produced by ``a + b``.

    Any exception raised during operator dispatch propagates unchanged.
    """
    return a + b


def subtract(a: Any, b: Any) -> Any:
    """Return the result of applying ``-`` to two operands.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The value produced by ``a - b``.

    Any exception raised during operator dispatch propagates unchanged.
    """
    return a - b