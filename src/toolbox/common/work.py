"""Module for work."""
import datetime


def get_month_working_days(month: int, year: int) -> int:
    """Get the number of working days for a given month.

    Args:
        month (int): Month of the year.
        year (int): Year of the month.
    """
    holidays = {}
    business_days = 0
    for i in range(1, 32):
        try:
            date = datetime.date(year, month, i)
        except ValueError:
            break
        if date.weekday() < 5 and date not in holidays:  # Monday == 0, Sunday == 6
            business_days += 1
    return business_days


def get_month_working_hours(month: int, year: int) -> int:
    """Get the number of working hours for a given month.

    Args:
        month (int): Month of the year.
        year (int): Year of the month.
    """
    return get_month_working_days(month, year) * 8
