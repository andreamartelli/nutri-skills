# Istruzioni Smart Workspace - Nutrizione

Questo workspace è configurato per gestire il tuo ecosistema nutrizionale AI. L'agente utilizzerà le skill globali `nutrition-planner`, `canteen-matcher`, `grocery-manager` e `recipe-chef`.

## Gestione Dati e Output
- **Dati Persistenti**: Tutti i database vivono in `./data/` (JSON).
- **Output Generati**: Tutti i file visivi (PDF, HTML, PNG) vengono generati nella radice di questo workspace per facilità di accesso.
- **Template**: `./templates/Template dieta.pdf`.

## Regole di Inizializzazione
Se i file in `./data/` sono assenti, la skill `nutrition-planner` deve avviare il setup iniziale del profilo e del piano.

## Comandi Rapidi
- **"Aggiorna la dieta"**: Innesca il workflow di pianificazione e rigenera i file locali.
- **"Cosa mangio in mensa?"**: Analizza menu esterni e aggiorna lo stato locale.
- **"Genera lista spesa"**: Produce la lista basandosi sul piano e sullo stato attuale.
