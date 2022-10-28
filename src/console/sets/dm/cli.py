import click
import typer

from common.output import show_message

app = typer.Typer(name="DM (Direct Message) Framework CLI Tool")


@app.command()
def templates():
    """Lists all available templates."""
    pass
