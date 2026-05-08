# Canteen Matcher Skill (Expert)

## Overview
Analizzatore di menu esterni con intelligenza gastronomica. Gestisce l'incertezza dei pasti fuori casa.

## Culinary Domain Intelligence
Non limitarti alla lettura del testo. Se il menu cita:
- *"Carbonara"*: Identifica Uova + Guanciale (Grasso animale). Segnala come sgarro se non previsto.
- *"Pesce al forno"*: Assumi condimento con olio. Riduci l'olio nel resto del menu.
- *"Risotto"*: Identifica carboidrato complesso + burro.
Preferisci sempre insalate composte o proteine semplici (ai ferri/vapore).

## Smart Swap Logic
Se il pasto previsto per OGGI non è disponibile:
1. Analizza \`data/piano.json\` e cerca un match in *qualunque* altro giorno della settimana non ancora consumato.
2. Proponi lo scambio: *"Oggi mangiamo il pesce del venerdì, e venerdì faremo le uova di oggi"*.
3. Aggiorna \`data/state_settimanale.json\` per tenere traccia dello spostamento.

## Workflow
1. Ricevi input (Foto/Testo/PDF).
2. Leggi Master Plan e Tracker (\`state_settimanale.json\`).
3. Filtra piatti tramite Blacklist (\`profilo_utente.json\`).
4. Genera 2-3 opzioni di vassoio ottimali.
