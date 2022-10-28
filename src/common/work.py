import numpy as np
from common.calendar import get_first_date_of_current_month, get_last_date_of_month


def get_month_working_days(month: int, year: int) -> int:
    start_date = get_first_date_of_current_month(year, month)
    end_date = get_last_date_of_month(year, month)
    return np.busday_count(start_date, end_date) + 1


def get_month_working_hours(month: int, year: int) -> int:
    return get_month_working_days() * 8 + 8
