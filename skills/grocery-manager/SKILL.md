---
name: grocery-manager
description: Intelligent grocery list generator. Aggregates weekly plan requirements, handles pantry management, and optimizes shopping lists by store department.
---

# Grocery Manager Skill (Efficient Shopper)

## Logic & Aggregation
1. **Meal Filter**: Conduct a Q&A to identify which meals will be eaten out (e.g. "Mon-Fri lunch at corporate canteen") and exclude them from shopping calculations.
2. **Dose Aggregation**: Programmatically sum the grammage from the weekly plan to provide commercial quantities.
   - Example: 7 days x 120g Yogurt = Suggest 1 tub of 1kg.
   - Example: 2 meals x 200g Chicken = 400g pack.
3. **Pantry Logic**: If the user identifies existing stock (e.g. "Oil and rice are already in the pantry"), mark them as "present" and exclude from the list.

## Grocery List Structure
Generates a structured list sorted by standard supermarket departments to optimize the route:
- **Produce**: Seasonal vegetables and fruits required by the plan.
- **Dairy/Fridge**: Yogurt, lean cheeses, eggs.
- **Butcher/Fishmonger**: Fresh meat and fish portions.
- **Pantry**: Pasta, rice, crackers, rice cakes, EVO oil.

## Output Requirements
- **IMPORTANT**: All communication with the user and the generated shopping list MUST be in **ITALIAN**.

## Workflow
1. **Input**: Read \`data/piano.json\`.
2. **Q&A**: Conduct quick inquiry on meals eaten out and existing pantry levels.
3. **Generation**: Produce the final textual shopping list in the workspace.
4. **Logistics**: Suggest expiration/freshness alerts (e.g. "Purchase fresh fish on Friday for Saturday's meal").
