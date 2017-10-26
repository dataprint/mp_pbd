 # FUNCTIONAL TEST PROGRAM

    import unittest
    from calculator import Calculator


    # Test the calculator functionality
    class TestCalculator(unittest.TestCase):


    def setUp(self):
        self.calc = Calculator()


    # Test the addition functionality in the calculator program
    def test_add_function(self):
        result = self.calc.add(2, 2)


    self.assertEqual(4, result)
    result = self.calc.add(2, 4)
    self.assertEqual(6, result)
    result = self.calc.add(2, -2)
    self.assertEqual(0, result)


    # Test the subtraction functionality in the calculator program
    def test_subtract_function(self):
        result = self.calc.subtract(3, 2)


    self.assertEqual(1, result)
    result = self.calc.subtract(2, 4)
    self.assertEqual(-2, result)
    result = self.calc.subtract(50, 20)
    self.assertEqual(30, result)


    # Test the multiplication functionality in the calculator program
    def test_multiply_function(self):
        result = self.calc.multiply(2, 3)


    self.assertEqual(6, result)
    result = self.calc.multiply(4, 4)
    self.assertEqual(16, result)
    result = self.calc.multiply(5, -2)
    self.assertEqual(-10, result)


    # Test the division functionality in the calculator program
    def test_divide_function(self):
        result = self.calc.divide(10, 2)


    self.assertEqual(5, result)
    result = self.calc.divide(50, 4)
    self.assertEqual(12.5, result)
    result = self.calc.divide(100, 2)
    self.assertEqual(50, result)


    # Test the exponential functionality in the calculator program
    def test_exponent_function(self):
        result = self.calc.exponent(2, 3)


    self.assertEqual(8, result)
    result = self.calc.exponent(4, 3)
    self.assertEqual(64, result)
    result = self.calc.exponent(5, 4)
    self.assertEqual(625, result)


    # Test the square root functionality in the calculator program
    def test_squareRoot_function(self):
        result = self.calc.squareRoot(81)


    self.assertEqual(9, result)
    result = self.calc.squareRoot(9)
    self.assertEqual(3, result)
    result = self.calc.squareRoot(6)
    self.assertEqual(2.449, result)


    # Test the squared functionality in the calculator program
    def test_squared_function(self):
        result = self.calc.squared(3)


    self.assertEqual(9, result)
    result = self.calc.squared(44)
    self.assertEqual(1936, result)
    result = self.calc.squared(-6)
    self.assertEqual(36, result)


    # Test the cubed functionality in the calculator program
    def test_cubed_function(self):
        result = self.calc.cubed(3)


    self.assertEqual(27, result)
    result = self.calc.cubed(44)
    self.assertEqual(85184, result)
    result = self.calc.cubed(-6)
    self.assertEqual(-216, result)


    # Test the sine functionality in the calculator program
    def test_sin_function(self):
        result = self.calc.sin(1)


    self.assertEqual(0.841, result)
    result = self.calc.sin(3)
    self.assertEqual(0.141, result)
    result = self.calc.sin(99)
    self.assertEqual(-0.999, result)


    # Test the cosine functionality in the calculator program
    def test_cos_function(self):
        result = self.calc.cos(1)


    self.assertEqual(0.540, result)
    result = self.calc.cos(3)
    self.assertEqual(-0.99, result)
    result = self.calc.cos(99)
    self.assertEqual(0.04, result)


    # Test that an error is returned if a non-numeric character is entered
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, ‘two’, ‘three’)
        self.assertRaises(ValueError, self.calc.subtract, ‘two’, ‘three’)
        self.assertRaises(ValueError, self.calc.multiply, ‘two’, 0)
        self.assertRaises(ValueError, self.calc.divide, 2, ‘three’)
        self.assertRaises(ValueError, self.calc.exponent, 7, ‘five’)
        self.assertRaises(ValueError, self.calc.squareRoot, ‘three’)
        self.assertRaises(ValueError, self.calc.squared, ‘three’)
        self.assertRaises(ValueError, self.calc.cubed, ‘two’)
        self.assertRaises(ValueError, self.calc.sin, ‘three’)
        self.assertRaises(ValueError, self.calc.cos, ‘five’)

        if __name__ == ‘__main__’:
            unittest.main()
