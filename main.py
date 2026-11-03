#Main:
#Impression du menu
#Choix du joueur(1,3)
#Debut du processus(choix)

#Impression du menu:
    #Nom du jeu
    #Propositions de ce que le joueur peut faire 

#Choix du joueur(min,max)
#Boucle infinie
    #choix = Demander le choix de l'utilisateur
        #Si choix < min ou choix > max
            #Message d'erreur
        #Sinon
            #return l'int choix
    #break

#Processus(choix):
    #Si choix == 1:
        #Sélection des personnages:
    #Si choix == 2:
        #Montrer le classement
    #Si choix == 3:
        #Quitter le jeu

#Sélection des personnages:
    #Récupérer la BD de personnages de MongoDB et la mettre sous forme de liste
    #Initialiser une liste équipe
    #Tant que mon équipe n'a pas 3 membres
        #Montrer la liste de personnages*
        #L'utilisateur choisit son personnage*
            #Le personnage est mis dans la liste équipe
            #Le personnage est retiré de la liste MongoDB
            #return équipe
    #Début du jeu

#Début du jeu:
    #Initialisation de la wave
    #Choix aléatoire de l'ennemi
    #Tant que equipe en vie:
        #Si ennemi status est True
            #Attaque des persos en vie
            #Attaque du monstre
        #Si ennemi status est False
            #Choix aléatoire de l'ennemi
            #wave += 1
            #ennemi status = True
    #Losing screen

#Ennemi status
    #Si HP enemy > 0
        #return True
    #return False

#Joueurs en vie(équipe):
    #Pour chaque personnages de équipe
        #si HP du perso > 0

#Attaque du monstre:
    #Choisir un joueur aléatoire en vie dans l'équipe
    #HP joueur + DEF joueur - atk monstre 

#Attaque des persos:
    #pour chaque joueurs en vie
    #HP monstre + DEF monstre - ATK Joueur


#Choix aléatoire de l'ennemi:
    #Générer un nombre aléatoire entre 1 et 10
    #ID du monstre <=> nbr aléatoire
    #Mettre le monstre dans une liste





        





