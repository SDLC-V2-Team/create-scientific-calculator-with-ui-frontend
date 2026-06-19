import pytest
from src.main import evaluate, main
from unittest.mock import patch, call
import io


def test_evaluate_basic_arithmetic():
    """Happy path: basic arithmetic expressions are evaluated correctly."""
    assert evaluate("2 + 3") == "5"
    assert evaluate("10 - 4") == "6"
    assert evaluate("3 * 7") == "21"
    assert evaluate("20 / 4") == "5.0"


def test_evaluate_math_functions():
    """Happy path: math functions from the math module work correctly."""
    result = evaluate("sqrt(16)")
    assert result == "4.0"

    result = evaluate("floor(3.7)")
    assert result == "3"

    result = evaluate("pow(2, 10)")
    assert result == "1024.0"


def test_evaluate_math_constants():
    """Happy path: math constants like pi and e are available."""
    import math
    result = evaluate("pi")
    assert result == str(math.pi)

    result = evaluate("e")
    assert result == str(math.e)


def test_evaluate_empty_expression():
    """Edge case: empty string expression returns an Error string."""
    result = evaluate("")
    assert result.startswith("Error:")


def test_evaluate_division_by_zero():
    """Edge case: division by zero returns an Error string."""
    result = evaluate("1 / 0")
    assert result.startswith("Error:")


def test_evaluate_invalid_expression():
    """Error path: invalid/malicious expressions return an Error string."""
    result = evaluate("this is not valid math")
    assert result.startswith("Error:")

    # Attempt to access builtins should be blocked
    result = evaluate("__import__('os').listdir('.')")
    assert result.startswith("Error:")


def test_main_exit(capsys):
    """Happy path: main loop exits on 'exit' command."""
    with patch("builtins.input", side_effect=["2 + 2", "exit"]):
        main()
    captured = capsys.readouterr()
    assert "4" in captured.out
    assert "Scientific Calculator CLI" in captured.out


def test_main_eof_exits_gracefully(capsys):
    """Edge case: main loop handles EOFError gracefully."""
    with patch("builtins.input", side_effect=EOFError):
        main()
    captured = capsys.readouterr()
    assert "Scientific Calculator CLI" in captured.out