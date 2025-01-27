from player import Player

class Hole:
    def __init__(self, letter: str, index: int, player_name: str):
        self.nb_of_seeds: int = 4
        self.letter: str = letter
        self.index: int = index
        self.owner: Player = Player(player_name)

    def __str__(self):
        return f"nb = {self.nb_of_seeds}, letter = {self.letter}, index = {self.index}, owner = {self.owner}"






