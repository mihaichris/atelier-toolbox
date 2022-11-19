"""Module for testing PDF commands."""
import unittest
import os
from typer.testing import CliRunner
from src.console.cli import app

runner = CliRunner()


class TestPDFCommands(unittest.TestCase):
    """Testing class for PDF commands"""

    def test_convert_selectable_pdf_to_selectable_pdf_without_output_will_abort(self):
        """Test if convert a selectable pdf to selectable pdf will output error."""
        result = runner.invoke(
            app, ["pdf", "convert-to-selectable-pdf", "tests/resources/selectable_test.pdf"])
        self.assertEqual(1, result.exit_code)
        self.assertRegex(result.output, r'(Aborted)')
        self.assertFalse(os.path.isfile(
            'tests/resources/scanned_test_selectable.pdf'))

    def test_convert_pdf_to_selectable_pdf_without_output(self):
        """Test converting a scanned pdf to selectable pdf with no specified output file."""
        result = self.invoke_convert_to_selectable_pdf(
            ["tests/resources/scanned_test.pdf"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(File converted successfully)')
        self.assertTrue(os.path.isfile(
            'tests/resources/scanned_test_selectable.pdf'))
        os.remove('tests/resources/scanned_test_selectable.pdf')

    def test_convert_pdf_to_selectable_pdf_with_output(self):
        """Test converting a scanned pdf to selectable pdf with specified output file."""
        result = self.invoke_convert_to_selectable_pdf(
            ["tests/resources/scanned_test.pdf", "tests/resources/scanned_test_output.pdf"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(File converted successfully)')
        self.assertTrue(os.path.isfile(
            'tests/resources/scanned_test_output.pdf'))
        os.remove('tests/resources/scanned_test_output.pdf')

    def test_convert_pdf_to_docx_without_output(self):
        """Test converting a scanned pdf to docx with no specified output file."""
        result = self.invoke_convert_to_docx_pdf(
            ["tests/resources/scanned_test.pdf"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(File converted successfully)')
        self.assertTrue(os.path.isfile('tests/resources/scanned_test.docx'))
        os.remove('tests/resources/scanned_test.docx')

    def test_convert_pdf_to_docx_with_output(self):
        """Test converting a scanned pdf to docx with specified output file."""
        result = self.invoke_convert_to_docx_pdf(
            ["tests/resources/scanned_test.pdf", "tests/resources/scanned_test_output.docx"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(File converted successfully)')
        self.assertTrue(os.path.isfile(
            'tests/resources/scanned_test_output.docx'))
        os.remove('tests/resources/scanned_test_output.docx')

    def invoke_convert_to_selectable_pdf(self, args):
        """Invoke the convert-to-selectable-pdf command with args."""
        commands = ["pdf", "convert-to-selectable-pdf"]
        commands.extend(args)
        return runner.invoke(app, commands)

    def invoke_convert_to_docx_pdf(self, args):
        """Invoke the convert-to-docx command with args."""
        commands = ["pdf", "convert-to-docx"]
        commands.extend(args)
        return runner.invoke(app, commands)


if __name__ == '__main__':
    unittest.main()
