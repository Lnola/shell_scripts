import PyPDF2
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_signature_page(image_paths, coordinates):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    for (image_path, (width, height)) in zip(image_paths, coordinates):
        can.drawImage(image_path, width, height, width=100, height=50, mask='auto')  # Adjust width and height as needed
    can.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf

def add_signatures(input_pdf, output_pdf, image_paths, coordinates):
    existing_pdf = PdfReader(open(input_pdf, "rb"))
    output = PdfWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        new_pdf = create_signature_page(image_paths, coordinates)
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    with open(output_pdf, "wb") as outputStream:
        output.write(outputStream)

# Customize these variables
input_pdf = "input.pdf"
output_pdf = "output.pdf"
image_paths = ["signature.png", "signature.png"]  # Paths to your signature images
coordinates = [(100, 100), (200, 200)]  # Coordinates for each signature

add_signatures(input_pdf, output_pdf, image_paths, coordinates)
