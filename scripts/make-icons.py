"""Render the notebook-and-magnifier illustration as app icons."""
from pathlib import Path
from PIL import Image, ImageDraw

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
S = 1024
CREAM = '#f8f5ed'
INK = '#35575b'

def artwork(compact=False):
    canvas = Image.new('RGBA', (S, S), CREAM)
    d = ImageDraw.Draw(canvas)
    d.ellipse((55, 75, 969, 949), fill='#eadfba')
    book = Image.new('RGBA', (S, S))
    b = ImageDraw.Draw(book)
    b.rounded_rectangle((205, 192, 761, 823), radius=32, fill='#c9bc95')
    b.rounded_rectangle((188, 172, 743, 803), radius=30, fill='#fffdf4', outline=INK, width=7)
    b.line((272, 174, 272, 800), fill='#da9983', width=4)
    for y in (295, 390, 485, 580, 675):
        b.line((302, y, 697, y), fill='#d9e1d6', width=4)
    for y in (252, 350, 448, 546, 644, 742):
        b.ellipse((220, y, 238, y+18), fill='#587376')
    # Fruit shapes echo the illustration on the learning site's home screen.
    def apple(x, y):
        b.line((x+51, y+17, x+61, y-18), fill='#587376', width=7)
        b.ellipse((x+63, y-18, x+103, y+1), fill='#819d74')
        b.ellipse((x, y, x+72, y+100), fill='#d9816b', outline='#b46856', width=5)
        b.ellipse((x+47, y, x+120, y+100), fill='#d9816b', outline='#b46856', width=5)
        b.polygon([(x+38,y+14),(x+80,y+14),(x+80,y+89),(x+38,y+89)], fill='#d9816b')
    apple(337, 335)
    apple(493, 335)
    for x in (369, 529):
        b.ellipse((x-47, 503, x+47, 597), fill='#e0af58')
        if not compact:
            b.line((x-23, 516, x-7, 509), fill='#f7d796', width=6)
    book = book.rotate(8, resample=Image.Resampling.BICUBIC)
    canvas.alpha_composite(book)
    # The handle points down-left, as in the supplied reference.
    lens = Image.new('RGBA', (S, S))
    l = ImageDraw.Draw(lens)
    l.line((751, 642, 640, 837), fill='#294f58', width=63)
    l.ellipse((608, 806, 672, 870), fill='#294f58')
    l.ellipse((576, 421, 885, 730), fill='#b4c9b2b0', outline='#294f58', width=28)
    l.ellipse((608, 453, 854, 699), outline='#e4ece1b0', width=13)
    if not compact:
        l.arc((630, 474, 829, 673), 238, 295, fill='#fffdf4', width=15)
    canvas.alpha_composite(lens)
    return canvas.convert('RGB')

for size, name in ((180, 'apple-touch-icon.png'), (192, 'icon-192.png'), (512, 'icon-512.png'), (32, 'favicon.png')):
    artwork(size <= 32).resize((size, size), Image.Resampling.LANCZOS).save(ASSETS / name)
artwork().resize((512, 512), Image.Resampling.LANCZOS).save(ASSETS.parent.parent / 'icon-preview.png')
