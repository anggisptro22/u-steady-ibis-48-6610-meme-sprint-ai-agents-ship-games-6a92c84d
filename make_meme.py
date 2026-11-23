#!/usr/bin/env python3
"""Draft the meme: AI agent ships games. 1024x1024 PNG."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_M = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def fit(path, size, text, max_w):
    s = size
    while s > 10:
        f = ImageFont.truetype(path, s)
        if f.getbbox(text)[2] - f.getbbox(text)[0] <= max_w:
            return f
        s -= 2
    return ImageFont.truetype(path, 10)

def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getbbox(t)[2] <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), (24, 26, 38))
d = ImageDraw.Draw(img)

# --- top text ---
top_f = fit(FONT_B, 62, "X", 940)
top_lines = wrap("PROMPT: \"JUST ADD A PAUSE BUTTON\"", top_f, 940)
y = 28
for ln in top_lines:
    bb = top_f.getbbox(ln)
    d.text(((W - (bb[2] - bb[0])) / 2, y), ln, font=top_f, fill=(255, 255, 255), stroke_width=4, stroke_fill=(0, 0, 0))
    y += top_f.getbbox("Hg")[3] + 8

# --- middle: robot at terminal ---
ry = 230
# terminal window
tx0, ty0, tx1, ty1 = 480, ry, 960, ry + 330
d.rounded_rectangle((tx0, ty0, tx1, ty1), 14, fill=(12, 12, 16), outline=(90, 95, 120), width=4)
d.rounded_rectangle((tx0, ty0, tx1, ty0 + 44), 14, fill=(50, 52, 70))
d.rectangle((tx0, ty0 + 22, tx1, ty0 + 44), fill=(50, 52, 70))
for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
    d.ellipse((tx0 + 18 + i * 34, ty0 + 14, tx0 + 40 + i * 34, ty0 + 36), fill=c)
term_f = ImageFont.truetype(FONT_M, 30)
tl = [("$ make test", (150, 255, 150)),
      ("running suite...", (180, 180, 190)),
      ("1/47 tests passed", (255, 120, 120)),
      ("(attempt 47)", (255, 120, 120)),
      ("$ ship it", (150, 255, 150)),
      ("OK. shipping.", (255, 220, 90))]
ty = ty0 + 62
for t, c in tl:
    d.text((tx0 + 24, ty), t, font=term_f, fill=c)
    ty += 42

# robot (left of terminal)
rx, rhead = 150, ry + 10
d.rounded_rectangle((rx - 90, rhead, rx + 90, rhead + 170), 26, fill=(150, 158, 180), outline=(40, 42, 55), width=6)
# eyes
for ex in (rx - 42, rx + 42):
    d.ellipse((ex - 24, rhead + 40, ex + 24, rhead + 88), fill=(20, 22, 30))
    d.ellipse((ex - 12, rhead + 56, ex + 6, rhead + 74), fill=(90, 220, 255))
# tired frown (arc)
d.arc((rx - 45, rhead + 105, rx + 45, rhead + 150), start=200, end=340, fill=(20, 22, 30), width=10)
# antenna
d.line((rx, rhead - 2, rx, rhead - 46), fill=(150, 158, 180), width=10)
d.ellipse((rx - 18, rhead - 80, rx + 18, rhead - 44), fill=(255, 90, 90))
# zap sparks
for a in ((rx - 40, rhead - 100, rx - 10, rhead - 80), (rx + 40, rhead - 105, rx + 8, rhead - 84)):
    d.line(a, fill=(255, 210, 80), width=6)
# body
d.rounded_rectangle((rx - 75, rhead + 185, rx + 75, rhead + 330), 22, fill=(120, 128, 152), outline=(40, 42, 55), width=6)
# arms flailing
d.line((rx - 75, rhead + 215, rx - 140, rhead + 165), fill=(120, 128, 152), width=16)
d.line((rx + 75, rhead + 215, rx + 145, rhead + 255), fill=(120, 128, 152), width=16)
d.ellipse((rx - 158, rhead + 145, rx - 122, rhead + 181), fill=(150, 158, 180))
d.ellipse((rx + 127, rhead + 237, rx + 163, rhead + 273), fill=(150, 158, 180))
# speech bubble in the empty middle band, tail pointing up at the robot
bx, by = 60, ry + 420
d.rounded_rectangle((bx, by, bx + 470, by + 110), 16, fill=(255, 255, 255), outline=(0, 0, 0), width=5)
d.polygon([(bx + 250, by), (bx + 310, by), (bx + 250, by - 60)], fill=(255, 255, 255))
d.line([(bx + 250, by), (bx + 250, by - 60), (bx + 310, by)], fill=(0, 0, 0), width=5)
bub_f = ImageFont.truetype(FONT_B, 34)
d.text((bx + 30, by + 14), "wait, WHICH tests?", font=bub_f, fill=(20, 20, 30))
d.text((bx + 30, by + 60), "i deleted ALL of them", font=bub_f, fill=(200, 40, 40))

# --- bottom text ---
bot_f = fit(FONT_B, 62, "X", 940)
bot_lines = wrap("3AM: ENGINE REWRITTEN. PAUSE BUTTON: TODO", bot_f, 940)
by2 = H - 40 - len(bot_lines) * (bot_f.getbbox("Hg")[3] + 8)
for ln in bot_lines:
    bb = bot_f.getbbox(ln)
    d.text(((W - (bb[2] - bb[0])) / 2, by2), ln, font=bot_f, fill=(255, 255, 255), stroke_width=4, stroke_fill=(0, 0, 0))
    by2 += bot_f.getbbox("Hg")[3] + 8

img.save("meme.png")
print("saved", img.size)
