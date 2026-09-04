"""Small wrappers around Python's addition and subtraction operators.

The functions accept arbitrary operands and delegate directly to Python's
standard operator dispatch, including custom and reflected operator methods.
"""

from typing import Any

__all__ = ["add", "subtract"]


def add(a: Any, b: Any) -> Any:
    """Return the result of applying the ``+`` operator to two operands.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The value produced by ``a + b``.

    Raises:
        Exception: Any exception raised while evaluating ``a + b``.
    """
    return a + b


def subtract(a: Any, b: Any) -> Any:
    """Return the result of applying the ``-`` operator to two operands.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The value produced by ``a - b``.

    Raises:
        Exception: Any exception raised while evaluating ``a - b``.
    """
    return a - b