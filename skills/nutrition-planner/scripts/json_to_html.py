import sys
import json
import os

def to_html():
    if len(sys.argv) != 3:
        print("Usage: json_to_html.py <plan.json> <output.html>")
        sys.exit(1)

    json_path = sys.argv[1]
    out_path = sys.argv[2]

    if not os.path.exists(json_path):
        print(f"Error: JSON not found at {json_path}")
        sys.exit(1)

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)

    days = ["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ", "SABATO", "DOMENICA"]
    meals = ["Colazione", "Spuntino 1", "Pranzo", "Spuntino 2", "Cena"]

    html = """
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Piano Alimentare Settimanale</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; margin: 0; padding: 20px; color: #333; }
            .container { max-width: 1300px; margin: auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
            h1 { color: #2c3e50; text-align: center; border-bottom: 3px solid #e67e22; padding-bottom: 15px; margin-bottom: 30px; text-transform: uppercase; letter-spacing: 1px; }
            table { width: 100%; border-collapse: separate; border-spacing: 0; margin-top: 10px; table-layout: fixed; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }
            th, td { border: 0.5px solid #eee; padding: 15px; text-align: left; vertical-align: top; }
            th { background-color: #2c3e50; color: white; text-transform: uppercase; font-size: 14px; font-weight: 600; text-align: center; }
            .meal-row:nth-child(even) { background-color: #fafafa; }
            .meal-label { font-weight: bold; color: #95a5a6; font-size: 11px; text-transform: uppercase; margin-bottom: 8px; display: block; border-left: 3px solid #e67e22; padding-left: 8px; }
            .protein { color: #2980b9; font-weight: bold; margin-bottom: 4px; }
            .alt { color: #d35400; font-style: italic; font-size: 0.95em; margin-top: 8px; padding-top: 5px; border-top: 1px dashed #eee; display: block; }
            .normal { color: #2c3e50; margin-bottom: 2px; }
            @media print { body { background: white; padding: 0; } .container { box-shadow: none; border: none; width: 100%; max-width: 100%; } }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Piano Alimentare Settimanale</h1>
            <table>
                <thead>
                    <tr>
    """

    for day in days:
        html += f"                    <th>{day}</th>\n"

    html += """                </tr>
                </thead>
                <tbody>
    """

    for row_idx, meal_label in enumerate(meals):
        html += '                <tr class="meal-row">\n'
        for col_idx in range(7):
            html += "                    <td>\n"
            html += f'                        <span class="meal-label">{meal_label}</span>\n'
            try:
                day_meals = data[col_idx][row_idx]
                for item in day_meals:
                    text = item.get("text", "")
                    style = item.get("style", "normal")
                    html += f'                        <div class="{style}">{text}</div>\n'
            except:
                html += '                        <div class="normal">-</div>\n'
            html += "                    </td>\n"
        html += "                </tr>\n"

    html += """            </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    try:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Successfully generated HTML: {out_path}")
    except Exception as e:
        print(f"Error saving HTML: {e}")
        sys.exit(1)

if __name__ == "__main__":
    to_html()
