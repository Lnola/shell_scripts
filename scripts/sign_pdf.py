import PyPDF2
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import random
import os

def create_signature_page(image_path, coordinates, page_width, page_height):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    for (x, y) in coordinates:
        # Calculate random offsets
        x += page_width * 0.02 * (random.uniform(-1, 1))
        can.drawImage(image_path, x, y, width=70, height=35, mask='auto')  # Adjust width and height as needed
    can.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf

def add_signatures(input_pdf, output_pdf, image_folder, coordinates):
    existing_pdf = PdfReader(open(input_pdf, "rb"))
    output = PdfWriter()

    page_width, page_height = letter

    # Get all PNG files from the folder
    image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(".png")]


    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]
        # Select a random signature for each page
        selected_image_path = random.choice(image_paths)
        new_pdf = create_signature_page(selected_image_path, coordinates, page_width, page_height)
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    with open(output_pdf, "wb") as outputStream:
        output.write(outputStream)

# Customize these variables
input_pdf = "ugovor.pdf"
output_pdf = "output.pdf"
image_folder = "./signatures"  # Path to the folder containing signature images
coordinates = [(430, 250), (430, 54)]  # Coordinates for each signature

add_signatures(input_pdf, output_pdf, image_folder, coordinates)
