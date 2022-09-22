from board import Board
from player import Player

class Mancala:
    """Defines an instance of the game mancala"""

    def __init__(self, name_1, name_2):
        self._playerA = Player("A", name_1)
        self._playerB = Player("B", name_2)
        self._board = Board(self._playerA, self._playerB)
        self._winner = None   # will be set to winner
        print("                                     Welcome to Mancala! ")
        print("  ")
        print("     This is a two-player game. The game board has 12 spaces numbered 1 through 12 and two goal spots")
        print("labeled A and B for players A and B, respectively. Spaces 1-6 are on A's side of the board while spaces")
        print("7-12 are B's side. Player A's goal is between spaces 6 and 7 while player B's goal is between 12 and 1.")
        print("The objective of the game is to have the most marbles in your goal by the time all the spaces are empty")
        print("     The Player A starts the game by choosing a pile of marbles from ")
        print("the A side of the board (spaces 1, 2, 3, 4, 5, or 6). Player A will pick up the pile of marbles in their")
        print("chosen starting space and move in ascending order around the board dropping one marble in each spot until")
        print("they have no marbles left in their hand. If the last space the player dropped a marble in was not empty,")
        print("the player will pick up that new pile of marbles and continue around the board. If they landed on an empty")
        print("space, however, player A's turn is over. If the player lands in their own goal, they can move again from")
        print("their side of the board. If a player has a turn, and their side of the board is completely empty, they may")
        print("move from the other player's side of the board. The game is over when their are no marbles left in any of")
        print("the spaces. To make a move, use the move() function with the space as a string argument.")
        print("For example: game1._playerA.move('1').")
        self._playerA.update_board_object(self._board)
        self._playerB.update_board_object(self._board)