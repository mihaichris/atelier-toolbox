"""PDF set commads."""
from typing import Optional
import typer
from toolbox.sets.pdf.converter import convert_pdf_to_docx, convert_pdf_to_selectable
from toolbox.common.output import show_message, abort
from toolbox.common.exceptions import ConvertPDFException

app = typer.Typer(short_help="PDF CLI Tool")
