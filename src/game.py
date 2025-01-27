from board import Board
from player import Player


class Game:
    def __init__(self, player1_name: str, player2_name: str):
        self.player_1 = Player(player1_name)
        self.player_2 = Player(player2_name)
        self.board = Board(player1_name, player2_name)
        self.current_player = self.player_1
        self.current_hole = 0


    def return_next_hole_counterclockwise(self) -> int :
        if self.current_hole == 0:
            return 11
        else:
            return self.current_hole - 1

    def return_next_hole_clockwise(self) -> int:
        if self.current_hole == 11:
            return 0
        else:
            return self.current_hole + 1

    def saw_seeds(self):
        # Get seeds from current hole
        nb_of_seeds: int = self.board.board[self.current_hole].nb_of_seeds
        # Empty the current hole
        self.board.board[self.current_hole].nb_of_seeds = 0
        # Sow seeds counterclockwise
        for _ in range(nb_of_seeds):
            next_hole = self.return_next_hole_counterclockwise()
            self.board.board[next_hole].nb_of_seeds += 1
            self.current_hole = next_hole

    def harvest_seeds(self):
        # Check and harvest in clockwise direction
        nb_of_seeds = self.board.board[self.current_hole].nb_of_seeds
        while nb_of_seeds == 2 or nb_of_seeds == 3:
            # Add seeds to current player's score
            self.current_player.increment_score(nb_of_seeds)
            # Empty the hole
            self.board.board[self.current_hole].nb_of_seeds = 0
            # Move to next hole clockwise
            self.return_next_hole_clockwise()

    def change_player(self):
        # switch players when the game turn is done
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def get_input(self) -> int :
        print(self.board.display_board(self.player_1, self.player_2))
        # asking the current player which hole they want to retrieve seeds from
        str_input: str = input(f"{self.current_player.name} : Choose a starting hole: ")
        # looking for the corresponding index to the chosen letter
        for hole in self.board.board:
            if hole.letter == str_input:
                if hole.player_name != self.current_player.name:
                    print("This hole is not yours")
                    return self.get_input()
                return hole.index
        print("Invalid input. Please try again.")
        return self.get_input()


    def gameplay(self):
        while True:
            # getting the input from the current player
            self.current_hole = self.get_input()
            while self.board.board[self.current_hole].nb_of_seeds == 0:
                print("no seed available, choose another hole")
                self.current_hole = self.get_input()
            # doing the saw seed action
            self.saw_seeds()
            # doing the harvest seed action (if possible)
            self.harvest_seeds()
            # switching players
            self.change_player()

# @todo : add winning condition
