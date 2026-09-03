"""Small utility functions for Python's addition and subtraction operators.

The functions in this module intentionally accept arbitrary operands and
delegate directly to Python's operator implementations. This preserves
operator overloading and the exceptions raised for unsupported operands.
"""

from typing import Any


def add(a: Any, b: Any) -> Any:
    """Return ``a + b``.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The result produced by Python's addition operator.

    Raises:
        Any exception raised by the operands' ``__add__`` or ``__radd__``
        implementations, including ``TypeError`` for unsupported operands.
    """
    return a + b


def subtract(a: Any, b: Any) -> Any:
    """Return ``a - b``.

    Args:
        a: The left operand.
        b: The right operand.

    Returns:
        The result produced by Python's subtraction operator.

    Raises:
        Any exception raised by the operands' ``__sub__`` or ``__rsub__``
        implementations, including ``TypeError`` for unsupported operands.
    """
    return a - b