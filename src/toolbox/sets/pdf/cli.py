"""PDF set commads."""
from typing import Optional
import typer
from toolbox.sets.pdf.converter import convert_pdf_to_docx, convert_pdf_to_selectable
from toolbox.common.output import show_message, abort
from toolbox.common.exceptions import ConvertPDFException
from toolbox.sets.pdf import __version__ as pdf_package_version

app = typer.Typer(short_help="PDF CLI Tool")


def version_callback(value: bool):
    """Version callback."""
    if value:
        show_message(f"PDF CLI Version: {pdf_package_version.__version__}")
        raise typer.Exit()


@app.command()
def convert_to_selectable_pdf(input_file: str, output_file: Optional[str] = typer.Argument(None)):
    """Converts a scan PDF file to selectable PDF."""
    try:
        convert_pdf_to_selectable(input_file, output_file)
    except ConvertPDFException as err:
        abort(f'Error converting to selectable pdf: {err}')
    show_message("File converted successfully[green].")


@app.command()
def convert_to_docx(input_file: str, output_file: Optional[str] = typer.Argument(None)):
    """Converts a PDF file to a DOCX file."""
    try:
        convert_pdf_to_docx(input_file, output_file)
    except ConvertPDFException as err:
        abort(f'Error converting to docx: {err}')
    show_message("File converted successfully[green].")


@app.callback()
def version(ver: bool = typer.Option(None, "--version",
                                     callback=version_callback,
                                     help="Get command version.",
                                     is_eager=True)):
    """Version Output."""
    return ver
