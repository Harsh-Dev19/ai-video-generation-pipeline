from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_thumbnail(title):
    width = 1280
    height = 720

    # Background color
    img = Image.new("RGB", (width, height), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 90)
    except:
        font = ImageFont.load_default()

    wrapped_text = textwrap.fill(title, width=20)

    text_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Shadow
    draw.multiline_text((x+4, y+4), wrapped_text, font=font, fill="black")

    # Main text
    draw.multiline_text((x, y), wrapped_text, font=font, fill="white")

    img.save("thumbnail.jpg")
    print("Thumbnail created: thumbnail.jpg")
