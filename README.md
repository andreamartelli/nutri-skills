# 🥗 nutri-skills

**nutri-skills** is a modular AI ecosystem designed to transform a static nutritional prescription into an interactive, dynamic, and portable assistant. Developed for those following the Mediterranean diet, the project automates meal planning, analysis of external menus (canteens, restaurants), grocery management, and recipe creation, while always maintaining consistency with a nutritionist's guidelines.

## 🚀 Project Vision
Unlike traditional diet apps, **nutri-skills** doesn't require manual calorie counting. It uses artificial intelligence to interpret original medical documents, user personal tastes, and the current context (e.g., today's office canteen offerings) to propose correct food choices in real-time.

---

## 🛠️ The Skill Suite

The project is built upon 4 specialized, independent, and portable skills:

### 1. `nutrition-planner` (The Architect)
The brain of the system. It handles translating the medical prescription into a digital plan (`piano.json`) and generating user documents.
- **Features**: OCR analysis of PDF prescriptions, user profile management (allergies, blacklist), calculation of weekly protein frequencies.
- **Usage Example**: *"Activate nutrition-planner and analyze my new summer diet, excluding bell peppers because I don't digest them well."*

### 2. `canteen-matcher` (The Canteen Assistant)
Solves the problem of eating out. It analyzes external menus and finds the perfect match with your diet.
- **Features**: Interprets menus from photos/screenshots/text using culinary domain knowledge. Suggests "Smart Swaps" (swapping meals between different days) if today's menu isn't compatible with the planned meal.
- **Usage Example**: *"Use canteen-matcher on this photo of the Trattoria menu and tell me what I can pick to stay on plan today."*

### 3. `grocery-manager` (The Personal Shopper)
Optimizes food procurement while reducing waste.
- **Features**: Conducts a quick Q&A to understand how many meals will be eaten at home. Reads the weekly plan and generates an aggregated shopping list by department (Produce, Dairy, Pantry, Meat/Fish).
- **Usage Example**: *"Generate the shopping list for next week: lunch in the canteen from Monday to Friday, and I have a dinner out on Saturday night."*

### 4. `recipe-chef` (The Creative Cook)
Transforms pantry ingredients into real Mediterranean tradition dishes.
- **Features**: Proposes real recipes based on purchased ingredients (analyzing receipts or shopping lists). Alerts if essential components for planned meals are missing.
- **Usage Example**: *"Chef, I bought everything except the beans. What can I cook tonight that is consistent with the plan and follows Italian cuisine?"*

---

## 🔄 Typical Operational Workflow

1.  **Sunday Evening**: Invoke `nutrition-planner` to generate the new week's menu.
2.  **Shopping Planning**: Invoke `grocery-manager` to know what to buy, excluding office lunches.
3.  **In the Canteen (Mon-Fri)**: At 12:00, paste the corporate menu text into `canteen-matcher` to decide your tray. If you choose a Thursday dish, the "swap" is automatically recorded.
4.  **Dinner at Home**: Ask `recipe-chef` for a quick recipe to cook the planned protein with the vegetables you have in the fridge.

---

## 📂 Supported Use Cases
- **Bootstrap from PDF**: Creation of a digital plan starting from a scan or PDF of a prescribed diet.
- **Multi-Format Output**: Automatic generation of an HD PDF (based on the original template) and a responsive HTML version for smartphones.
- **Intelligent Culinary Analysis**: Ability to recognize "hidden" ingredients in complex dishes (e.g., knowing that *Risotto alla milanese* implies the use of butter/fats).
- **Blacklist Management**: Automatic and persistent exclusion of disliked foods, allergens, or items prohibited by religious beliefs.
- **Smart Swapping**: Dynamic management of unforeseen events through meal swaps between days of the week.

---

## ⚙️ Installation and Setup

### Prerequisites
- **Gemini CLI** (or a compatible agent).
- **Python 3.10+** with libraries: `PyMuPDF (fitz)`, `Pillow`, `pdfplumber`.

### Quick Start
1.  Clone the repository: `git clone https://github.com/andreamartelli/nutri-skills.git`
2.  Run the installer: `./setup.sh` (copies skills locally and configures dependencies).
3.  Enter the workspace and start: *"Activate the nutrition-planner skill"*.

---
*Project developed for Andrea Martelli. Nutritional logic based on models by Dr. Massimo Mariani.*
