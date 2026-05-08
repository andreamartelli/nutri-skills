# Grocery Manager Skill (Expert)

## Overview
Generatore di liste spesa dinamiche e intelligenti basate sulla vita reale dell'utente.

## Logic & Aggregation
1. **Pianificazione**: Chiede quali giorni pranzerai in mensa (default Lun-Ven) e se ci sono cene fuori.
2. **Estrazione**: Legge \`data/piano.json\`. Ignora i pasti "fuori casa".
3. **Quantità**: Somma gli ingredienti.
   - Es: 7 giorni di colazione = 1kg yogurt + 1 pacco biscotti + 250g mandorle.
   - Es: 3 pasti di pesce = 1 trancio spada + 2 branzini interi.
4. **Categorizzazione**: Divide la lista per reparti supermercato (Ortofrutta, Banco Frigo, Carne/Pesce, Dispensa).

## Workflow
1. Q&A Rapido su impegni settimana.
2. Generazione lista testuale nel workspace.
3. Suggerimento scadenze (compra il pesce fresco il giorno X).
