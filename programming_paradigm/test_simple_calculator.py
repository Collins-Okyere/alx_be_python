import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -10), 5)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0))

    def test_edge_cases(self):
        """Test edge cases for all methods."""
        # Very large numbers
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
        self.assertEqual(self.calc.subtract(1e10, 1e10), 0)
        self.assertEqual(self.calc.multiply(1e10, 2), 2e10)
        self.assertEqual(self.calc.divide(1e10, 2), 5e9)

        # Small (decimal) numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=1)
        self.assertEqual(self.calc.subtract(0.5, 0.2), 0.3)
        self.assertEqual(self.calc.multiply(0.1, 0.2), 0.02)
        self.assertEqual(self.calc.divide(0.1, 0.2), 0.5)

if __name__ == "__main__":
    unittest.main()
