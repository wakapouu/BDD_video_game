class Vague:
    def __init__(self, vague_actuelle, monsters: list[model.MonsterDB]):
        self.vague_actuelle = vague_actuelle
        self.monsters = monsters

    def PickEnemies(self, vague: model.VagueDB) -> list[model.MonsterDB]:
        ...

    def PlayVague(self) -> None:
        ...

    def GetDifficulty(self, lap: int) -> model.Difficulty:
        ...