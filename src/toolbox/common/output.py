"""Module for output to console"""
from rich.console import Console
from rich.table import Table
import typer

console = Console()

ERROR_STYLE = "bold red"
INFO_STYLE = "bold blue"
SUCCESS_STYLE = "bold green"


def success_message(message: str) -> None:
    """Prints a success message"""
    show_message(message=message, style=SUCCESS_STYLE)


def error_message(message: str) -> None:
    """Prints an error message"""
    show_message(message=message, style=ERROR_STYLE)


def show_table(table: Table) -> None:
    """Prints a table"""
    console.print(table)


def show_message(message: str, style: str = None) -> None:
    """Prints a message"""
    if style is None:
        style = INFO_STYLE
    console.print(f"{message}", style=style)


def abort(message: str):
    """Prints an error message"""
    error_message(message=message)
    raise typer.Abort()
