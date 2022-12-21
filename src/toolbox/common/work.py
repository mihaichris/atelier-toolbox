"""Module for work."""
import datetime


def get_month_working_days(month: int, year: int) -> int:
    """Get the number of working days for a given month.

    Args:
        month (int): Month of the year.
        year (int): Year of the month.
    """
    holidays = {}
    businessdays = 0
    for i in range(1, 32):
        try:
            thisdate = datetime.date(year, month, i)
        except ValueError:
            break
        if thisdate.weekday() < 5 and thisdate not in holidays:  # Monday == 0, Sunday == 6
            businessdays += 1
    return businessdays


def get_month_working_hours(month: int, year: int) -> int:
    """Get the number of working hours for a given month.

    Args:
        month (int): Month of the year.
        year (int): Year of the month.
    """
    return get_month_working_days(month, year) * 8
