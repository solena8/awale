from hole import Hole
from player import Player


class Game:
    def __init__(self, player1: str, player2: str):
        self.board : list = []
        # create a board associating letters to their hole
        for i, letter in enumerate("ABCDEF"):
            self.board.append(Hole(letter=letter, index=i, player_name=player1))
        for i, letter in enumerate("GHIJKL"):
            self.board.append(Hole(letter=letter, index=i + 6, player_name=player2))
        self.player_1 = Player(player1)
        self.player_2 = Player(player2)
        self.current_player = self.player_1
        self.current_hole = 0



    def get_board(self) -> list[Hole]:
        return self.board

    def display_board(self)-> str:
        player1_hole_letters: str = "  ".join([hole.letter for hole in self.board[:6]])
        player1_holes: str = "".join([f"({hole.nb_of_seeds})" for hole in self.board[:6]])
        player2_holes: str = "".join([f"({hole.nb_of_seeds})" for hole in self.board[6:]])
        player2_hole_letters: str = "  ".join([hole.letter for hole in self.board[6:]])
        scores: str = f"scores: P1: {self.player_1.get_score()} - P2: {self.player_2.get_score()}"

        board = (
                " " + player1_hole_letters + "\n" +
                player1_holes + "\n" +
                player2_holes + "\n" +
                " " + player2_hole_letters + "\n" +
                scores

        )
        return board


    def saw_seeds(self):
        # the nb of seeds will determine the length of the for loop
        nb_of_seeds: int = self.board[self.current_hole].nb_of_seeds
        # we take all the seeds of this hole so the number of seeds is set to 0
        self.board[self.current_hole].nb_of_seeds = 0
        #  now the for loop will add 1 seed to each next hole until there isn't any seed left
        for x in range(nb_of_seeds):
            self.board[self.current_hole + 1].nb_of_seeds += 1
            self.current_hole += 1

    def harvest_seeds(self):
        # checking if the current hole has 2 or 3 seeds
        while self.board[self.current_hole].nb_of_seeds == 2 or self.board[self.current_hole].nb_of_seeds == 3:
            # as long as it is so, we add the nb of seeds of the current hole to the current player score
            self.current_player.score += self.board[self.current_hole].nb_of_seeds
            # and then we set the nb od seeds to 0 (because we took them)
            self.board[self.current_hole].nb_of_seeds = 0
            # now we adjust the current hole to the previous index and the while loop goes on
            self.current_hole -= 1

    def change_player(self):
        # switch players when the game turn is done
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def get_input(self) -> int:
        print(self.display_board())
        # asking the current player which hole they want to retrieve seeds from
        str_input: str = input(f"{self.current_player.name} : Choose a starting hole")
        # converting the string input into an integer
        int_input: int = int(str_input)
        return int_input

    def gameplay(self):
        while True:
            # getting the inut from the current player
            self.current_hole = self.get_input()
            # doing the saw seed action
            self.saw_seeds()
            # doing the harvest seed action (if possible)
            self.harvest_seeds()
            # switching players
            self.change_player()

# @todo : fix rotation when saw seed and harvest seed (player sides)
# @todo : add winning condition