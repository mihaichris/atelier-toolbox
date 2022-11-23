"""Module for testing the work package."""
import unittest
from src.toolbox.common import work


class TestWork(unittest.TestCase):
    """Test class for testing the work package."""

    def test_get_month_working_days(self):
        """Test get month working days."""
        self.assertEqual(22, work.get_month_working_days(11, 2022))

    def test_get_month_working_hours(self):
        """Test get month working hours."""
        self.assertEqual(176, work.get_month_working_hours(11, 2022))


if __name__ == '__main__':
    unittest.main()
