import sys
import json
import fitz
import os
from PIL import Image, ImageDraw, ImageFont

def render():
    if len(sys.argv) != 4:
        print("Usage: render_plan.py <template.pdf> <plan.json> <output.pdf>")
        sys.exit(1)

    template_path = sys.argv[1]
    json_path = sys.argv[2]
    out_path = sys.argv[3]

    # Dynamically extract user name from plan filename or generic default
    user_display_name = "Utente Nutri-Skills"

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)

    # 1. Open Template
    try:
        doc = fitz.open(template_path)
        page = doc[0]
        pix = page.get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        draw = ImageDraw.Draw(img)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # 2. Setup Fonts (User-Agnostic)
    try:
        font_paths = ["/System/Library/Fonts/Helvetica.ttc", "/Library/Fonts/Arial.ttf"]
        font_regular = None
        for p in font_paths:
            if os.path.exists(p):
                font_regular = ImageFont.truetype(p, 36)
                font_bold = ImageFont.truetype(p, 36, index=1 if ".ttc" in p else 0)
                font_italic = ImageFont.truetype(p, 30, index=2 if ".ttc" in p else 0)
                break
        if not font_regular:
            font_regular = ImageFont.load_default()
            font_bold = font_regular
            font_italic = font_regular
    except:
        font_regular = ImageFont.load_default()
        font_bold = font_regular
        font_italic = font_regular

    # 3. Render Data
    cols = [80, 565, 1055, 1545, 2035, 2530, 3015]
    y_offsets = [520, 890, 1230, 1630, 1980] 
    line_spacing = 45

    for col_idx, day_data in enumerate(data):
        if col_idx >= len(cols): break
        x = cols[col_idx]
        for row_idx, meal_items in enumerate(day_data):
            if row_idx >= len(y_offsets): break
            y_cursor = y_offsets[row_idx]
            if not isinstance(meal_items, list): continue
            
            for item in meal_items:
                text = str(item.get("text", ""))
                style = item.get("style", "normal")
                
                f = font_regular
                color = (50, 50, 50)
                if style == "protein":
                    f = font_bold
                    color = (33, 97, 140)
                elif style == "alt":
                    f = font_italic
                    color = (211, 84, 0)
                    y_cursor += 12
                
                draw.text((x, y_cursor), text, font=f, fill=color)
                y_cursor += line_spacing

    # Dynamic Footer (Anonymous)
    draw.text((3100, 2400), f"Generato per: {user_display_name}", font=font_italic, fill=(180, 180, 180))

    img.save(out_path, "PDF", resolution=300.0)
    print(f"Generated PDF: {out_path}")

if __name__ == "__main__":
    render()
