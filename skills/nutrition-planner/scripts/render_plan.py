import sys
import json
import fitz
import os
from PIL import Image, ImageDraw, ImageFont

if len(sys.argv) != 3:
    print("Usage: render_plan.py <plan.json> <output.pdf>")
    sys.exit(1)

# Get current script dir to resolve relative paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
TEMPLATE_PATH = os.path.join(REPO_ROOT, "templates", "Template dieta.pdf")

json_path = sys.argv[1]
out_path = sys.argv[2]

if not os.path.exists(TEMPLATE_PATH):
    print(f"Error: Template not found at {TEMPLATE_PATH}")
    sys.exit(1)

with open(json_path, 'r') as f:
    data = json.load(f)

# 1. Regenerate HD Image from PDF
doc = fitz.open(TEMPLATE_PATH)
page = doc[0]
pix = page.get_pixmap(dpi=300)
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
draw = ImageDraw.Draw(img)

# 2. Setup High-Quality Fonts
try:
    font_regular = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    font_bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36, index=1)
    font_small_italic = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30, index=2)
except:
    font_regular = ImageFont.load_default()
    font_bold = font_regular
    font_small_italic = font_regular

# 3. Offsets
cols = [80, 565, 1055, 1545, 2035, 2530, 3015]
y_offsets = [520, 890, 1230, 1630, 1980]
line_spacing = 45

for col_idx, day_data in enumerate(data):
    if col_idx >= len(cols): break
    x = cols[col_idx]
    for row_idx, meal_items in enumerate(day_data):
        if row_idx >= len(y_offsets): break
        y_cursor = y_offsets[row_idx]
        for item in meal_items:
            text = item.get("text", "")
            style = item.get("style", "normal")
            
            f = font_regular
            color = (50, 50, 50)
            if style == "protein":
                f = font_bold
                color = (33, 97, 140)
            elif style == "alt":
                f = font_small_italic
                color = (211, 84, 0)
                y_cursor += 12
            
            draw.text((x, y_cursor), text, font=f, fill=color)
            y_cursor += line_spacing

draw.text((3100, 2400), "Dott. Massimo Mariani | Andrea Martelli", font=font_small_italic, fill=(180, 180, 180))

# Save as PDF
img.save(out_path, "PDF", resolution=300.0)
print(f"Successfully generated PDF: {out_path}")
