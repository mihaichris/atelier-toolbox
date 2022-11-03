from rich.console import Console
import typer

console = Console()

ERROR_STYLE = "bold red"
INFO_STYLE = "bold blue"
SUCCESS_STYLE = "bold green"


def success_message(message: str) -> None:
    show_message(message=message, style=SUCCESS_STYLE)


def error_message(message: str) -> None:
    show_message(message=message, style=ERROR_STYLE)


def show_message(message: str, style: str = None) -> None:
    if style is None:
        style = INFO_STYLE
    console.print(message, style=style)


def abort(message: str):
    error_message(message=message)
    raise typer.Abort()
