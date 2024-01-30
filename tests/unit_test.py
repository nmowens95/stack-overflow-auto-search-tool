import unittest
from search_tool.error_checker import execute_python_code

class TestPythonErrorChecker(unittest.TestCase):
    def test_no_errors(self):
        code = "print('Hello, world!')"
        result = execute_python_code(code)
        self.assertTrue(result["success"])

    def test_runtime_errors(self):
        code = "print(variable_that_does_not_exist)"
        result = execute_python_code(code)
        self.assertFalse(result["success"])
        self.assertEqual(result["error_type"], "RuntimeError")

    def test_exception(self):
        code = "1 / 0"
        result = execute_python_code(code)
        self.assertFalse(result["success"])
        self.assertEqual(result["error_type"], "Exception")

    def test_code_from_file(self):
        file_name = "practice_error.py"

        with open(file_name, "r") as file:
            code = file.read()

        result = execute_python_code(code)
        self.assertTrue(result["success"])

    if __name__ == "__main__":
        unittest.main()