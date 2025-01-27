from hole import Hole
from player import Player


class Board:
    def __init__(self, player1_name: str, player2_name: str):
        self.board: [Hole] = []
        # Initialize board directly in constructor
        for i, letter in enumerate("ABCDEF"):
            self.board.append(Hole(letter=letter, index=i, player_name=player1_name))
        for i, letter in enumerate("LKJIHG"):
            self.board.append(Hole(letter=letter, index=6 + i, player_name=player2_name))

    def get_board(self) -> list[Hole]:
        return self.board

    def display_board(self, player1: Player, player2: Player) -> str:
        player1_hole_letters: str = "  ".join([hole.letter for hole in self.board[:6]])
        player1_holes: str = "".join([f"({hole.nb_of_seeds})" for hole in self.board[:6]])
        player2_holes: str = "".join([f"({hole.nb_of_seeds})" for hole in reversed(self.board[6:])])
        player2_hole_letters: str = "  ".join([hole.letter for hole in reversed(self.board[6:])])
        scores: str = f"Scores: {player1.name}: {player1.get_score()} - {player2.name}: {player2.get_score()}"

        board = (
            " " + player1_hole_letters + " " + player1.name + "\n" +
            player1_holes + "\n" +
            player2_holes + "\n" +
            " " + player2_hole_letters + " " + player2.name + "\n" +
            scores
        )
        return board
