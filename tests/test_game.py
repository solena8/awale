from game import Game
from hole import Hole
from abc import ABC


class Gamemixin(ABC):
    def _get_game(self):
        return Game("Soléna", "Sam")


class TestBoard(Gamemixin):

    def test_get_board_returns_a_list(self):
        board = self._get_game()
        assert type(board.get_board()) == list

    def test_get_boards_returns_a_list_of_instance_of_hole(self):
        board = self._get_game()
        assert all(isinstance(hole, Hole) for hole in board.get_board())


class TestDisplayBoard(Gamemixin):

    def test_display_board_when_game_starts(self):
        board = self._get_game()
        starting_board = board.display_board()
        correct_starting_board = " A  B  C  D  E  F\n(4)(4)(4)(4)(4)(4)\n(4)(4)(4)(4)(4)(4)\n G  H  I  J  K  L\nscores: P1: 0 - P2: 0"
        assert starting_board == correct_starting_board

    def test_display_board_when_game_has_seeds(self):
        board = self._get_game()
        board1 = board.get_board()
        board1[0].nb_of_seeds = 1
        starting_board = board.display_board()

        correct_starting_board = " A  B  C  D  E  F\n(1)(4)(4)(4)(4)(4)\n(4)(4)(4)(4)(4)(4)\n G  H  I  J  K  L\nscores: P1: 0 - P2: 0"
        assert starting_board == correct_starting_board



class TestSawSeeds(Gamemixin):

    def test_saw_8_seeds_from_index_0(self):
        game = self._get_game()
        game.current_hole = 0
        game.saw_seeds()
        board = game.get_board()
        board_A: Hole = board[0]
        board_B: Hole = board[1]
        assert board_A.nb_of_seeds == 0
        assert board_B.nb_of_seeds == 5



class TestHarvestSeeds(Gamemixin):

    def test_harvest_5_seeds_from_index_7(self):
        game = self._get_game()
        board1 = game.get_board()
        game.current_hole = 7
        board1[3].nb_of_seeds = 1
        board1[4].nb_of_seeds = 2
        board1[5].nb_of_seeds = 3
        board1[6].nb_of_seeds = 2
        board1[7].nb_of_seeds = 3
        game.harvest_seeds()
        assert board1[7].nb_of_seeds == 0
        assert board1[6].nb_of_seeds == 0
        assert board1[5].nb_of_seeds == 0
        assert board1[4].nb_of_seeds == 0
        assert board1[3].nb_of_seeds == 1
        assert game.current_player.score == 10


