#!/Users/lnola/.python/venv/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.packageName Youtube Thumbnail
# @raycast.title Create YouTube Thumbnail
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ../../assets/icons/youtube.png
# @raycast.argument1 { "type": "text", "placeholder": "Titles" }
# @raycast.argument2 { "type": "text", "placeholder": "Rainbow (true/false)" }

# Documentation:
# @raycast.description Create YouTube thumbnails with the argument titles.
# @raycast.author Luka Nola

from PIL import Image, ImageDraw, ImageFont
import random, os, argparse, re, colorsys

SIZE_X = 1280
SIZE_Y = 720
FONT_SIZE = 150
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def generate_color(index, total, rainbow):
    if rainbow:
        r, g, b = colorsys.hsv_to_rgb(index / max(1, total - 1), 1.0, 1.0)
        return int(r * 255), int(g * 255), int(b * 255)
    return tuple(random.randint(0, 255) for _ in range(3))


def clean_filename(title):
    return re.sub(r"[^a-zA-Z0-9]", "_", title)


def create_thumbnail(title, index, total, rainbow=False):
    img = Image.new("RGB", (SIZE_X, SIZE_Y), generate_color(index, total, rainbow))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except:
        font = ImageFont.load_default()

    text_size = draw.textbbox((0, 0), title, font=font)
    text_x = (SIZE_X - (text_size[2] - text_size[0])) / 2
    text_y = (SIZE_Y - (text_size[3] - text_size[1])) / 2

    draw.text((text_x, text_y), title, fill="white", font=font)
    filename = clean_filename(title) + ".png"
    img.save(os.path.join(os.path.expanduser("~"), "Desktop", filename))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("titles", type=str, nargs="+", help="Titles for thumbnails")
    parser.add_argument("rainbow", type=str, help="Rainbow (true/false)")
    args = parser.parse_args()

    # This way of interpreting comes from raycast understanding multiple strings as a single argument
    # To call this script from terminal, use: python create-yt-thumbnail.py "Title1,Title2"
    titles = args.titles[0].split(",")
    total_titles = len(titles) + 1
    rainbow = args.rainbow.lower() == "true"

    for index, title in enumerate(titles):
        create_thumbnail(title.strip(), index, total_titles, rainbow)
