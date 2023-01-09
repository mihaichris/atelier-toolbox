"""Module for testing the calendar package."""
import unittest
import datetime
from src.toolbox.common.calendar import get_first_date_of_month, get_last_date_of_month


class TestCalendar(unittest.TestCase):
    """Testing class for calendar."""

    def test_get_first_date_of_current_month(self):
        """Test get first date of current month."""
        now = datetime.datetime.now()
        first_date = datetime.datetime(now.year, now.month, 1)
        current_month_first_date = get_first_date_of_month(
            now.year, now.month)
        self.assertEqual(first_date.strftime(
            "%Y-%m-%d"), current_month_first_date)

    def test_get_first_date_of_past_month(self):
        """Test get first date of past month."""
        now = datetime.datetime.now()
        now_month = now.month - 1
        past_month = now.month-1
        if past_month == 0:
            past_month = 1
        if now_month == 0:
            now_month = 1
        last_date = datetime.datetime(now.year, now_month, 1)
        last_month_first_date = get_first_date_of_month(
            now.year, past_month)
        self.assertEqual(last_date.strftime("%Y-%m-%d"), last_month_first_date)

    def test_get_first_date_of_future_month(self):
        """Test get first date of future month."""
        now = datetime.datetime.now()
        future_month = now.month + 1
        if future_month == 13:
            future_month = 12
        future_date = datetime.datetime(now.year, future_month, 1)
        future_month_first_date = get_first_date_of_month(
            now.year, future_month)
        self.assertEqual(future_date.strftime(
            "%Y-%m-%d"), future_month_first_date)

    def test_get_last_date_january(self):
        """Test get last date of January."""
        last_date = datetime.datetime(2022, 1, 31)
        january_last_date = get_last_date_of_month(
            2022,  1)
        self.assertEqual(last_date.strftime(
            "%Y-%m-%d"), january_last_date)

    def test_get_last_date_of_december(self):
        """Test get last date of december."""
        last_date = datetime.datetime(2022, 12, 31)
        last_month_december = get_last_date_of_month(
            2022, 12)
        self.assertEqual(last_date.strftime("%Y-%m-%d"), last_month_december)


if __name__ == '__main__':
    unittest.main()
