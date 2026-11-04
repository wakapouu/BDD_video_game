import random
import db_init 
import time

def main():
    print_menu()
    choix = player_choice(1, 3)
    processus(choix)

def print_menu():
    texte1 = "JEU TRES COOL"
    center(texte1)
    print('1. Démarrer une partie')
    print('2. Voir le classement')
    print('3. Quitter')

def center(texte):
    print('=' * 20)
    print(texte.center(20))
    print('=' * 20)

def player_choice(min, max):
    while True:
        choix = input(f"Quelle action voulez-vous faire ? (Choisir entre {min} et {max})")
        if verify_player_choice(choix, min, max) is True:
            return int(choix)
        print('Erreur')

def verify_player_choice(choix, min, max):
    if choix.isdigit():
        choix = int(choix)
        if choix < min or choix > max:
            return False
        return True
    return False

def processus(choix):
    if choix == 1:
        team = select_character()
        start_wave(team)
    elif choix == 2:
        print('Classement')
    else:
        print('Quitter le jeu')

def select_character():
    team = []
    available_characters = get_characters()
    while len(team) <= 3:
        show_character_list(available_characters)
        user_champ_select(team, available_characters)
    return team

def start_wave(team):
    wave = 0
    enemy = new_opponent()
    handle_wave(team, wave, enemy)
    losing_screen(wave)

def handle_wave(team, wave, enemy):
    while is_team_alive(team):
        if is_enemy_alive(enemy):
            attack(team, enemy)
        else:
            wave += 1
            enemy = new_opponent()

def new_opponent():
    enemy = random_enemy()
    return enemy

def losing_screen(wave):
    print(f'Vous avez perdu ! Vous avez survécu {wave} manches !')

def is_enemy_alive(enemy):
    if enemy['hp'] > 0:
        return True
    return False

def is_team_alive(team):
    for character in team:
        if is_alive(character):
            return True
        return False

def is_alive(character):
    return character['hp'] > 0

def monster_attack(team, enemy):
    alive = get_alive_characters(team)
    target = random_character(alive)
    target_received_damage = target['hp'] - enemy_damage(target, enemy)
    print_monster_damage(enemy, target, target_received_damage)

def character_attack(team, enemy):
    alive = get_alive_characters(team)
    for character in alive:
        if is_enemy_alive(enemy):
            enemy_received_damage =  character_damage(enemy, alive)
            print_character_damage(character, enemy, enemy_received_damage)

def attack(team, enemy):
    character_attack(team, enemy)
    if is_enemy_alive(enemy):
        monster_attack(team, enemy)

def print_monster_damage(enemy, target, target_received_damage):
    print(f'{enemy['name']} attaque {target['name']} et inflige {target_received_damage} dégâts.')
    time.sleep(0.1)
    print(f'{target['name']} a désormais {target['hp']} PV.')
    time.sleep(0.5)

def print_character_damage(character, enemy, enemy_received_damage):
    print(f"{character['name']} attaque {enemy['name']} et inflige {enemy_received_damage} dégâts.")
    time.sleep(0.1)
    print(f'{enemy['name']} a désormais {enemy['hp']} PV.')
    time.sleep(0.5)

def attack(team, enemy):
    character_attack(team, enemy)

def random_enemy():
    random_number = random.randint(0, 9)
    find_enemy = db_init.database("enemy")
    random_number = find_enemy.find_one({'nb' : random_number})

def random_character(alive): 
     chosen_character = random.choice(alive)
     return chosen_character

def get_alive_characters(team):
    alive_characters = []
    for character in team:
        if is_alive(character):
            alive_characters.append(character)
        return alive_characters

def show_character_list(available_characters):
    for character in available_characters:
        print(f'NB : {character['nb']} NOM : {character['name']} | ATK : {character['atk']} | DEF : {character['def']} | PV : {character['hp']} ')

def user_champ_select(team, available_characters):
    choix = player_choice(1, 9)
    add_character(choix, team, available_characters)

def add_character(choix, team, available_character):
    user_choice = db_init.collection.find_one({'nb' : choix })
    if user_choice:
        team.append(user_choice)
        if user_choice in available_character:
            available_character.remove(user_choice)
    print('Erreur')

def get_characters():
    characters = db_init.database("characters")
    characters_list = list(characters)
    return characters_list

def enemy_damage(target, enemy):
    damage = enemy['atk'] - target['def']
    if damage < 0:
        damage = 0
    return damage

def character_damage(enemy, alive):
    damage = alive['atk'] - enemy['def']
    if damage < 0:
        damage = 0
    return damage

main()