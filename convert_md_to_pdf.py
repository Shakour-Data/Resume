"""
convert_md_to_pdf.py

This script converts a Markdown file (Resume.md) to a PDF file (Resume.pdf).

Dependencies:
- markdown: pip install markdown
- pdfkit: pip install pdfkit
- wkhtmltopdf: must be installed on the system (https://wkhtmltopdf.org/)

Alternatively, you can use weasyprint instead of pdfkit if preferred.

Usage:
python3 convert_md_to_pdf.py
"""

import os
import markdown
import pdfkit

def convert_md_to_pdf(md_path: str, pdf_path: str):
    # Read Markdown content
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert Markdown to HTML
    html_text = markdown.markdown(md_text, extensions=['extra', 'smarty'])

    # Convert HTML to PDF
    # You can configure pdfkit options here if needed
    options = {
        'enable-local-file-access': None  # Needed to allow local file access for wkhtmltopdf
    }

    pdfkit.from_string(html_text, pdf_path, options=options)
    print(f"Converted '{md_path}' to '{pdf_path}' successfully.")

if __name__ == "__main__":
    md_file = "Resume.md"
    pdf_file = "Resume.pdf"
    if not os.path.exists(md_file):
        print(f"Error: Markdown file '{md_file}' not found.")
    else:
        convert_md_to_pdf(md_file, pdf_file)
