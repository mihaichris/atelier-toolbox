"""Module for testing Business commands."""
import unittest
from typer.testing import CliRunner
from toolbox.cli import app
from toolbox.common.work import get_month_working_days, get_month_working_hours

runner = CliRunner()


class TestBusinessCommands(unittest.TestCase):
    """Testing class for Business commands"""

    def test_get_working_days_current_month(self):
        """Test get working days current month."""
        result = runner.invoke(
            app, ["business", "working-days", "--this-month"])
        days = get_month_working_days(11, 2022)
        self.assertEqual(0, result.exit_code)
        self.assertRegex(
            result.output, rf'(Current month working days|{days})')

    def test_get_working_hours_this_month(self):
        """Test get working hours current month."""
        result = runner.invoke(
            app, ["business", "working-hours", "--this-month"])
        hours = get_month_working_hours(11, 2022)
        self.assertEqual(0, result.exit_code)
        self.assertRegex(
            result.output, rf'(Current month working hours|{hours})')


if __name__ == '__main__':
    unittest.main()
