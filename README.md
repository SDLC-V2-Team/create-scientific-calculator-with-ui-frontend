# Scientific Calculator (CLI)

A simple command-line scientific calculator built with Python.

## Features
- Basic arithmetic: `+`, `-`, `*`, `/`, `**` (power), `%`
- Trigonometric functions: `sin`, `cos`, `tan` (radians)
- Inverse trigonometric: `asin`, `acos`, `atan`
- Logarithmic: `log` (base e), `log10`, `log2`
- Exponential: `exp`, `sqrt`
- Constants: `pi`, `e`
- Full expression evaluation using Python's `math` module.

## Usage

From the project root:

```bash
python src/main.py
```

Type expressions at the prompt. Exit with `exit` or `quit`.

Example:
```
> sin(30) + 1
1.5
> log(100)
4.605170185988092
> pi
3.141592653589793
```

## Running Tests

```bash
python -m unittest discover tests
```

## License
MIT