"""Business set commands."""
import datetime
import typer
from toolbox.common.work import get_month_working_hours, get_month_working_days
from toolbox.common.output import show_message
from toolbox.sets.business import __version__ as business_package_version

app = typer.Typer(short_help="Business CLI Tool")


def version_callback(value: bool):
    """Version callback."""
    if value:
        show_message(f"Business CLI Version: {business_package_version.__version__}")
        raise typer.Exit()


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


@app.callback()
def version(ver: bool = typer.Option(None, "--version",
                                     callback=version_callback, help="Get command version.",
                                     is_eager=True)):
    """Version Output."""
    return ver
