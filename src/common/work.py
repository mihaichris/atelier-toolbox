"""Module for work."""
import numpy as np
from common.calendar import get_first_date_of_month, get_last_date_of_month


def get_month_working_days(month: int, year: int) -> int:
    """Get the number of working days for a given month.

    Args:
        month (int): Month of the year.
        year (int): Year of the month.
    """
    start_date = get_first_date_of_month(year, month)
    end_date = get_last_date_of_month(year, month)
    return np.busday_count(start_date, end_date) + 1


def get_month_working_hours(month: int, year: int) -> int:
    """Get the number of working hours for a given month.

    Args:
        month (int): Month of the year.
        year (int): Year of the month.
    """
    return get_month_working_days(month, year) * 8
