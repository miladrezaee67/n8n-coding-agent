"""Small wrappers around Python's addition and subtraction operators.

The functions accept arbitrary operands and preserve Python's normal operator
dispatch, including custom operator implementations and reflected methods.
"""

from typing import Any


def add(a: Any, b: Any) -> Any:
    """Return ``a + b`` using Python's normal operator semantics.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The result produced by the addition operator.

    Raises:
        Any exception raised while evaluating the operation, including
        ``TypeError`` when the operands do not support addition.
    """
    return a + b


def subtract(a: Any, b: Any) -> Any:
    """Return ``a - b`` using Python's normal operator semantics.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The result produced by the subtraction operator.

    Raises:
        Any exception raised while evaluating the operation, including
        ``TypeError`` when the operands do not support subtraction.
    """
    return a - b