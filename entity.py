import db_init
import main
import model

class Entity:

    def __init__(self, hp: int, defense: int, attack: int, maxhp: int):
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.maxhp = maxhp

    def isAlive() -> bool:
        ...

    def TakeDamage(self, amount: int) -> None:
        ...

    def Heal(self, amount: int) -> None:
        ...

    def Attack(self, target: "Entity") -> None:
        ...

    def PlayTurn(self) -> None:
        ...



class Player(Entity):

    def __init__(self, name: str, team: list[model.CharacterDB], inventory: list[model.Item], hp: int, defense: int, attack: int, maxhp: int):
        super().__init__(hp, defense, attack, maxhp)
        self.name = name
        self.team = team
        self.inventory = inventory

    def PlayTurn(self) -> None:
        ...
    def PickCharacter(self, character: model.CharacterDB) -> None:
        ...
    def IsTeamAlive(self) -> bool:
        ...
    def CheckInventory(self) -> None:
        ...
    def UseItem(self, item: model.Item) -> None:
        ...

class Monster(Entity):

    def __init__(self, name: str, hp: int, defense: int, attack: int, dropable: list[model.Item]):
        super().__init__(hp, defense, attack, hp)
        self.name = name
        self.dropable = dropable

    def PlayTurn(self) -> None:
        ...

    def DropLoot(self) -> list[model.Item]:
        ...
