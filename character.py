class Character:
    def __init__(self,equipement: list[model.Item], attack: int, defense: int):
        self.equipement = equipement
        self.attack = attack
        self.defense = defense


    def EquipItem(self, item: model.Item) -> None:
        ...

    def UnequipItem(self, item: model.Item) -> None:
        ...

    def isSlotAvailable(self, slot: str) -> bool:
        ...

    def GetEquipment(self, slot: str) -> model.Item:
        ...

    def ProjectDamage(self, target: "Entity") -> int:
        ...

    def PlayTurn(self) -> None:
        ...
        
    