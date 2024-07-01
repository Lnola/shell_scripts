#!/usr/bin/env python3

from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import random
import os
from datetime import datetime, timedelta


def get_current_date():
    now = datetime.now()
    if now.day > 23:
        next_month = now.replace(day=28) + timedelta(days=4)  # this will never fail
        next_month = next_month.replace(day=1)
        current_date = next_month.strftime("%m_%Y")
    else:
        current_date = now.strftime("%m_%Y")

    return current_date


def create_signature_page(image_paths, coordinates, page_width, page_height):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    for image_path, (x, y) in zip(image_paths, coordinates):
        # Calculate random offsets
        x += page_width * 0.02 * (random.uniform(-1, 1))
        can.drawImage(
            image_path, x, y, width=70, height=35, mask="auto"
        )  # Adjust width and height as needed
    can.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)
    return new_pdf


def add_signatures(input_pdf, output_pdf, image_folder, coordinates):
    existing_pdf = PdfReader(open(input_pdf, "rb"))
    output = PdfWriter()

    page_width, page_height = letter

    # Get all PNG files from the folder
    image_paths = [
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if f.endswith(".png")
    ]

    num_pages_to_sign = 3
    for i in range(num_pages_to_sign):
        page = existing_pdf.pages[i]
        # Select unique random signatures for each coordinate on the page
        selected_image_paths = random.sample(image_paths, len(coordinates))
        new_pdf = create_signature_page(
            selected_image_paths, coordinates, page_width, page_height
        )
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

    # Add the remaining pages without signatures
    for i in range(num_pages_to_sign, len(existing_pdf.pages)):
        output.add_page(existing_pdf.pages[i])

    with open(output_pdf, "wb") as outputStream:
        output.write(outputStream)


def sign_pdf(input_pdf):
    # Customize these variables
    # Path to the folder containing signature images
    image_folder = "./assets/signatures"
    coordinates = [(430, 250), (430, 54)]  # Coordinates for each signature

    # Determine the output PDF file path
    input_folder = os.path.dirname(input_pdf)
    current_date = get_current_date()
    output_pdf = os.path.join(input_folder, f"{current_date}.pdf")

    add_signatures(input_pdf, output_pdf, image_folder, coordinates)
