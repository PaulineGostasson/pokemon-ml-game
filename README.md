# Pokémon ML Battle Game 

This project is a machine learning-based Pokémon battle simulator built with Python and Tkinter. It combines real data from a Pokémon dataset with a trained classification model to simulate battles between Pokémon based on their stats.

Note: This game is not a perfect or fully polished product. It is my first attempt at combining machine learning with a game using real-world data. There is definitely room for improvement such as adding more accurate battle mechanics, better balancing, and visual effects but it represents a strong foundation for learning and development.

---

## Machine Learning Model

A Gradient Boosting Classifier is trained on thousands of simulated battles, using real Pokémon stats such as:
- HP
- Attack
- Defense
- Special Attack
- Special Defense
- Speed

Each "match" compares two Pokémon and predicts which one would win based on their stats.

---

## Game Features

- Choose your name and starter Pokémon (from a list of official starters)
- Battle a wild, balanced opponent (based on total stat range)
- The trained ML model predicts the winner
- UI built with `Tkinter`
- Shows prediction confidence
- Stats are displayed for both Pokémon

---

## File Overview

- `main.py` – Main game file (Tkinter GUI)
- `pokemon_data.py` - Functions for loading and filtering Pokémon from CSV
- `data/Pokemon.csv` – The original dataset from Kaggle
- `data/model.pkl` - Trained model
- `data/scaler.pkl` – Scaler used to normalize inputs
- `analysis.ipynb` - Jupyter Notebook used for training and evaluation

---

## Requirements

- Python 3.10
- Packages:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - tkinter (built-in)
  - jupyter (for analysis)

To install:
```bash
pip install -r requirements.txt
```

To run game:
```bash
python main.py
```


