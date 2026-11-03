#Main():
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
    #Boucle infinie
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
    #Initialisation de la wave
    #enemy = Choix aléatoire de l'ennemi()
    #start_wave():

#start_wave():
    #Tant que is_team_alive():
        #Si enemy_status() est True
            #attack()
        #Sinon
            #new_opponent(wave)
    #Losing screen()

#new_opponent(wave):
    #random_enemy()
    #wave += 1
    #return wave
    #enemy_status() = True

#Losing screen(wave):
    #Afficher message perdu avec le nombre de waves survécues

#enemy_status():
    #Si HP enemy > 0
        #return True
    #return False

#player_alive(équipe):
    #Pour chaque personnages de équipe
        #si HP du perso > 0
            #...

#is_team_alive():

#monster_attack():
    #Choisir un joueur aléatoire en vie dans l'équipe
    #HP joueur + DEF joueur - atk monstre 

#character_attack():
    #pour chaque joueurs en vie
    #HP monstre + DEF monstre - ATK Joueur

#attack():
    #monster_attack()
    #character_attack()

#random_enemy():
    #Générer un nombre aléatoire entre 1 et 10
    #ID du monstre <=> nbr aléatoire
    #Mettre le monstre dans une liste
