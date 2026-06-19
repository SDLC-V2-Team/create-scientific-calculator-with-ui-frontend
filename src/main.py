#!/usr/bin/env python3
"""CLI entry point for the scientific calculator."""

import sys
import math

# Securely evaluate expressions using only math functions and constants
SAFE_DICT = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}
# Add basic arithmetic operators via eval's built-in scope or allow them naturally
# We'll use eval with math as the global namespace and an empty local dict.


def evaluate(expression: str) -> str:
    """Evaluate a mathematical expression and return a string result."""
    try:
        result = eval(expression, {"__builtins__": {}}, SAFE_DICT)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def main():
    print("Scientific Calculator CLI (type 'exit' to quit)")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in ("exit", "quit"):
                break
            if not user_input:
                continue
            output = evaluate(user_input)
            print(output)
        except (EOFError, KeyboardInterrupt):
            print()
            break


if __name__ == "__main__":
    main()
