import sys
import ocrmypdf
from common.output import show_message


def convert_pdf_to_selectable(input_file: str, output_file: str) -> None:
    try:
        ocrmypdf.ocr(input_file, output_file, deskew=True)
    except Exception as err:
        show_message('Error converting to selectable pdf: {0}'.format(err))


def convert_pdf_to_docx():
    pass
