# Simple unittests for the insertion_sort method
import unittest

from Applications.ExpressionEvaluator import evaluate_expression


class ExpressionEvaluatorTest(unittest.TestCase):

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            evaluate_expression("")

    def test_singleton_expression(self):
        import random
        for i in range(10):
            num = random.randint(1, 50)
            self.assertEqual(evaluate_expression(str(num)), float(num),
                             "The method fails with random singleton expression.")

        for operand in ["*", "+", "/", "-"]:
            with self.assertRaises(ValueError):
                evaluate_expression(operand)

        with self.assertRaises(ValueError):
            evaluate_expression("operand")

    def test_expression(self):
        self.assertEqual(evaluate_expression("1 - 32*0.5 + 12"), -3.0, "The method doesn't evaluate properly")
        self.assertEqual(evaluate_expression("6/3 - 2*3 + 1 - 5/2 + 3/8 + 0.125 + 0.5"), -4.5,
                         "The method doesn't evaluate properly")
        self.assertEqual(evaluate_expression("2+3-4/2*2+3*2/0.5"), 16.0, "The method doesn't evaluate properly")

        with self.assertRaises(ArithmeticError):
            evaluate_expression("5*(6 - 3")
        with self.assertRaises(ArithmeticError):
            evaluate_expression("(3-(2+1+(6*7))")

        with self.assertRaises(ValueError):
            evaluate_expression("5^7 - 3*2")


if __name__ == '__main__':
    unittest.main()
