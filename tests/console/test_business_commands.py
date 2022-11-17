import unittest
from typer.testing import CliRunner

from src.console.cli import app

runner = CliRunner()


class TestBusinessCommands(unittest.TestCase):

    def test_get_working_days_today(self):
        result = runner.invoke(
            app, ["business", "working-days", "--this-month"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(Current month working days|22)')

    def test_get_working_hours_today(self):
        result = runner.invoke(
            app, ["business", "working-hours", "--this-month"])
        self.assertEqual(0, result.exit_code)
        self.assertRegex(result.output, r'(Current month working hours|176)')


if __name__ == '__main__':
    unittest.main()
