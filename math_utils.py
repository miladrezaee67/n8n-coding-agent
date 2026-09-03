"""Utilities that delegate to Python's addition and subtraction operators.

The functions in this module accept arbitrary operands, preserving normal
operator overloading and exception behavior.
"""

from typing import Any


def add(a: Any, b: Any) -> Any:
    """Return the result of evaluating ``a + b``.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The value produced by Python's addition operator.

    Raises:
        Any exception raised during operator dispatch, including ``TypeError``
        when the operands do not support addition.
    """
    return a + b


def subtract(a: Any, b: Any) -> Any:
    """Return the result of evaluating ``a - b``.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The value produced by Python's subtraction operator.

    Raises:
        Any exception raised during operator dispatch, including ``TypeError``
        when the operands do not support subtraction.
    """
    return a - b