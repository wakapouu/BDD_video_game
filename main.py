#main():
    #print_menu()
    #choix = player_choice(1,3)
    #processus(choix)

#print_menu():
    #texte1 = Nom du jeu
    #texte2 = Propositions de ce que le joueur peut faire 
    #center les textes

#center(texte):
    #Imprimer 20 * "="
    #Imprimer texte.center(20)
    #Imprimer 20 * "="

#player_choice(min,max)
    #Boucle infinie
        #choix = Demander le choix de l'utilisateur
        #Si verify_player_choice(choice,min,max):
            #renvoyer l'int(choix)
        #Message d'erreur

#verify_player_choice(choice,min,max)
        #Si choix is digit
            #choix = int(choix)
            #Si choix < min ou choix > max
                #Renvoyer False
            #Renvoyer True
        #Renvoyer False

#processus(choix):
    #Si choix == 1:
        #equipe = select_character():
        #start_game(equipe)
    #Si choix == 2:
        #Montrer le classement()
    #Sinon
        #Quitter le jeu()

#select_character():
    #Initialiser une liste équipe
    #available_characters = get_characters()
    #Tant que mon équipe n'a pas 3 membres
        #show_character_list(available_characters)
        #user_champ_select(equipe, available_characters)
    #return équipe

#start_game(equipe):
    #start_wave(equipe) 

#start_wave(equipe):
    #wave = 0
    #enemy = new_opponent()
    #fight(equipe,wave)
    #Losing screen(wave)

#fight(equipe,wave):
    #Tant que is_team_alive(equipe):
        #Si is_enemy_alive(enemy) 
            #attack(equipe, enemy)
        #Sinon
            #wave += 1
            #enemy = new_opponent()

#new_opponent():
    #enemy = random_enemy()
    #Renvoyer enemy

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

#monster_attack(equipe, enemy):
    #vivants = get_alive_characters(equipe)
    #cible = random_character(vivants)
    #HP cible + DEF cible - atk monstre 

#character_attack(equipe, enemy):
    #vivants = get_alive_characters(equipe)
    #pour chaque perso vivants
        #HP monstre + DEF monstre - ATK Joueur

#attack(team,enemy):
    #character_attack(team, enemy)
    #if is_enemy_alive(enemy):
        #monster_attack(team,enemy)

#random_enemy():
    #Générer un nombre aléatoire
    #ID du monstre <=> nbr aléatoire
    #Renvoyer le monstre

#random_character(vivants)
    #Choisir un perso aléatoirement dans vivants
    #Renvoyer le perso

#get_alive_characters(equipe):
    #personnage_vivants = []
        #Pour chaque personnage de l'équipe 
            #Si HP > 0 
                #Append à personnage_vivants
        #Renvoyer personnage_vivants

#show_character_list(available_characters):
    #Pour chaque perso dans available_characters
        #Afficher les caractéristiques séparément

#user_champ_select(equipe, available_characters):
    #choix = player_choice(1, 9)
    #add_character(choix, equipe, available_characters)

#add_character(choix, equipe, available_character)
    #.find le choix
    #le append à equipe
    #supprimer le choix de la liste de available_character

#get_characters():
    #Recuperer les persos depuis MongoDB
    #Mettre le résultat en liste
    #Return le résultat

