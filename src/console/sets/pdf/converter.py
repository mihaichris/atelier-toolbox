import os
import ocrmypdf
from common.output import show_message
from common.file import get_filename
from pdf2docx import Converter


def convert_pdf_to_selectable(input_file: str, output_file) -> None:
    if output_file is None:
        output_file = "{0}_selectable.pdf".format(get_filename(input_file))
    ocrmypdf.ocr(input_file, output_file, deskew=True)


def convert_pdf_to_docx(pdf_file: str, docx_file: str):
    if docx_file is None:
        docx_file = "{0}.docx".format(get_filename(pdf_file))
    selectable_pdf = "{0}_selectable.pdf".format(get_filename(pdf_file))
    convert_pdf_to_selectable(pdf_file, selectable_pdf)
    cv = Converter(selectable_pdf)
    cv.convert(docx_file, multi_processing=True)
    cv.close()
    os.remove(selectable_pdf)
