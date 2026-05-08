# 🥗 nutri-skills

**nutri-skills** è un ecosistema AI modulare progettato per trasformare una prescrizione nutrizionale statica in un assistente interattivo, dinamico e portatile. Sviluppato per chi segue la dieta mediterranea, il progetto automatizza la pianificazione dei pasti, l'analisi dei menù esterni (mense, ristoranti), la gestione della spesa e la creazione di ricette reali, mantenendo sempre la coerenza con le direttive del medico nutrizionista.

## 🚀 Visione del Progetto
A differenza delle app di dieta tradizionali, **nutri-skills** non richiede l'inserimento manuale di calorie. Utilizza l'intelligenza artificiale per interpretare i documenti medici originali, i gusti personali dell'utente e il contesto del momento (es. cosa offre la mensa aziendale oggi) per proporre scelte alimentari corrette in tempo reale.

---

## 🛠️ La Suite di Skill

Il progetto si basa su 4 skill specializzate, indipendenti e portatili:

### 1. `nutrition-planner` (The Architect)
È il cervello del sistema. Incorpora le regole nutrizionali estratte dalla **Guida Alimentare** (frequenze, dosi, blocchi).
- **Processo**: Analisi OCR di prescrizioni PDF, gestione profilo (allergie, blacklist), calcolo delle frequenze (Pesce 3v, Uova 3v, Formaggi 3v, Carne 2v).
- **Conoscenza**: Dosi precise (10g Olio, 120g Yogurt, 150g Frutta) e bilanciamento dei macro-nutrienti.
- **Esempio d'uso**: *"Analizza la mia nuova dieta PDF e crea il piano settimanale escludendo il merluzzo."*

### 2. `menu-matcher` (The Canteen Assistant)
Risolve il problema dei pasti fuori casa usando intelligenza gastronomica.
- **Processo**: Analizza menu da foto/screenshot/testo. Flagga i pasti come "consumati" in locale.
- **Logica**: Se il menu non offre il piatto previsto, propone uno **"Smart Swap"** con qualsiasi altro giorno della settimana. Conosce gli ingredienti "nascosti" nei piatti della tradizione.
- **Esempio d'uso**: *"Cosa posso mangiare oggi da questo screenshot del menu della Trattoria?"*

### 3. `grocery-manager` (The Personal Shopper)
Ottimizza l'approvvigionamento alimentare.
- **Processo**: Sottopone un Q&A per capire quanti pasti farai a casa. Genera una lista della spesa aggregata per reparto (Ortofrutta, Banco Frigo, ecc.).
- **Esempio d'uso**: *"Genera la lista della spesa per la settimana: pranzo fuori Lun-Ven."*

### 4. `recipe-chef` (The Creative Cook)
Trasforma il piano in ricette reali e azionabili.
- **Processo**: Analizza scontrini o liste spesa per conoscere l'inventario reale. Propone ricette italiane/mediterranee con tecnica "no-soffritto".
- **Esempio d'uso**: *"Chef, cosa cuciniamo stasera con gli ingredienti che ho comprato e il pesce spada previsto?"*

---

## 📂 Casi d'Uso Supportati
- **Bootstrap da PDF**: Creazione del piano digitale partendo da una scansione o PDF della dieta prescritta.
- **Multi-Format Output**: Generazione automatica di un PDF HD (basato sul template originale) e di una versione HTML responsive.
- **Analisi Gastronomica Intelligente**: Riconoscimento ingredienti in piatti complessi (es. Risotto = burro/grassi).
- **Smart Swapping & Persistence**: Gestione dinamica degli imprevisti tramite scambi di pasto tracciati in JSON locale.

---

## ⚙️ Installazione e Setup

1.  Clona il repository: `git clone https://github.com/andreamartelli/nutri-skills.git`
2.  Esegui l'installatore: `./setup.sh`
3.  Entra nel workspace e inizia: *"Attiva la skill nutrition-planner"*.

---
*Progetto sviluppato per Andrea Martelli. Dati nutrizionali basati sul piano del Dott. Massimo Mariani.*
