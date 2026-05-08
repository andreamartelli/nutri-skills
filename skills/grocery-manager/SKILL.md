---
name: grocery-manager
description: Intelligent grocery list generator. Aggregates weekly plan requirements, handles pantry management, and optimizes shopping lists by store department.
---

# Grocery Manager Skill (Efficient Shopper)

## Overview
Questa skill trasforma il piano alimentare in un piano d'azione logistico. Ottimizza la spesa per evitare sprechi e dimenticanze.

## Logic & Aggregation
1. **Filtro Pasti**: Chiede quali pasti verranno fatti fuori casa (es. "Pranzi Lun-Ven in mensa") e li esclude dai calcoli.
2. **Aggregazione Dosi**: Somma le grammature del piano.
   - Yogurt: 7 giorni x 120g = 1 confezione da 1kg.
   - Pollo: 2 pasti x 200g = 400g di petto di pollo.
   - Mandorle: 7 giorni x 15pz = circa 200g.
3. **Pantry Logic**: Se l'utente specifica di avere già degli ingredienti (es. "Olio e riso ci sono"), la skill li marca come già presenti.

## Grocery List Structure
Genera una lista ordinata per reparti standard (per minimizzare i tempi in negozio):
- **Ortofrutta**: Verdure e frutta di stagione (basate sul piano).
- **Banco Frigo**: Yogurt, formaggi magri, uova.
- **Macelleria/Pescheria**: Carne e pesce freschi.
- **Dispensa**: Pasta, riso, cracker, gallette, olio.

## Workflow
1. Leggi data/piano.json.
2. Q&A veloce su pasti fuori casa e scorte esistenti.
3. Generazione lista testuale nel workspace.
4. Suggerimento scadenze (es. "Compra il pesce fresco il giorno in cui lo cucini").
