import unittest
import os
import src.common.file as file


class TestFile(unittest.TestCase):

    def test_get_filename(self):
        current_filename = 'test_file.py'
        self.assertEqual('test_file', file.get_filename(current_filename))

    def test_load_toml_file(self):
        self.init_test_file()
        self.assertEqual({'test': {'value': 1}},
                         file.load_toml('test_toml_file.toml'))
        self.remove_test_file()

    def init_test_file(self):
        toml_file = open("test_toml_file.toml", 'w')
        toml_file.write("[test]\nvalue=1")
        toml_file.close()

    def remove_test_file(self):
        os.remove('test_toml_file.toml')


if __name__ == '__main__':
    unittest.main()
