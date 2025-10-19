import unittest
from functions import get_file_content, get_files_info

class TestGetFiles(unittest.TestCase):
    maxDiff = None

    def test_self(self):
        result = get_files_info.get_files_info("calculator", ".")
        print(result)
        expected = """Result for current directory:
  - tests.py: file_size=1342 bytes, is_dir=False
  - pkg: file_size=4096 bytes, is_dir=True
  - main.py: file_size=575 bytes, is_dir=False"""
        self.assertEqual(result, expected)

    def test_pkg(self):
        result = get_files_info.get_files_info("calculator", "pkg")
        print(result)
        expected = """Result for 'pkg' directory:
  - render.py: file_size=766 bytes, is_dir=False
  - __pycache__: file_size=4096 bytes, is_dir=True
  - calculator.py: file_size=1737 bytes, is_dir=False"""
        self.assertEqual(result, expected)

    def test_bin(self):
        result = get_files_info.get_files_info("calculator", "/bin")
        print(result)
        expected = """Result for '/bin' directory:
    Error: Cannot list "/bin" as it is outside the permitted working directory"""
        self.assertEqual(result, expected)

    def test_parent(self):
        result = get_files_info.get_files_info("calculator", "../")
        print(result)
        expected = """Result for '../' directory:
    Error: Cannot list "../" as it is outside the permitted working directory"""
        self.assertEqual(result, expected)
    
    def test_read_main(self):
        result = get_file_content.get_file_content("calculator", "main.py")
        print(result)
        expected = """# main.py

import sys
from pkg.calculator import Calculator
from pkg.render import render


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()"""
        self.assertEqual(result, expected)

    def test_read_calc(self):
        result = get_file_content.get_file_content("calculator", "pkg/calculator.py")
        print(result)
        expected = """# calculator.py

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))"""
        self.assertEqual(result, expected)
    def test_read_outside(self):
        result = get_file_content.get_file_content("calculator", "/bin/cat")
        print(result)
        expected = """Error: Cannot read "/bin/cat" as it is outside the permitted working directory"""
        self.assertEqual(result, expected)
    def test_read_dne(self):
        result = get_file_content.get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)
        expected = """Error: File not found or is not a regular file: "pkg/does_not_exist.py\""""
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()