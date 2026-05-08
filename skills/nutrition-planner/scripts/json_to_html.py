import sys
import json

if len(sys.argv) != 3:
    print("Usage: json_to_html.py <plan.json> <output.html>")
    sys.exit(1)

json_path = sys.argv[1]
out_path = sys.argv[2]

with open(json_path, 'r') as f:
    data = json.load(f)

days = ["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ", "SABATO", "DOMENICA"]
meals = ["Colazione", "Spuntino 1", "Pranzo", "Spuntino 2", "Cena"]

html = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Piano Alimentare Settimanale</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; text-align: center; border-bottom: 2px solid #e67e22; padding-bottom: 10px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; vertical-align: top; }
        th { background-color: #2c3e50; color: white; text-transform: uppercase; font-size: 13px; }
        .meal-name { font-weight: bold; color: #7f8c8d; font-size: 11px; text-transform: uppercase; margin-bottom: 5px; display: block; }
        .protein { color: #2980b9; font-weight: bold; }
        .alt { color: #d35400; font-style: italic; font-size: 0.9em; margin-top: 5px; display: block; }
        .normal { color: #333; }
        @media print { body { background: white; padding: 0; } .container { box-shadow: none; border: none; width: 100%; } }
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
    html += "                <tr>\n"
    for col_idx in range(7):
        html += "                    <td>\n"
        html += f'                        <span class="meal-name">{meal_label}</span>\n'
        day_meals = data[col_idx][row_idx]
        for item in day_meals:
            text = item.get("text", "")
            style = item.get("style", "normal")
            html += f'                        <div class="{style}">{text}</div>\n'
        html += "                    </td>\n"
    html += "                </tr>\n"

html += """            </tbody>
        </table>
    </div>
</body>
</html>
"""

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Successfully generated HTML: {out_path}")
