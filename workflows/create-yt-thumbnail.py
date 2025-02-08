#!/Users/lnola/python-venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Workflows
# @raycast.title Create YouTube Thumbnail
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ./assets/youtube.png
# @raycast.argument1 { "type": "text", "placeholder": "Titles" }

# Documentation:
# @raycast.description Create YouTube thumbnails with the argument titles.
# @raycast.author Luka Nola

from PIL import Image, ImageDraw, ImageFont
import random, os, argparse, re

SIZE_X = 1280
SIZE_Y = 720
FONT_SIZE = 150
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def generate_color():
    return tuple(random.randint(0, 255) for _ in range(3))


def clean_filename(title):
    return re.sub(r"[^a-zA-Z0-9]", "_", title)


def create_thumbnail(title):
    img = Image.new("RGB", (SIZE_X, SIZE_Y), generate_color())
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except:
        font = ImageFont.load_default()

    text_size = draw.textbbox((0, 0), title, font=font)
    text_x = (SIZE_X - (text_size[2] - text_size[0])) / 2
    text_y = (SIZE_Y - (text_size[3] - text_size[1] + FONT_SIZE / 2)) / 2

    draw.text((text_x, text_y), title, fill="white", font=font)
    filename = clean_filename(title) + ".png"
    img.save(os.path.join(os.path.expanduser("~"), "Desktop", filename))
    img.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("titles", type=str, nargs="+", help="Titles for thumbnails")
    args = parser.parse_args()

    # This way of interpreting comes from raycast understanding multiple strings as a single argument
    # To call this script from terminal, use: python create-yt-thumbnail.py "Title1 Title2"
    for title in args.titles[0].split(" "):
        create_thumbnail(title)
