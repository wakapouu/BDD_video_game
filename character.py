import db_init
import model


class Character:
    def __init__(self,equipement: list[db_init.Item], attack: int, defense: int):
        self.equipement = equipement
        self.attack = attack
        self.defense = defense


    def EquipItem(self, item: model.Item) -> None:
        # on vérifie si le slot est disponible pour équiper l'objet
        # si oui, on équipe l'objet et on met à jour les stats du personnage
        # si non, on affiche un message d'erreur

    def UnequipItem(self, item: model.Item) -> None:
        # on vérifie si l'objet est équipé
        # si oui, on le déséquipe et on met à jour les stats du personnage

    def isSlotAvailable(self, slot: str) -> bool:
        # on vérifie si le slot est disponible pour équiper un objet
        # si oui, on retourne True
        # si non, on retourne False
        

    def GetEquipment(self, slot: str) -> db_init.Item:
        # on retourne l'objet équipé dans le slot spécifié
        # si aucun objet n'est équipé, on retourne None

    def ProjectDamage(self, target: ) -> int:
        #fait une copie de l'entité cible et calcule les dégats projetés en fonction de l'attaque du personnage et de la défense de la cible
        #affiche les dégats projetés


    def PlayTurn(self) -> None:
        # On affiche les options du joueur (attaquer, utiliser un objet, etc.)
        # On récupère le choix du joueur
        # Si c'est attaquer, on choisit une cible et on attaque
        # Si c'est utiliser un objet, on choisit un objet et on l'utilise
    