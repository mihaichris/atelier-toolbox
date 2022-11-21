"""Module for testing the file package."""
import unittest
import os
from src.common import file


class TestFile(unittest.TestCase):
    """Test class for file package."""

    def test_get_filename(self):
        """Test get filename."""
        current_filename = 'test_file.py'
        self.assertEqual('test_file', file.get_filename(current_filename))

    def test_load_toml_file(self):
        """Test load toml file."""
        self.init_test_file()
        self.assertEqual({'test': {'value': 1}},
                         file.load_toml('test_toml_file.toml'))
        self.remove_test_file()

    def init_test_file(self):
        """Init test file."""
        try:
            with open("test_toml_file.toml", 'w',  encoding="utf-8") as toml_file:
                toml_file.write("[test]\nvalue=1")
                toml_file.close()
        except OSError:
            toml_file = None

    def remove_test_file(self):
        """Remove test file."""
        os.remove('test_toml_file.toml')


if __name__ == '__main__':
    unittest.main()
