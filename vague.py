import entity
import model


class Vague:
    def __init__(self, vague_actuelle, monsters: list[model.MonsterDB], team: list[entity.Player]):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters
        self.team = team

    def PickEnemies(self, vague: model.VagueDB) -> list[model.MonsterDB]:
        

    def PlayVague(self) -> None:
        while True:
            for character in self.team:
                character.PlayTurn()
            for monster in self.monsters:
                monster.PlayTurn()

    def GetDifficulty(self, lap: int) -> model.Difficulty:
        # on récupère la difficulté de la vague en fonction du tour actuel
        