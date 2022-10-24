import click
import typer

from pdf.converter import convert_pdf_to_docx, convert_pdf_to_selectable
from common.output import show_message
from typing import Optional

app = typer.Typer()


@app.command()
@click.argument('input_file')
@click.argument('output_file')
def convert_pdf_to_selectable_pdf(input_file: str, output_file: Optional[str] = typer.Argument(None)):
    """Converts a scan PDF file to selectable PDF."""
    convert_pdf_to_selectable(input_file, output_file)
    show_message("File converted successfully[green].")


@app.command()
@click.argument('input_file')
@click.argument('output_file')
def convert_to_docx(input_file: str, output_file: Optional[str] = typer.Argument(None)):
    """Converts a PDF file to a DOCX file."""
    convert_pdf_to_docx(input_file, output_file)
    show_message("File converted successfully[green].")


typer_click_object = typer.main.get_command(app)


def main():
    typer_click_object()
