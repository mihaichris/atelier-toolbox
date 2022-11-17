import unittest
from src.common.calendar import get_first_date_of_month, get_last_date_of_month
from datetime import datetime


class TestCalendar(unittest.TestCase):

    def test_get_first_date_of_current_month(self):
        now = datetime.now()
        first_date = datetime(now.year, now.month, 1)
        current_month_first_date = get_first_date_of_month(
            now.year, now.month)
        self.assertEqual(first_date.strftime(
            "%Y-%m-%d"), current_month_first_date)

    def test_get_first_date_of_past_month(self):
        now = datetime.now()
        last_date = datetime(now.year, now.month - 1, 1)
        last_month_first_date = get_first_date_of_month(
            now.year, now.month-1)
        self.assertEqual(last_date.strftime("%Y-%m-%d"), last_month_first_date)

    def test_get_first_date_of_future_month(self):
        now = datetime.now()
        future_date = datetime(now.year, now.month + 1, 1)
        future_month_first_date = get_first_date_of_month(
            now.year, now.month+1)
        self.assertEqual(future_date.strftime(
            "%Y-%m-%d"), future_month_first_date)

    def test_get_last_date_January(self):
        last_date = datetime(2022, 1, 31)
        january_last_date = get_last_date_of_month(
            2022,  1)
        self.assertEqual(last_date.strftime(
            "%Y-%m-%d"), january_last_date)

    def test_get_last_date_of_december(self):
        last_date = datetime(2022, 12, 31)
        last_month_december = get_last_date_of_month(
            2022, 12)
        self.assertEqual(last_date.strftime("%Y-%m-%d"), last_month_december)


if __name__ == '__main__':
    unittest.main()
