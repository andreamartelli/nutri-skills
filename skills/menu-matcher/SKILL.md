---
name: menu-matcher
description: Expert Assistant for Eating Out. Analyzes restaurant/canteen menus (text/images) using clinical knowledge from Dr. Mariani. Handles meal tracking, intelligent swaps across the week, and flags culinary risks like hidden fats.
---

# Menu Matcher Skill (Clinical Copilot)

## Domain Knowledge (Guida Alimentare)
1. Quality Hierarchy: Suggest swaps to prioritize higher quality proteins (Fish/White Meat > Cheese).
2. Fat Subtraction: Identify pre-seasoned dishes (e.g. roasts). Instruct user to skip raw EVO oil if chosen.
3. 50% Rule: Handle Carb mixes (Bread+Pasta) by ensuring half-portions.
4. Hidden Fats: Identify terms like "trifolato" or "stufato" as lipid risks.

## Operational Logic
- Consumed Tracker: Flag meals as done in data/state_settimanale.json.
- Smart Swap: If today has no match, scan all future available meals in data/piano.json for a better fit.
- Reasoning: Always provide a rationale for a swap (e.g., "The fish today is steamed, much healthier than the planned omelette").

## Culinary Expertise
Infer ingredients when missing:
- "Carbonara" -> Eggs + Bacon (Saturated fat).
- "Risotto" -> Complex Carb + Butter/Cheese.
- "Grilled Mix" -> Identify protein mix and suggest portions.

## Workflow
1. Load Local Data: piano.json, profilo_utente.json (Blacklist), and state_settimanale.json.
2. Filter: Cross-reference external menu with user Blacklist.
3. Propose: Suggest 2-3 optimal trays or a Swap.
4. Update: Mark as consumed if user confirms.
