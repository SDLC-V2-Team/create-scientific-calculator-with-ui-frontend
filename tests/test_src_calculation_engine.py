import math
import pytest
from src.calculation_engine import FUNCTIONS, CONSTANTS, evaluate


def test_functions_contains_math_symbols():
    """FUNCTIONS should expose known math module members."""
    assert "sqrt" in FUNCTIONS
    assert "sin" in FUNCTIONS
    assert "cos" in FUNCTIONS
    assert "log" in FUNCTIONS
    assert callable(FUNCTIONS["sqrt"])


def test_constants_contain_pi_and_e():
    """CONSTANTS should expose pi and e with correct values."""
    assert "pi" in CONSTANTS
    assert "e" in CONSTANTS
    assert CONSTANTS["pi"] == pytest.approx(math.pi)
    assert CONSTANTS["e"] == pytest.approx(math.e)


def test_evaluate_basic_arithmetic():
    """Happy path: basic arithmetic expressions return correct string results."""
    assert evaluate("2 + 3") == "5"
    assert evaluate("10 - 4") == "6"
    assert evaluate("3 * 4") == "12"
    assert evaluate("15 / 3") == "5.0"


def test_evaluate_math_functions():
    """Happy path: math functions like sqrt and sin are evaluated correctly."""
    result = evaluate("sqrt(16)")
    assert result == str(math.sqrt(16))

    result = evaluate("sin(0)")
    assert result == str(math.sin(0))

    result = evaluate("log(1)")
    assert result == str(math.log(1))


def test_evaluate_constants():
    """Happy path: pi and e constants are accessible in evaluate."""
    result = evaluate("pi")
    assert result == str(math.pi)

    result = evaluate("e")
    assert result == str(math.e)

    result = evaluate("pi * 2")
    assert result == str(math.pi * 2)


def test_evaluate_invalid_expression_returns_error_message():
    """Error path: invalid expression returns an error message string."""
    result = evaluate("import os")
    assert result.startswith("Evaluation error:")

    result = evaluate("undefined_function()")
    assert result.startswith("Evaluation error:")

    result = evaluate("1 +* 2")
    assert result.startswith("Evaluation error:")


def test_evaluate_division_by_zero_returns_error_message():
    """Edge case: division by zero should return an error message."""
    result = evaluate("1 / 0")
    assert result.startswith("Evaluation error:")


def test_evaluate_empty_expression_returns_error_message():
    """Edge case: empty expression string should return an error message."""
    result = evaluate("")
    assert result.startswith("Evaluation error:")