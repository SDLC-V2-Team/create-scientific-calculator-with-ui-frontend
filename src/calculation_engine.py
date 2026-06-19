"""
Calculation Engine - wraps Python's math module for use by the calculator.
Provides safe evaluation of expressions limited to math functions.
"""

import math

# Public API: expose math functions and constants in a controlled namespace
FUNCTIONS = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}


def evaluate(expression):
    """
    Evaluate a mathematical expression using only allowed math operations.

    Args:
        expression (str): A mathematical expression string.

    Returns:
        str: The computed result as a string, or an error message.
    """
    allowed_names = {**FUNCTIONS, **CONSTANTS}
    try:
        # Use eval with restricted globals and locals
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Evaluation error: {e}"
