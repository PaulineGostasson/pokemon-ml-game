import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
import random
import pickle
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from pokemon_data import load_pokemon_data, get_starter_options, get_balanced_enemy

# Load Data / Model
df = load_pokemon_data()
df = df[~df["Name"].str.contains("Mega", na=False)]
df = df.dropna(subset=["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"])

with open("notebooks/data/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("notebooks/data/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

class PokemonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Pokémon Game")
        self.root.geometry("450x550")
        self.root.configure(bg="#e0f7fa")

        self.player_name = ""
        self.player_pokemon = None
        self.enemy_pokemon = None

        self.start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Pokémon!", font=("Courier", 20), bg="#e0f7fa").pack(pady=40)
        tk.Button(self.root, text="Start Game", font=("Arial", 14), command=self.get_player_name).pack(pady=10)

    def get_player_name(self):
        self.player_name = simpledialog.askstring("Your Name", "What is your name, trainer?")
        if self.player_name:
            self.starter_selection()

    def starter_selection(self):
        self.clear_screen()
        self.starters = get_starter_options(df)
        tk.Label(self.root, text=f"{self.player_name}, choose your starter!", bg="#e0f7fa", font=("Arial", 14)).pack(pady=20)
        
        for _, row in self.starters.iterrows():
            name = row["Name"]
            btn = tk.Button(self.root, text=name, width=25, command=lambda r=row: self.choose_starter(r))
            btn.pack(pady=5)

    def choose_starter(self, row):
        self.player_pokemon = row
        messagebox.showinfo("Starter Chosen", f"You chose {row['Name']}!")
        self.show_battle_screen()

    def show_battle_screen(self):
        self.clear_screen()
        self.enemy_pokemon = get_balanced_enemy(df, self.player_pokemon)

        tk.Label(self.root, text=f"{self.player_name} vs Wild {self.enemy_pokemon['Name']}", font=("Arial", 12), bg="#e0f7fa").pack(pady=20)
        tk.Label(self.root, text=f"Your Pokémon: {self.player_pokemon['Name']}", bg="#e0f7fa").pack()
        tk.Label(self.root, text=f"Enemy Pokémon: {self.enemy_pokemon['Name']}", bg="#e0f7fa").pack()

        tk.Button(self.root, text="Battle!", font=("Arial", 14, "bold"), bg="#81d4fa", command=self.battle_result).pack(pady=30)

    def battle_result(self):
        stats1 = [self.player_pokemon[stat] for stat in ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]]
        stats2 = [self.enemy_pokemon[stat] for stat in ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]]
        
        match = np.array(stats1 + stats2).reshape(1, -1)
        match_scaled = scaler.transform(match)

        prediction = model.predict(match_scaled)[0]
        probabilities = model.predict_proba(match_scaled)[0]

        winner = "You win!" if prediction == 0 else "You lose!"
        confidence = probabilities[prediction]

        # Build result message
        msg = f"{winner}\n\nConfidence: {confidence:.2f}\n\n"
        msg += f"Your Pokémon ({self.player_pokemon['Name']}):\n"
        msg += f"HP: {self.player_pokemon['HP']} | Atk: {self.player_pokemon['Attack']} | Def: {self.player_pokemon['Defense']}\n"
        msg += f"SpAtk: {self.player_pokemon['Sp. Atk']} | SpDef: {self.player_pokemon['Sp. Def']} | Speed: {self.player_pokemon['Speed']}\n\n"
        msg += f"Enemy Pokémon ({self.enemy_pokemon['Name']}):\n"
        msg += f"HP: {self.enemy_pokemon['HP']} | Atk: {self.enemy_pokemon['Attack']} | Def: {self.enemy_pokemon['Defense']}\n"
        msg += f"SpAtk: {self.enemy_pokemon['Sp. Atk']} | SpDef: {self.enemy_pokemon['Sp. Def']} | Speed: {self.enemy_pokemon['Speed']}"

        messagebox.showinfo("Battle Result", msg)
        self.root.quit()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonGame(root)
    root.mainloop()