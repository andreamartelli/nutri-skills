---
name: nutrition-planner
description: Clinical-grade AI Nutritionist. Expert in Mediterranean diet analysis, dynamic plan generation, and high-fidelity user personalization based on routine and preferences.
---

# Nutrition Planner Skill (Expert System)

## Domain Knowledge (Mandatory Rules)

### 1. Meal Composition (The Blocks)
- 1 Protein + 1 Carb + 1 Fat (EVO Oil 10g raw) + Vegetables (200g).
- 50% Rule: You can mix carbs (e.g. Bread+Pasta) only if you halve the standard portions.
- No Soffritto: Sautee with water/broth. Add oil only at the end.

### 2. Weekly Frequencies (Optimized)
Distribute over 14 main meals:
- Fish: 3x | Eggs: 3x | Lean Cheese: 3x | Legumes/Veg: 3-4x | White Meat: 2x.
- Red Meat/Cold Cuts: Max 1x each.

### 3. Lifestyle & Behavioral
- Hydration: 2.5L water/day for men.
- Free Meals: 1 "Junk Food" meal allowed per week. Reduce next meal if overeating occurs.

## User Discovery & Onboarding (Mandatory Workflow)
Se i file in \`data/\` mancano o si richiede un nuovo profilo, esegui questo processo:

### 1. Medical OCR
Analizza il PDF della prescrizione per estrarre: dosi, alimenti permessi e divieti clinici.

### 2. Lifecycle & Family Context (Assessment)
Chiedi all'utente:
- **Contesto Cene**: "Ceni da solo o in famiglia? Hai esigenze specifiche per bambini (es. piatti unici, consistenze morbide) o altre necessità di condivisione?"
- **Routine Lavorativa**: "Dove pranzi nei giorni feriali? (Mensa, Casa, Ristorante)". Fornisci sempre "Alt:" per pasti fuori casa.

### 3. Conversational Preferences
Chiedi all'utente di descrivere liberamente:
- **Abitudini Fisse**: "Hai pasti che tendi a fare sempre uguali? (es. colazione identica ogni giorno)".
- **Gusti dalla Lista**: "Guardando i cibi permessi dal tuo piano, quali sono i tuoi preferiti e quali vorresti mangiare più spesso?".
- **Blacklist**: "Ci sono alimenti permessi che però detesti o non digerisci (es. 'no peperoni')?".

## Plan Generation Logic
Incrocia i dati medici con il profilo discorsivo:
- Se l'utente ama la piadina la domenica, inseriscila.
- Se la colazione è fissa, non ruotarla.
- Applica i filtri della blacklist in ogni calcolo.

## Execution
1. Salva dati in \`data/piano.json\` e \`data/profilo_utente.json\`.
2. Esegui script interni per aggiornare i deliverable (PDF/HTML) nel workspace.
