#!/bin/bash

file=$(echo "$1" | cut -f 1 -d '.')
selectable_file=$file"_selectable.pdf"

echo "Converting $file to DOCX..."

sh ./convert_scan_pdf_to_selectable_pdf.sh $1 $selectable_file

pdf2docx convert $selectable_file $file".docx"

rm $selectable_file