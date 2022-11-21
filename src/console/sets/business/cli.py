"""Business set commands."""
import datetime
import typer
from common.work import get_month_working_hours, get_month_working_days
from common.output import show_message

app = typer.Typer(name="Business CLI Tool")


@app.command()
def working_hours(
        is_month: bool = typer.Option(False, '--this-month',
                                      help="Get current month working hours.", is_flag=True)):
    """Get working hours based of a date period."""
    year = datetime.datetime.now().year
    if is_month:
        month = datetime.datetime.now().month
        month_working_hours = get_month_working_hours(month, year)
        show_message(f"Current month working hours: {month_working_hours}")


@app.command()
def working_days(
    is_month: bool = typer.Option(False, '--this-month',
                                  help="Get current month working days.", is_flag=True)):
    """Get working days based of a date period."""
    year = datetime.datetime.now().year
    if is_month:
        month = datetime.datetime.now().month
        month_working_days = get_month_working_days(month, year)
        show_message(f"Current month working days: {month_working_days}")
