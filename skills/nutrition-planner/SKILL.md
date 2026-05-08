# Nutrition Planner Skill (Core)

## Overview
Gestisce il Master Plan e il profilo utente. Supporta l'inizializzazione automatica per nuovi utenti.

## Initialization Logic
Se `data/profilo_utente.json` o `data/piano.json` non esistono nel workspace corrente:
1. **Inizia Assessment Profilo**: Chiede Allergie, Intolleranze, Blacklist. Salva in `data/profilo_utente.json`.
2. **Inizia Assessment Piano**: Chiede Modalità pasti e preferenze proteine. Salva in `data/piano.json`.

## Deliverables Management
Tutti i file generati (PDF, HTML, Immagini) DEVONO essere salvati all'interno della cartella corrente (workspace) per garantire la visibilità e la portabilità dei risultati.

## Comandi
- PDF: python3 scripts/render_plan.py data/piano.json Piano_Settimanale.pdf
- HTML: python3 scripts/json_to_html.py data/piano.json Piano_Settimanale.html
