"""Module for converting files."""
import os
import ocrmypdf
from pdf2docx import Converter
from toolbox.common.file import get_filename
from toolbox.common.exceptions import ConvertPDFException


def convert_pdf_to_selectable(input_file: str, output_file) -> None:
    """Converts a PDF file to a selectable PDF file.

    Args:
        input_file (str): The path to the PDF file.
        output_file (str): The path to the selectable PDF file.
"""
    input_filename = get_filename(input_file)
    if output_file is None:
        output_file = f"{input_filename}_selectable.pdf"
    try:
        ocrmypdf.ocr(input_file, output_file, deskew=True)
    except Exception as err:
        raise ConvertPDFException(str(err)) from err


def convert_pdf_to_docx(pdf_file: str, docx_file: str):
    """Converts a PDF file to a docx file.

    Args:
        pdf_file (str): The path to the PDF file.
        docx_file (str): The path to the docx file.
    """
    pdf_filename = get_filename(pdf_file)
    if docx_file is None:
        docx_file = f"{pdf_filename}.docx"
    selectable_pdf = f"{pdf_filename}_selectable.pdf"
    convert_pdf_to_selectable(pdf_file, selectable_pdf)
    try:
        converter = Converter(selectable_pdf)
        converter.convert(docx_file, multi_processing=True)
        converter.close()
        os.remove(selectable_pdf)
    except Exception as err:
        raise ConvertPDFException(str(err)) from err
