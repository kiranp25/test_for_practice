import requests
from dataclasses import dataclass

# --- ZONE 1: THE BLUEPRINT (OOP) ---
# Hint: Add the robot decorator to automatically build this class!
@dataclass
class Pokemon:
    name: str
    height: int
    weight: int
    defense: int

    # --- ZONE 2: THE SCRIBE (File Handling) ---
    def save_to_pc(self):
        # Hint: Open "pc_box.txt" in append ("a") mode using the Context Manager
        with open("pc_box.txt", "a") as file:
            # .title() just capitalizes the first letter so it looks nice!
            file.write(f"Name: {self.name.title()} | Height: {self.height} | Weight: {self.weight} | Def: {self.defense}\n")


print("--- Welcome to the Pokémon PC System ---")

while True:
    # We add .lower() because the API only accepts lowercase names!
    pkmn_name = input("\nEnter a Pokemon name to catch (or type 'quit'): ").lower()
    
    if pkmn_name == 'quit':
        print("Powering down the PC. Goodbye!")
        break

    # --- ZONE 4: THE SHIELD (Error Handling) ---
    # Hint: Start the safety shield here to protect the internet request!
    try:
        print(f"Searching the internet for {pkmn_name.title()}...")
        url = f"https://pokeapi.co/api/v2/pokemon/{pkmn_name}"
        
        # --- ZONE 3: THE WEB WEAVER (API) ---
        # Hint 1: What requests method fetches the URL?
        # Hint 2: What method turns the response into a dictionary?
        response = requests.get(url)
        data = response.json()
        
        # We extract the stats using your Nested Dungeon skills
        height = data['height']
        weight = data['weight']
        defense = data['stats'][2]['base_stat']
        
        # Create the object and save it!
        caught_pkmn = Pokemon(pkmn_name, height, weight, defense)
        caught_pkmn.save_to_pc()
    
        print(f"Gotcha! {pkmn_name.title()} was caught and saved to pc_box.txt!")
        
    # Hint: Catch the error if the internet request fails or the name is fake!
    # (Using 'Exception' catches ANY error that happens in the try block)
    except Exception:
        print("Error: Could not find that Pokemon! Check your spelling and try again.")