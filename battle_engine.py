import random

# Optional: Type bonuses
type_advantages = {
    "Fire": "Grass",
    "Water": "Fire",
    "Grass": "Water"
}

def calculate_damage(attacker, defender):
    base = attacker["Attack"]
    defense = defender["Defense"]
    move_power = random.randint(40, 60)
    type_bonus = 1.5 if type_advantages.get(attacker["Type 1"]) == defender["Type 1"] else 1.0

    damage = ((base - defense) + move_power) * type_bonus
    return max(1, int(damage))

def battle_result(player, enemy):
    player_hp = player["HP"]
    enemy_hp = enemy["HP"]

    # Turn-based damage
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= calculate_damage(player, enemy)
        if enemy_hp <= 0:
            return "You win!"

        player_hp -= calculate_damage(enemy, player)
        if player_hp <= 0:
            return "You lose!"

    return "Draw"
