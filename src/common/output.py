from rich.console import Console

console = Console()


def show_message(message: str) -> None:
    console.print(message)
