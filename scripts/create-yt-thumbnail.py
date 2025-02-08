from PIL import Image, ImageDraw, ImageFont
import random, os, argparse


def generate_color():
    return tuple(random.randint(0, 255) for _ in range(3))


def create_thumbnail(text):
    img = Image.new("RGB", (1280, 720), generate_color())
    draw = ImageDraw.Draw(img)
    font_size = 150
    font_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()

    text_size = draw.textbbox((0, 0), text, font=font)
    text_x = (1280 - (text_size[2] - text_size[0])) / 2
    text_y = (720 - (text_size[3] - text_size[1] + font_size / 2)) / 2

    draw.text((text_x, text_y), text, fill="white", font=font)
    img.save(os.path.join(os.path.expanduser("~"), "Desktop", "thumbnail.png"))
    img.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("title", type=str, help="Title text for the thumbnail")
    args = parser.parse_args()

    create_thumbnail(args.title)
