import tkinter as tk
from tkinter import messagebox, simpledialog
from pokemon_data import load_pokemon_data, get_starter_options, get_balanced_enemy
from battle_engine import battle_result

df = load_pokemon_data()

class PokemonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Pokémon Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#d2f0c2")

        self.player_name = ""
        self.player_pokemon = None
        self.enemy_pokemon = None

        self.start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Pokémon", font=("Courier", 20), bg="#d2f0c2").pack(pady=40)
        tk.Button(self.root, text="Start", font=("Arial", 14), command=self.get_player_name).pack(pady=10)

    def get_player_name(self):
        self.player_name = simpledialog.askstring("Your Name", "What is your name, trainer?")
        if self.player_name:
            self.starter_selection()

    def starter_selection(self):
        self.clear_screen()
        self.starters = get_starter_options(df)
        tk.Label(self.root, text=f"Hello {self.player_name}!\nChoose your starter!", bg="#d2f0c2", font=("Arial", 14)).pack(pady=20)
        
        for _, row in self.starters.iterrows():
            name = row["Name"]
            btn = tk.Button(self.root, text=name, width=20, command=lambda r=row: self.choose_starter(r))
            btn.pack(pady=5)

    def choose_starter(self, row):
        self.player_pokemon = row
        messagebox.showinfo("Starter Chosen", f"You chose {row['Name']}!")
        self.show_battle_screen()

    def show_battle_screen(self):
        self.clear_screen()
        self.enemy_pokemon = get_balanced_enemy(df, self.player_pokemon)

        tk.Label(self.root, text=f"{self.player_name} vs Wild {self.enemy_pokemon['Name']}", font=("Arial", 12), bg="#d2f0c2").pack(pady=20)
        tk.Label(self.root, text=f"Your Pokémon: {self.player_pokemon['Name']}", bg="#d2f0c2").pack()
        tk.Label(self.root, text=f"Enemy Pokémon: {self.enemy_pokemon['Name']}", bg="#d2f0c2").pack()

        tk.Button(self.root, text="Battle!", command=self.do_battle).pack(pady=30)

    def do_battle(self):
        result = battle_result(self.player_pokemon, self.enemy_pokemon)
        messagebox.showinfo("Battle Result", result)
        self.root.quit()

# Start game
if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonGame(root)
    root.mainloop()
