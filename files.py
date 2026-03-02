from dataclasses import dataclass

# --- CHALLENGE A: What decorator goes here? ---
@dataclass
class Player:
    name: str
    level: int

    def save_game(self):
        # --- CHALLENGE B: Write the two lines to open the file in Append ("a") mode and write to it ---
        with open("players.txt", "a") as file:
             file.write(f"Name: {self.name}, Level: {self.level}\n")


print("--- Welcome to the Guild Registration ---")

while True:
    name_input = input("Enter hero name (or type 'quit' to exit): ")
    if name_input.lower() == 'quit':
        break

    # --- CHALLENGE C: Add the two keywords to make this try/except shield work ---
    try:
        level_input = int(input(f"What level is {name_input}? "))
        
        new_hero = Player(name_input, level_input)
        new_hero.save_game()
        print(f"Successfully registered {new_hero.name}!\n")
        
    except ValueError:
        print("Invalid input! Level must be a whole number. Try again.\n")