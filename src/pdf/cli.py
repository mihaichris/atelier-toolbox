import typer

from .converter import convert_pdf_to_docx, convert_pdf_to_selectable
from common.output import show_message

app = typer.Typer(help="Awesome CLI for working with PDF files.")


@app.command("convert_to_selectable", help="Converts a scan PDF file to selectable PDF.")
def hello_world():
    show_message("Converted to selectable")


@app.command("convert_to_docx", help="Converts a PDF file to a DOCX file.")
def hello_world():
    show_message("Converted to DOCX")


def main():
    app()
