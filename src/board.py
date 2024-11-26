from hole import Hole

class Board:
     def __init__(self, player_1: str, player_2: str):
        self.board: list[Hole] = [Hole("A", player_1), Hole("B", player_1), Hole("C", player_1),
                                Hole("D", player_1), Hole("E", player_1), Hole("F", player_1),
                                Hole("G", player_2), Hole("H", player_2), Hole("I", player_2),
                                Hole("J", player_2), Hole("K", player_2), Hole("L", player_2)]



     def get_board(self):
         return self.board

     def display_board(self):
         pass
