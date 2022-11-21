"""PDF set commads."""
from typing import Optional
import typer
from console.sets.pdf.converter import convert_pdf_to_docx, convert_pdf_to_selectable
from common.output import show_message, abort
from common.exceptions import ConvertPDFException

app = typer.Typer(name="PDF CLI Tool")


@app.command()
def convert_to_selectable_pdf(input_file: str, output_file: Optional[str] = typer.Argument(None)):
    """Converts a scan PDF file to selectable PDF."""
    try:
        convert_pdf_to_selectable(input_file, output_file)
    except ConvertPDFException as err:
        print(err)
        abort(f'Error converting to selectable pdf: {err}')
    show_message("File converted successfully[green].")


@ app.command()
def convert_to_docx(input_file: str, output_file: Optional[str] = typer.Argument(None)):
    """Converts a PDF file to a DOCX file."""
    try:
        convert_pdf_to_docx(input_file, output_file)
    except ConvertPDFException as err:
        abort(f'Error converting to docx: {err}')
    show_message("File converted successfully[green].")
