from PIL import Image, ImageDraw, ImageFont
import textwrap
from get_quotes import get_quotes


def get_image():
    astr = get_quotes()
    para = textwrap.wrap(astr, width=17)

    MAX_W, MAX_H = 360 , 640
    im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(
        'SHOWG.TTF', 24)

    current_h, pad = 200, 20
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font)
        current_h += h + pad

    im.save('test.png')