import PyPDF2
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_signature_page(signature_text, width, height):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(width, height, signature_text)
    can.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf

def add_signature(input_pdf, output_pdf, signature_text, page_number, x, y):
    existing_pdf = PdfReader(open(input_pdf, "rb"))
    output = PdfWriter()

    new_pdf = create_signature_page(signature_text, x, y)

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        if i == page_number:
            page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    with open(output_pdf, "wb") as outputStream:
        output.write(outputStream)

# Customize these variables
input_pdf = "input.pdf"
output_pdf = "output.pdf"
signature_text = "Your Signature"
page_number = 2  # 0-indexed, so this is the 3rd page
x = 100
y = 100

add_signature(input_pdf, output_pdf, signature_text, page_number, x, y)
