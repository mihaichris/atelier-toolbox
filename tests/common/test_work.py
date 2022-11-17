import unittest
import os
import src.common.work as work


class TestWork(unittest.TestCase):

    def test_get_month_working_days(self):
        self.assertEqual(22, work.get_month_working_days(11, 2022))

    def test_get_month_working_days(self):
        self.assertEqual(176, work.get_month_working_hours(11, 2022))


if __name__ == '__main__':
    unittest.main()
