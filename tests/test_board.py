from board import Board
from hole import Hole

class TestBoard:
    def _get_board(self):
        return Board("Soléna", "Valentin")

    def test_get_board_returns_a_list(self):
        board = self._get_board()
        assert type(board.get_board()) == list

    def test_get_boards_returns_a_list_of_instance_of_hole(self):
        board = self._get_board()
        assert all(isinstance(hole, Hole) for hole in board.get_board())

    def test_display_of_board(self):
        board = self._get_board()
        print(board.display_board())