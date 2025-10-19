import unittest
from functions import get_files_info

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

if __name__ == "__main__":
    unittest.main()