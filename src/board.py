from hole import Hole


class Board:
    def __init__(self, player1: str, player2: str):
        self.board: list = []
        for letter in "ABCDEF":
            self.board.append(Hole(letter, player1))
        for letter in "GHIJKL":
            self.board.append(Hole(letter, player2))

    def get_board(self):
        return self.board

    def display_board(self):
        player1_hole_names = "  ".join([hole.name for hole in self.board[:6]])
        player1_holes = "".join([f"({hole.nb_of_seeds})" for hole in self.board[:6]])
        player2_holes = "".join([f"({hole.nb_of_seeds})" for hole in self.board[:6]])
        player2_hole_names = "  ".join([hole.name for hole in self.board[6:]])
        board = (
                " " + player1_hole_names + "\n" +
                player1_holes + "\n" +
                player2_holes + "\n" +
                " " + player2_hole_names
        )
        return board
