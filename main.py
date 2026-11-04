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
        choix = f"Quelle action voulez-vous faire ? (Choisir entre {min} et {max})"
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
        equipe = select_character()
        start_wave(equipe)
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

#select_character():
    #Initialiser une liste équipe
    #available_characters = get_characters()
    #Tant que mon équipe n'a pas 3 membres
        #show_character_list(available_characters)
        #user_champ_select(equipe, available_characters)
    #return équipe

def start_wave(equipe):
    wave = 0
    enemy = new_opponent()
    handle_wave(equipe, wave)
    losing_screen(wave)

#start_wave(equipe):
    #wave = 0
    #enemy = new_opponent()
    #handle_wave(equipe,wave)
    #Losing screen(wave)

def handle_wave(team, wave):
    while is_team_alive(equipe):
        if is_enemy_alive(enemy):
            attack(equipe, enemy)
        else:
            wave += 1
            enemy = new_opponent()

def new_opponent():
    enemy = random_enemy()
    return enemy

#handle_wave(equipe,wave):
    #Tant que is_team_alive(equipe):
        #Si is_enemy_alive(enemy) 
            #attack(equipe, enemy)
        #Sinon
            #wave += 1
            #enemy = new_opponent()

#new_opponent():
    #enemy = random_enemy()
    #Renvoyer enemy

def losing_screen(wave):
    print(f'Vous avez perdu ! Vous avez survécu {wave} manches !')

#Losing screen(wave):
    #Afficher message perdu avec le nombre de waves survécues

#is_enemy_alive(enemy):
    #Si HP enemy > 0
        #return True
    #return False

#is_team_alive(equipe):
    #Pour chaque perso de equipe
        #Si HP > 0
            #Renvoyer True
    #Renvoyer False

def is_team_alive(team):
    for character in team:
        if is_alive(character):
            return True
        return False

def is_alive(character):
    return character['hp'] > 0

#monster_attack(equipe, enemy):
    #vivants = get_alive_characters(equipe)
    #cible = random_character(vivants)
    #enemy_damage(cible, enemy)

#character_attack(equipe, enemy):
    #vivants = get_alive_characters(equipe)
    #pour chaque perso vivants
        #character_damage(enemy, vivants)

#attack(team,enemy):
    #characters_attack(team, enemy)
    #if is_enemy_alive(enemy):
        #monster_attack(team,enemy)

#random_enemy():
    #Générer un nombre aléatoire
    #ID du monstre <=> nbr aléatoire
    #Renvoyer le monstre

def random_enemy():
    random_number = random.randint(0, 9)
    find_enemy = db_init.database("enemy")
    random_number = find_enemy.find_one({'nb' : random_number})

#random_character(vivants)
    #Choisir un perso aléatoirement dans vivants
    #Renvoyer le perso

#get_alive_characters(equipe):
    #personnage_vivants = []
        #Pour chaque personnage de l'équipe 
            #Si HP > 0 
                #Append à personnage_vivants
        #Renvoyer personnage_vivants

def get_alive_characters(team):
    alive_characters = []
    for character in team:
        if is_alive(character):
            alive_characters.append(character)
        return alive_characters

def show_character_list(available_characters):
    for character in available_characters:
        print(f'NB : {character['nb']} NOM : {character['name']} | ATK : {character['atk']} | DEF : {character['def']} | PV : {character['hp']} ')

#show_character_list(available_characters):
    #Pour chaque perso dans available_characters
        #Afficher les caractéristiques séparément

def user_champ_select(team, available_characters):
    choix = player_choice(1, 9)
    add_character(choix, team, available_characters)

#user_champ_select(equipe, available_characters):
    #choix = player_choice(1, 9)
    #add_character(choix, equipe, available_characters)

def add_character(choix, team, available_character):
    available_character = db_init.collection.find({'nb' : choix })
    team.append(character)

#add_character(choix, equipe, available_character)
    #.find le choix
    #le append à equipe
    #supprimer le choix de la liste de available_character

def get_characters():
    characters = db_init.database("characters")
    characters_list = list(characters)
    return characters_list

#get_characters():
    #recup les persos depuis MongoDB
    #Mettre le résultat en liste
    #Return le résultat

#character_damage(enemy, vivants)
    #HP enemy + DEF enemy - ATK Joueur

#enemy_damage(cible, enemy)
    #HP cible + DEF cible - ATK enemy
