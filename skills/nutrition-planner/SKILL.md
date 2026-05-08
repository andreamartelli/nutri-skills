---
name: nutrition-planner
description: Expert AI nutritionist. Handles OCR prescription analysis, dynamic plan generation (piano.json), and robust PDF/HTML rendering for Mediterranean diets.
---

# Nutrition Planner Skill (Hardened)

## Overview
Questa skill è il motore primario dell'ecosistema. È progettata per garantire affidabilità totale nella trasformazione di dati medici in piani d'azione quotidiani.

## 1. Domain Knowledge (Mandatory Rules)
L'agente deve applicare rigorosamente queste specifiche estratte dalla "Guida Alimentare":
- **Struttura Pasti**: Proteina + Carboidrato + Grasso (Olio EVO 10g a crudo) + Verdura (200g).
- **Frequenze Settimanali**: Pesce (3v), Uova (3v), Formaggi Magri (3v), Carne Bianca (2v), Legumi (3v).
- **Dosi Standard**: Yogurt (120g), Pane (100g), Frutta (150g x 2).

## 2. Dynamic Initialization (Zero-to-Hero)
Se i file in \`data/\` mancano:
1. **Analisi OCR**: Chiede il PDF della prescrizione. Deve estrarre dosi, alimenti permessi e frequenze.
2. **Assessment**: Chiede tramite \`ask_user\`:
   - Modalità pranzo (Mensa, Casa, Bar).
   - Preferenze proteine e blacklist (es. "no peperoni").
   - Conferma colazione standard (Yogurt magro frutta 120g + biscotti + mandorle).
3. **Generazione JSON**: Crea \`data/piano.json\` e \`data/profilo_utente.json\` seguendo le specifiche tecniche sotto riportate.

## 3. Data Structure Specification (JSON Schema)
\`piano.json\` deve essere una lista di 7 giorni. Ogni giorno è una lista di 5 pasti. Ogni pasto è una lista di oggetti:
\`{"text": "descrizione", "style": "normal"|"protein"|"alt"}\`.

## 4. Execution & Delivery
Dopo ogni creazione o modifica:
1. **Aggiorna JSON**: Salva in \`data/piano.json\`.
2. **Render PDF**: Esegue \`python3 <SKILL_PATH>/scripts/render_plan.py templates/Template\ dieta.pdf data/piano.json Piano_Settimanale.pdf\`.
3. **Render HTML**: Esegue \`python3 <SKILL_PATH>/scripts/json_to_html.py data/piano.json Piano_Settimanale.html\`.

*Nota: <SKILL_PATH> viene risolto dinamicamente dallo script setup.sh.*
