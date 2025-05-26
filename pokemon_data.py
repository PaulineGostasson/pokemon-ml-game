import pandas as pd
import random

def load_pokemon_data(filepath="data/Pokemon.csv"):
    df = pd.read_csv(filepath)
    df = df[~df["Name"].str.contains("Mega", na=False)]
    df = df.dropna(subset=["HP", "Attack", "Defense", "Speed"])
    return df

def get_starter_options(df):
    starters = [
        "Bulbasaur", "Charmander", "Squirtle",
        "Chikorita", "Cyndaquil", "Totodile",
        "Treecko", "Torchic", "Mudkip"
    ]
    return df[df["Name"].isin(starters)].sample(3, random_state=random.randint(1, 1000)).reset_index(drop=True)

def get_balanced_enemy(df, player_stats):
    total = sum([player_stats[col] for col in ["HP", "Attack", "Defense", "Speed"]])
    df["TotalStat"] = df["HP"] + df["Attack"] + df["Defense"] + df["Speed"]
    balanced = df[df["TotalStat"] <= total + 30]  # +/- 30 buffer
    return balanced.sample(1).iloc[0]
