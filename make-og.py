"""Draw og.png - the 1200x630 picture a link preview shows (LinkedIn, iMessage, Slack, email).

Same palette as index.html's light theme. Fonts are Windows' own (Georgia for the
serif heading, Segoe UI for the text), so this runs with nothing installed but Pillow.
Re-run after changing the wording: python make-og.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BG, INK, MUTED, ACCENT, CHIP = "#f7f6f2", "#1d2321", "#5b6461", "#1f6f5c", "#e7f1ed"
W, H = 1200, 630


def font(name, size):
    return ImageFont.truetype(os.path.join(r"C:\Windows\Fonts", name), size)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 24, H], fill=ACCENT)                       # the accent edge
d.text((96, 120), "Lance Massey", font=font("georgiab.ttf", 92), fill=INK)
d.text((100, 250), "Secondary-school teacher who builds", font=font("segoeuib.ttf", 46), fill=INK)
d.text((100, 308), "and ships classroom software", font=font("segoeuib.ttf", 46), fill=INK)

x = 100
for chip in ("Maths manipulatives", "VR math rooms", "Games arcade", "Full-stack apps"):
    f = font("segoeui.ttf", 28)
    w = d.textlength(chip, font=f)
    d.rounded_rectangle([x, 404, x + w + 36, 456], radius=26, fill=CHIP)
    d.text((x + 18, 430), chip, font=f, fill=INK, anchor="lm")
    x += w + 52

d.text((100, 540), "tokkathedj.github.io", font=font("segoeuib.ttf", 34), fill=ACCENT)
img.save(os.path.join(HERE, "og.png"), optimize=True)
print("og.png", img.size, "%d KB" % (os.path.getsize(os.path.join(HERE, "og.png")) // 1024))
