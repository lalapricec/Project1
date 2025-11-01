# 🧙‍♀️ Create Your Fantasy  
*A COMP 163 Project by Lauren Price*

## 📖 Overview
**Create Your Fantasy** is a text-based character creation and management program inspired by RPG systems.  
Players can **create**, **save**, and **load** custom fantasy characters — each with their own stats, class, and backstory.

This project demonstrates:
- Function definitions and modular design  
- File input/output (I/O)  
- User input validation  
- Dictionaries and lists  
- Loops and conditionals  

---

## 🧩 Features
✅ Create a new character  
✅ Automatic stat calculation  
✅ Save & load characters  
✅ Simple menu navigation  

---

## 🗂️ File Structure
project1_starter.py
README.md
sample_characters/ (optional)


---

## ⚙️ How It Works

### 1. Run the Program
python project1_starter.py


### 2. Use the Main Menu

Create new character
Load existing character
Quit

### 3. Create a Character  
Enter a name, class, level, and optional backstory. Stats are calculated automatically.

### 4. Save the Character  
Characters are saved in a simple text format:
Name: Aria
Class: Mage
Level: 5
Strength: 11
Defense: 7
Health: 60
Gold: 35
Equipment: Spellbook, Cloth Robe
Backstory: Scholar of the Runestones

### 5. Load a Saved Character  
Choose option 2 and type the filename.

---

## ⚔️ Character Classes

| Class   | Class Mod | Growth | Base Health | Starting Equipment |
|---------|-----------|--------|-------------|--------------------|
| Warrior | 5         | 3.0    | 30          | Short Sword, Leather Armor |
| Mage    | 1         | 2.0    | 20          | Spellbook, Cloth Robe |
| Rogue   | 3         | 2.5    | 24          | Dagger, Cloak |
| Ranger  | 2         | 2.7    | 26          | Bow, Light Armor |

---

## 🧠 Key Functions

| Function | Purpose |
|----------|---------|
| `get_valid_class()` | Validates class input |
| `calculate_stats()` | Calculates stats based on class + level |
| `create_character()` | Builds and returns a character dictionary |
| `save_character()` | Saves character data to a text file |
| `load_character()` | Loads character data back into the program |
| `menu()` | Displays menu options |
| `main()` | Runs the main loop |

---

## 💾 File Format Example
Name: Kael
Class: Ranger
Level: 3
Strength: 10
Defense: 8
Health: 45
Gold: 25
Equipment: Bow, Light Armor
Backstory: A forest scout with unmatched precision. 

---

## 🧑‍💻 Author’s Notes
This project was created for **COMP 163** and demonstrates understanding of Python fundamentals.  
AI assistance was used for documentation and explanation support.  

---

## 🏁 Final Note
> “Every hero starts with a story — create yours!”  
This project implements required COMP 163 concepts using functions and file I/O.
