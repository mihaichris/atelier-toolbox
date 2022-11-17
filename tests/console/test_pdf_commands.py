import unittest
from typer.testing import CliRunner
import os

from src.console.cli import app

runner = CliRunner()


class TestPDFCommands(unittest.TestCase):

    def test_convert_selectable_pdf_to_selectable_pdf_without_output_will_abort(self):
        result = runner.invoke(
            app, ["pdf", "convert-to-selectable-pdf", "tests/resources/selectable_test.pdf"])
        self.assertEqual(1, result.exit_code)
        self.assertRegex(result.output, r'(Aborted)')
        self.assertFalse(os.path.isfile(
            'tests/resources/scanned_test_selectable.pdf'))

    def test_convert_pdf_to_selectable_pdf_without_output(self):
        result = runner.invoke(
            app, ["pdf", "convert-to-selectable-pdf", "tests/resources/scanned_test.pdf"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(File converted successfully)')
        self.assertTrue(os.path.isfile(
            'tests/resources/scanned_test_selectable.pdf'))
        os.remove('tests/resources/scanned_test_selectable.pdf')

    def test_convert_pdf_to_selectable_pdf_with_output(self):
        result = runner.invoke(
            app, ["pdf", "convert-to-selectable-pdf", "tests/resources/scanned_test.pdf", "tests/resources/scanned_test_output.pdf"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(File converted successfully)')
        self.assertTrue(os.path.isfile(
            'tests/resources/scanned_test_output.pdf'))
        os.remove('tests/resources/scanned_test_output.pdf')

    def test_convert_pdf_to_docx_without_output(self):
        result = runner.invoke(
            app, ["pdf", "convert-to-docx", "tests/resources/scanned_test.pdf"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(File converted successfully)')
        self.assertTrue(os.path.isfile(
            'tests/resources/scanned_test.docx'))
        os.remove('tests/resources/scanned_test.docx')

    def test_convert_pdf_to_docx_with_output(self):
        result = runner.invoke(
            app, ["pdf", "convert-to-docx", "tests/resources/scanned_test.pdf", "tests/resources/scanned_test_output.docx"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(File converted successfully)')
        self.assertTrue(os.path.isfile(
            'tests/resources/scanned_test_output.docx'))
        os.remove('tests/resources/scanned_test_output.docx')


if __name__ == '__main__':
    unittest.main()
