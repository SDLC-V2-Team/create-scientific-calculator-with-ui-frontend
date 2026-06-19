import unittest
from src.calculation_engine import evaluate


class TestCalculationEngine(unittest.TestCase):

    def test_basic_arithmetic(self):
        self.assertEqual(evaluate("2 + 3"), "5")
        self.assertEqual(evaluate("10 - 4"), "6")
        self.assertEqual(evaluate("3 * 7"), "21")
        self.assertEqual(evaluate("15 / 3"), "5.0")
        self.assertEqual(evaluate("2 ** 10"), "1024")

    def test_trigonometric(self):
        # sin(0) = 0
        self.assertEqual(evaluate("sin(0)"), "0.0")
        # cos(0) = 1
        self.assertEqual(evaluate("cos(0)"), "1.0")
        # tan(0) = 0
        self.assertEqual(evaluate("tan(0)"), "0.0")

    def test_logarithms(self):
        # log(e) = 1
        self.assertEqual(evaluate("log(e)"), "1.0")
        # log10(100) = 2
        self.assertEqual(evaluate("log10(100)"), "2.0")
        # log2(8) = 3
        self.assertEqual(evaluate("log2(8)"), "3.0")

    def test_exponential_and_sqrt(self):
        # exp(0) = 1
        self.assertEqual(evaluate("exp(0)"), "1.0")
        # sqrt(9) = 3
        self.assertEqual(evaluate("sqrt(9)"), "3.0")

    def test_constants(self):
        # pi
        self.assertAlmostEqual(float(evaluate("pi")), 3.141592653589793)
        # e
        self.assertAlmostEqual(float(evaluate("e")), 2.718281828459045)

    def test_invalid_expression(self):
        result = evaluate("xyz")
        self.assertTrue("Error" in result or "error" in result)

    def test_safety_no_builtins(self):
        # Attempt to use dangerous builtin
        result = evaluate("__import__('os').system('ls')")
        self.assertTrue("error" in result.lower())


if __name__ == '__main__':
    unittest.main()
