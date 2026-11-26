from vague import Vague
import entity
import db_init

class Game(entity.Player, db_init.MongoClient, Vague.vague):
    def __init__(self, player: entity.Player, mongoclient: db_init.MongoClient, vague: Vague.vague):
        self.player = player
        self.mongoclient = mongoclient
        self.vague = vague

    def StartGame(self) -> None:
        # On initialise le jeu (choix du personnage, etc.)
        # On lance la première vague
        self.vague.PlayVague()

    def LoadGame(self) -> None:
        # On charge une partie sauvegardée
        pass

    def SaveGame(self) -> None:
        # On sauvegarde la partie en cours
        pass

    def LaunchGame(self) -> None:
        # On lance le jeu (StartGame ou LoadGame)
        pass

    def ShowLeaderboard(self) -> None:
        # On affiche le classement des joueurs
        pass

    def ExitGame(self) -> None:
        # On quitte le jeu
        pass
