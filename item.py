import db_init
import model


class Item:
    def __init__(self, name: str, description: str, droprate: str, rarity: str, item_type: str, stats=dict):
        self.name = name
        self.description = description
        self.droprate = droprate
        self.rarity = rarity
        self.item_type = item_type
        self.stats = stats

class Consumable(Item):
    def __init__(self, name: str, description: str, droprate: str, rarity: str, item_type: str, stats=dict):
        super().__init__(name, description, droprate, rarity, item_type, stats)

    def Use(self) -> None:
        # récupère la stat de l'objet et l'applique au personnage
        for stat, value in self.stats.items():
            if stat == "hp":
                # applique l'effet de soin
                pass
            elif stat == "attack":
                # applique l'effet d'attaque
                pass
            else:
                # applique l'effet de défense
                pass

class Equipable(Item):
    def __init__(self, name: str, description: str, droprate: str, rarity: str, item_type: str, stats=dict):
        super().__init__(name, description, droprate, rarity, item_type, stats)
