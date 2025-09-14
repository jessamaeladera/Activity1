from PIL import Image, ImageDraw, ImageFont
import os

# ---------------------
# Canvas
# ---------------------
width, height = 600, 800
canvas = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(canvas)

# ---------------------
# Background (Pastel gold gradient)
# ---------------------
for y in range(height):
    r = 255
    g = 240 - int(y / 8)
    b = 200 - int(y / 12)
    draw.line([(0, y), (width, y)], fill=(r, g, max(b, 150)))

# ---------------------
# Colors
# ---------------------
gold_light = (255, 215, 0)
gold_dark = (184, 134, 11)
black = (0, 0, 0)

# ---------------------
# CUP BODY (flared)
# ---------------------
draw.ellipse((180, 130, 420, 180), fill=gold_light, outline=black, width=3)  # Rim
cup_points = [(180, 150), (420, 150), (370, 340), (230, 340)]
draw.polygon(cup_points, fill=gold_light, outline=black)
draw.ellipse((232, 320, 370, 360), fill=gold_light, outline=black, width=3)  # Bottom curve

# ---------------------
# HANDLES (equal size, overlapping cup)
# ---------------------
draw.arc((120, 155, 250, 355), start=50, end=270, fill=gold_dark, width=14)  # Left handle
draw.arc((360, 150, 480, 350), start=265, end=138, fill=gold_dark, width=14)  # Right handle

# ---------------------
# STEM
# ---------------------
draw.rectangle((280, 360, 330, 460), fill=gold_dark, outline=black, width=3)
draw.ellipse((250, 445, 360, 460), fill=gold_light, outline=black, width=3)

# ---------------------
# BASE
# ---------------------
draw.rectangle((190, 460, 420, 600), fill="black", outline="black")
draw.rectangle((160, 530, 440, 650), fill="black", outline="black")

# ---------------------
# TEXT (engraved effect)
# ---------------------
try:
    plate_font_small = ImageFont.truetype("timesbd.ttf", 20)
    plate_font_big   = ImageFont.truetype("timesbd.ttf", 30)
except:
    plate_font_small = ImageFont.load_default()
    plate_font_big = ImageFont.load_default()

texts = [("2ND PLACER", plate_font_small),
         ("INTRAMURALS 2025", plate_font_small),
         ("CCIS PHANTOMS", plate_font_big)]

def engraved_text_centered(text, y, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    x_center = width // 2
    x = x_center - (text_w // 2)
    # Shadow
    draw.text((x+1, y+1), text, font=font, fill=(80, 60, 20))
    # Highlight
    draw.text((x-1, y-1), text, font=font, fill=(255, 255, 200))
    # Main
    draw.text((x, y), text, font=font, fill=(120, 90, 30))

# ---------------------
# Add BISU logo if exists
# ---------------------
logo_path = r"C:\Users\jessa mae\Downloads\Activity 1\bisu_logo.png"  # Change to your actual path

if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")
    logo_width, logo_height = 120, 120
    logo = logo.resize((logo_width, logo_height), Image. Resampling. LANCZOS)
    logo_x = (width - logo_width) // 2
    logo_y = 200  # Center vertically on cup
    canvas.paste(logo, (logo_x, logo_y), logo)
else:
    print(f"Warning: Logo file not found at {logo_path}. Trophy will be created without logo.")

# ---------------------
# Add texts
# ---------------------
engraved_text_centered(texts[0][0], 510, texts[0][1])
engraved_text_centered(texts[1][0], 545, texts[1][1])
engraved_text_centered(texts[2][0], 585, texts[2][1])

# ---------------------
# Save & Show
# ---------------------
output_file = "golden_cup_trophy_with_logo.png"
canvas.save(output_file)
canvas.show()
print(f"Trophy saved as {output_file}")
