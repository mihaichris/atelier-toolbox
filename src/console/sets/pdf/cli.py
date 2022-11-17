import click
import typer

from console.sets.pdf.converter import convert_pdf_to_docx, convert_pdf_to_selectable
from common.output import show_message, abort
from typing import Optional

app = typer.Typer(name="PDF CLI Tool")


@app.command()
def convert_to_selectable_pdf(input_file: str, output_file: Optional[str] = typer.Argument(None)):
    """Converts a scan PDF file to selectable PDF."""
    try:
        convert_pdf_to_selectable(input_file, output_file)
    except Exception as err:
        abort('Error converting to selectable pdf: {0}'.format(err))
    show_message("File converted successfully[green].")


@app.command()
def convert_to_docx(input_file: str, output_file: Optional[str] = typer.Argument(None)):
    """Converts a PDF file to a DOCX file."""
    try:
        convert_pdf_to_docx(input_file, output_file)
    except Exception as err:
        abort('Error converting to docx: {0}'.format(err))
    show_message("File converted successfully[green].")
