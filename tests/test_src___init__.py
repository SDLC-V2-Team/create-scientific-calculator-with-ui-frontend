import importlib
import sys


def test_src_package_importable():
    """Happy path: src package can be imported without errors."""
    import src
    assert src is not None


def test_src_is_package():
    """Happy path: src is recognized as a Python package."""
    import src
    assert hasattr(src, '__path__'), "src should be a package with __path__"


def test_src_package_name():
    """Edge case: verify the package name is correct."""
    import src
    assert src.__name__ == 'src'