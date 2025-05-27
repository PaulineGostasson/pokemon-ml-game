import pickle
import numpy as np

# Load model/scaler
with open("notebooks/data/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("notebooks/data/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

print("Skriv in statistik för två Pokémon:")

def get_stats(player_num):
    print(f"\nPokémon {player_num}")
    hp = float(input("HP: "))
    attack = float(input("Attack: "))
    defense = float(input("Defense: "))
    sp_atk = float(input("Sp. Atk: "))
    sp_def = float(input("Sp. Def: "))
    speed = float(input("Speed: "))
    return [hp, attack, defense, sp_atk, sp_def, speed]

stats1 = get_stats(1)
stats2 = get_stats(2)

match = np.array(stats1 + stats2).reshape(1, -1)
match_scaled = scaler.transform(match)
prediction = model.predict(match_scaled)

print("\nResultat:")
print("Player 1 wins!" if prediction[0] == 0 else "Player 2 wins!")
