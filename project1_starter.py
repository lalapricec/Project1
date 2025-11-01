# project1_starter.py
# COMP 163 - Project 1: Create Your Fantasy
# Implements: create_character, save_character, load_character, main menu
# Uses only functions and file I/O.
#
# AI Assistance Disclosure:
# I used AI assistance to help me improve code structure, understand functions,
# All final logic and testing were reviewed and verified by me.


VALID_CLASSES = {
    "warrior": {"class_mod": 5, "growth": 3, "base_health": 30, "equipment": ["Short Sword", "Leather Armor"]},
    "mage":    {"class_mod": 1, "growth": 2, "base_health": 20, "equipment": ["Spellbook", "Cloth Robe"]},
    "rogue":   {"class_mod": 3, "growth": 2.5, "base_health": 24, "equipment": ["Dagger", "Cloak"]},
    "ranger":  {"class_mod": 2, "growth": 2.7, "base_health": 26, "equipment": ["Bow", "Light Armor"]}
}

def get_valid_class():
    """Prompt until the user enters a valid class (case-insensitive). Returns the normalized class name."""
    print("Available classes:", ", ".join([c.capitalize() for c in VALID_CLASSES.keys()]))
    while True:
        choice = input("Choose a class: ").strip().lower()
        if choice in VALID_CLASSES:
            return choice
        else:
            print("Invalid class. Please choose a valid class from the list.")

def calculate_stats(char_class, level):
    """Return a dict of calculated stats for the given class (string) and level (int)."""
    info = VALID_CLASSES[char_class]
    class_mod = info["class_mod"]
    growth = info["growth"]
    base_health = info["base_health"]

    # Example stat formulas (consistent and simple)
    strength = int(class_mod + (level * growth))
    defense = int(class_mod + (level * (growth * 0.6)))
    health = int(base_health + (level * (growth * 4)))

    # Add any additional stats if desired
    stats = {
        "Strength": strength,
        "Defense": defense,
        "Health": health
    }
    return stats

def create_character():
    """Create a character by prompting the user. Returns a dict with character data."""
    print("\n--- Create New Character ---")
    name = input("Enter character name: ").strip()
    if name == "":
        print("Name cannot be empty. Using 'Unknown'.")
        name = "Unknown"

    char_class = get_valid_class()

    # Prompt for level and validate integer >= 1
    while True:
        level_str = input("Enter starting level (integer >= 1): ").strip()
        try:
            level = int(level_str)
            if level < 1:
                print("Level must be at least 1.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer for level.")

    # Optional bonus info: backstory and equipment selection
    backstory = input("Optional: write a one-line backstory (or press Enter to skip): ").strip()
    equipment = VALID_CLASSES[char_class]["equipment"][:]  # default starting equipment list copy

    # Calculate stats
    stats = calculate_stats(char_class, level)

    # Gold (simple calculation): base 10 + level * 5
    gold = 10 + level * 5

    character = {
        "Name": name,
        "Class": char_class.capitalize(),
        "Level": level,
        "Strength": stats["Strength"],
        "Defense": stats["Defense"],
        "Health": stats["Health"],
        "Gold": gold,
        "Equipment": equipment,
        "Backstory": backstory
    }

    print("\nCharacter created:")
    for k, v in character.items():
        print(f"{k}: {v}")
    return character

def save_character(character, filename):
    """
    Save character to a text file in the required format.
    Returns True on success, False on permission error.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            # Required simple format (one key: value per line)
            f.write(f"Name: {character.get('Name','')}\n")
            f.write(f"Class: {character.get('Class','')}\n")
            f.write(f"Level: {character.get('Level','')}\n")
            f.write(f"Strength: {character.get('Strength','')}\n")
            f.write(f"Defense: {character.get('Defense','')}\n")
            f.write(f"Health: {character.get('Health','')}\n")
            f.write(f"Gold: {character.get('Gold','')}\n")
            # Write equipment as comma-separated
            equipment = character.get("Equipment", [])
            f.write(f"Equipment: {', '.join(equipment)}\n")
            # Backstory may be empty
            f.write(f"Backstory: {character.get('Backstory','')}\n")
        print(f"Character saved to {filename}")
        return True
    except PermissionError:
        print(f"Permission denied: cannot write to {filename}")
        return False
    except Exception as e:
        # Generic fallback - can be removed if tests expect only the two specific errors
        print(f"Error saving character: {e}")
        return False

def load_character(filename):
    """
    Load a character from a file in the expected format.
    Returns a dict on success, None if file not found, or raises other exceptions.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = {}
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                # Expecting 'Key: value' format
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    data[key] = value
            # Post-process numeric fields
            if "Level" in data:
                try:
                    data["Level"] = int(data["Level"])
                except ValueError:
                    pass
            for num_field in ("Strength", "Defense", "Health", "Gold"):
                if num_field in data:
                    try:
                        data[num_field] = int(data[num_field])
                    except ValueError:
                        pass
            # Equipment split back to list
            if "Equipment" in data:
                data["Equipment"] = [x.strip() for x in data["Equipment"].split(",") if x.strip()]
            # Capitalize class value if present
            if "Class" in data:
                data["Class"] = data["Class"].capitalize()
            print(f"Character loaded from {filename}:")
            for k, v in data.items():
                print(f"{k}: {v}")
            return data
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except Exception as e:
        # If you want to handle other errors differently, you can expand this.
        print(f"Error loading character: {e}")
        return None

def menu():
    """Display menu and get user selection as an int (1-3)."""
    print("\n--- Character Creator Menu ---")
    print("1. Create new character")
    print("2. Load existing character")
    print("3. Quit")
    while True:
        choice = input("Choose an option (1-3): ").strip()
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Invalid option. Enter 1, 2, or 3.")

def main():
    """Main program loop."""
    print("Welcome to Create Your Fantasy (COMP 163 Project 1)\n")
    while True:
        choice = menu()
        if choice == 1:
            char = create_character()
            filename = input("Enter filename to save character (e.g., aria.txt): ").strip()
            if filename == "":
                filename = f"{char.get('Name','character')}.txt"
                print(f"No filename given. Using {filename}")
            success = save_character(char, filename)
            if not success:
                print("Failed to save character. Please check permissions and try again.")
        elif choice == 2:
            filename = input("Enter filename to load (e.g., aria.txt): ").strip()
            if filename == "":
                print("No filename entered.")
            else:
                loaded = load_character(filename)
                if loaded is None:
                    print("Could not load character (file missing or error).")
        elif choice == 3:
            print("Goodbye! Remember to push your changes to your GitHub repo for submission.")
            break

if __name__ == "__main__":
    main()



