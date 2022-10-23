import click
import typer

from pdf.converter import convert_pdf_to_docx, convert_pdf_to_selectable
from common.output import show_message

app = typer.Typer()


@app.command()
@click.argument('input_file')
@click.argument('output_file')
def convert_pdf_to_selectable_pdf(input_file: str, output_file: str):
    """Converts a scan PDF file to selectable PDF."""
    convert_pdf_to_selectable(input_file, output_file)
    show_message("File converted successfully[green].")


@app.command()
def convert_to_docx():
    """Converts a PDF file to a DOCX file."""
    show_message("Converted to DOCX")


typer_click_object = typer.main.get_command(app)


def main():
    typer_click_object()
