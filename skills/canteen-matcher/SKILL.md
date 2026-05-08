---
name: canteen-matcher
description: Professional assistant for eating out. Analyzes external menus (text/images) using culinary intelligence to find matches with the user's diet plan. Handles "Smart Swaps" and tracks meal consumption.
---

# Canteen Matcher Skill (Expert Assistant)

## Overview
Questa skill risolve il problema dei pasti "fuori controllo" (mensa, ristorante). Agisce incrociando il menu del giorno con il Master Plan e lo stato attuale della settimana.

## Culinary Intelligence
Non limitarti a cercare le parole. Usa la conoscenza del dominio culinario italiano per analizzare i piatti proposti:
- **Ingredienti Nascosti**: Se il menu dice "Pollo alla Cacciatora", sai che contiene olio/grassi e verdure (pomodoro, olive).
- **Bilanciamento Grassi**: Se un secondo è già condito (es. "Arrosto"), istruisci l'utente a non aggiungere l'olio previsto nel piano sull'insalata.
- **Sostituzioni**: Se il menu offre "Pasta al Pesto", identifica i grassi (pinoli, olio) e suggerisci di ridurre la quota grassi del resto del vassoio.

## Smart Swap & Persistence
Se il menu esterno non offre nulla di compatibile con il pranzo previsto per OGGI:
1. **Analisi Cross-Day**: Cerca un match in qualsiasi altro giorno della settimana (es. scambia il pesce del venerdì con le uova di oggi).
2. **Consulenza**: Spiega all'utente il perché dello scambio: "Oggi in mensa c'è un ottimo branzino, lo prendiamo al posto delle uova e spostiamo le uova a venerdì".
3. **Aggiornamento Stato**: Salva la modifica in data/state_settimanale.json. Flagga il pasto come "consumato".

## Input Types
Supporta:
- **Testo**: Copia-incolla da intranet.
- **Immagini**: Foto di menu cartacei o screenshot.
- **PDF**: Listini prezzi o menu settimanali scaricati.

## Workflow
1. Leggi data/piano.json e data/state_settimanale.json.
2. Analizza il menu fornito.
3. Proponi 2-3 opzioni di "Vassoio Ideale".
4. Evidenzia criticità (es. "Attenzione: questo piatto è fritto").
