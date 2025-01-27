from player import Player

class Hole:
    def __init__(self, letter: str, index: int, player_name: str):
        self.nb_of_seeds: int = 4
        self.letter: str = letter
        self.index: int = index
        self.owner: Player = Player(player_name)






