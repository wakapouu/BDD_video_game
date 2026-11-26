import db_init
import main
import model
from random import choice, random

class Entity:

    def __init__(self, hp: int, defense: int, attack: int, maxhp: int):
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.maxhp = maxhp

    def isAlive(self) -> bool:
        if self.hp > 0:
            return True

    def TakeDamage(self, amount: int) -> None:
        damage_taken = amount - self.defense
        if damage_taken < 0:
            damage_taken = 0
        self.hp -= damage_taken

    def Heal(self, amount: int) -> None:
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def Attack(self, target: "Entity") -> None:
        target.TakeDamage(self.attack)

    def PlayTurn(self) -> None:
        NotImplementedError("This method should be implemented in subclasses.")

class Player(Entity):

    def __init__(self, name: str, team: list[model.CharacterDB], inventory: list[model.Item], hp: int, defense: int, attack: int, maxhp: int):
        super().__init__(hp, defense, attack, maxhp)
        self.name = name
        self.team = team
        self.inventory = inventory
        

    def PickCharacter(self, character: model.CharacterDB) -> None:
        # Tant que l'équipe n'est pas pleine
            # On montre les persos dispos
            # On demande au joueur de choisir un perso
            # On ajoute le perso choisi à l'équipe
        while len(self.team) < 3:
            #Montrer persos dispos 
            #Demander Input 
            # Ajouter le perso choisi à l'équipe
            


    def IsTeamAlive(self) -> bool:
        for character in self.team:
            if character.hp > 0:
                return True
        return False

    def CheckInventory(self) -> None:
        for item in self.inventory:
            # afficher les infos de l'objet

    def UseItem(self, item: model.Item) -> None:
        if isinstance(item, db_init.Consumable):
            item.Use()
            self.inventory.remove(item)
        elif isinstance(item, db_init.Equipable):
            self.EquipItem(item)



class Monster(Entity):

    def __init__(self, name: str, hp: int, defense: int, attack: int, dropable: list[model.Item]):
        super().__init__(hp, defense, attack, hp)
        self.name = name
        self.dropable = dropable

    def PlayTurn(self) -> None:
        # On choisit une cible aléatoire parmi les personnages en vie du joueur
        target = choice([character for character in main.player.team if character.isAlive()])
        self.Attack(target)

    def DropLoot(self) -> list[model.Item]:
        ...