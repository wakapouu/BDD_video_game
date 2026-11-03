#main():
    #print_menu()
    #player_choice(1,3)
    #processus(choix)

#print_menu():
    #texte1 = Nom du jeu
    #texte2 = Propositions de ce que le joueur peut faire 
    #center(texte)

#center(texte):
    #Imprimer 20 * "="
    #Imprimer texte.center(20)
    #Imprimer 20 * "="

#player_choice(min,max)
    #choix = Demander le choix de l'utilisateur
    #verify_player_choice(choice,min,max)

#verify_player_choice(choice,min,max)
    #Boucle infinie
        #Si choix is digit
            #choix = int(choix)
            #Si choix < min ou choix > max
                #Message d'erreur
            #Sinon:
                #return choix
        #Message d'erreur

#processus(choix):
    #Si choix == 1:
        #select_character():
    #Si choix == 2:
        #Montrer le classement()
    #Sinon
        #Quitter le jeu()

#select_character():
    #Initialiser une liste équipe
    #get_characters()*
    #Tant que mon équipe n'a pas 3 membres
        #show_character_list()*
        #user_champ_select()*
    #return équipe
    #start_game():

#start_game():
    #enemy = new_opponent()
    #start_wave():

#start_wave():
    #wave = 0
    #Tant que is_team_alive():
        #Si enemy_status() est True
            #attack()
        #Sinon
            #new_opponent()
            #wave += 1
    #Losing screen()

#new_opponent(wave):
    #random_enemy()
    #enemy_status() = True

#Losing screen(wave):
    #Afficher message perdu avec le nombre de waves survécues

#enemy_status():
    #Si HP enemy > 0
        #return True
    #return False

#is_player_alive(équipe):
    #Pour chaque personnages de équipe
        #si HP du perso > 0
            #...

#is_team_alive():
    #...

#monster_attack():
    #random_character()
    #HP joueur + DEF joueur - atk monstre 

#character_attack():
    #pour chaque is_player_alive():
        #HP monstre + DEF monstre - ATK Joueur

#attack():
    #monster_attack()
    #character_attack()

#random_enemy():
    #random_number(min,max)
    #ID du monstre <=> nbr aléatoire
    #Mettre le monstre choisi dans une liste

#random_character()
    #random_number(min,max)
    #ID du joueur <=> nbr aléatoire

#get_characters():
    #...

#show_character_list():
    #Prendre tout les characters depuis MongoDB
    #Afficher les caractéristiques séparément

#user_champ_select(equipe):
    #choix = Demander quel perso choisir
    #verify_player_choice(choix, 1, 10)
    #add_character(choix)

#add_character(choix)
    #.find le choix
    #le append à equipe
    #supprimer le choix de la liste des personnages

#random_number(min,max)
    #random.randint(min,max)