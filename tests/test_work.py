"""Module for testing the work package."""
import unittest
from src.toolbox.common import work


class TestWork(unittest.TestCase):
    """Test class for testing the work package."""

    def test_get_month_working_days(self):
        """Test get month working days."""
        for month_and_hours in self.get_days_and_hours_for_year_2022():
            expected = month_and_hours['days']
            actual = work.get_month_working_days(month_and_hours['month'], 2022)
            self.assertEqual(expected, actual, "Test for month: {0}".format(month_and_hours['month']))

    def test_get_month_working_hours(self):
        """Test get month working hours."""
        for month_and_hours in self.get_days_and_hours_for_year_2022():
            expected = month_and_hours['days'] * 8
            actual = work.get_month_working_hours(month_and_hours['month'], 2022)
            self.assertEqual(expected, actual, "Test for month: {0}".format(month_and_hours['month']))

    @staticmethod
    def get_days_and_hours_for_year_2022() -> list:
        return [{"month": 1, "days": 21}, {"month": 2, "days": 20}, {"month": 3, "days": 23}, {"month": 4, "days": 21},
                {"month": 5, "days": 22}, {"month": 6, "days": 22}, {"month": 7, "days": 21}, {"month": 8, "days": 23},
                {"month": 9, "days": 22}, {"month": 10, "days": 21}, {"month": 11, "days": 22},
                {"month": 12, "days": 22}]


if __name__ == '__main__':
    unittest.main()
