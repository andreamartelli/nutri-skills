# nutri-skills: Smart Workspace Instructions

Questo workspace è il centro di comando del tuo ecosistema nutrizionale. Utilizza le skill globali attivandole con i comandi descritti nel README.

## Data & Persistence
- **data/piano.json**: Il database settimanale.
- **data/profilo_utente.json**: Allergie, intolleranze e blacklist.
- **data/state_settimanale.json**: Tracker dei pasti consumati e degli swap.

## Skill Integration Details

### nutrition-planner
Incorpora la conoscenza medica del Dott. Mariani:
- Dosi: 10g Olio, 120g Yogurt, 150g Frutta, ecc.
- Frequenze: Pesce (3v), Uova (3v), Formaggi (3v), Carne Bianca (2v), Legumi (3v).
- Workflow: Se i JSON mancano, analizza il PDF e crea il profilo.

### canteen-matcher
Usa intelligenza gastronomica per analizzare menu esterni (foto/testo). Flagga i pasti fatti nel tracker locale e propone scambi dinamici tra giorni diversi in caso di mismatch.

### grocery-manager
Genera liste spesa aggregate per reparto, chiedendo prima all'utente quanti pasti farà effettivamente a casa.

### recipe-chef
Propone ricette reali, bias mediterraneo, tecnica no-soffritto. Verifica la presenza degli ingredienti tramite scontrini o liste della spesa.
