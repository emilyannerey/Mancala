from board import Board
from player import Player

class Mancala:
    """Defines an instance of the game mancala while initializing the Player class and Board class"""

    def __init__(self, name_1, name_2):
        self._playerA = Player("A", name_1)
        self._playerB = Player("B", name_2)
        self._playerA_route = ['1', '2', '3', '4', '5', '6', 'A', '7', '8', '9', '10', '11', '12']
        self._playerB_route = ['7', '8', '9', '10', '11', '12', 'B', '1', '2', '3', '4', '5', '6']
        self._board_object = Board()
        self._winner = None         # will be set to winner
        self._a_turn = True         # describes if it's player A's turn. Used to keep track of whose turn it is
        self._first_move = True     # makes sure a player's starting move is on their own side
        self._game_over = False     # if game is still in session, will be set to false

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

    def get_winner(self):
        """Return's winner of the game as player object"""
        return self._winner

    def move(self, player, space):
        """player chooses which space they will pick up marbles from"""
        board = self._board_object.get_board()
        if self.is_game_over():
            return

        if self._board_object.is_empty(space):  # makes sure player chooses a space with marbles
            return

        if self.wrong_player(player):
            return

        if self._board_object.check_side(player):  # check to see if side is empty
            pass
        elif self._first_move:
            if self.check_move(player, space):  # check to see if player makes a legal move
                pass
            else:
                print("Please pick a starting space on your side of the board!")
                return

        route = self.set_route(player)

        num_marbles = board[space]  # how many spaces the player can move
        board[space] = 0  # pick up all the marbles in initial space, so it's set to zero
        route_position = route.index(space)  # index of route list
        key = space

        while num_marbles != 0:
            if route_position == 12:
                route_position -= 12
                key = route[route_position]
                board[key] += 1
                num_marbles -= 1
            else:
                route_position += 1  # move forward one on route list
                key = route[route_position]
                self.check_points(key, player)
                board[key] += 1
                num_marbles -= 1

        if self.next_turn(player, key):
            return

        if self.ends_in_goal(key):
            return

        self._first_move = False
        self.move(player, key)

    def check_points(self, key, player):
        """Adds 1 point to player's data member self._points"""
        if key == "A" or key == 'B':
            if player == 'A':
                self._playerA.update_points()
            else:
                self._playerB.update_points()

    def set_route(self, player):
        """Sets player route data member"""
        if player == 'A':
            return self._playerA_route
        else:
            return self._playerB_route

    def ends_in_goal(self, space):
        """Returns True if the player ended in their points pile. Returns false, otherwise"""
        board_object = self._board_object
        board = self._board_object.get_board()
        key = space

        if key == 'A' or key == 'B':  # ends in their points pile
            board_object.print_board()
            if board['A'] == 24 and board['B'] == 24:
                print("Score: A =", board['A'], "B =", board["B"])
                print("IT'S A TIE!")
                self._game_over = True
                return True
            elif board['A'] + board['B'] == 48:
                self._winner = self.set_winner()
                print("Score: A =", board['A'], "B =", board["B"])
                print("PLAYER ", self._winner, " WINS!")
                self._game_over = True
                return True
            else:
                print("You landed in your own points pile! You go again!")
                self._first_move = True
                return True
        else:
            return False

    def next_turn(self, player, space):
        """Returns true if the current turn is over, and it's now the other player's turn. Returns false, otherwise"""
        board_object = self._board_object
        board = self._board_object.get_board()
        key = space

        if board[key] == 1 and key != "A" and key != 'B':  # num_marbles is zero and they ended in a space with zero marbles
            board_object.print_board()
            if player == "A":
                print("You landed in an empty space. Player B's turn!")
                self._first_move = True
                self._a_turn = False
            else:
                print("You landed in an empty space. Player A's turn!")
                self._first_move = True
                self._a_turn = True
            return True
        else:
            return False

    def wrong_player(self, player):
        """Returns True if wrong player is taking a turn, and False if it's the correct player"""
        if self._a_turn and player == 'A':  # this section makes sure the correct player is taking a turn
            return False
        elif self._a_turn and player == "B":
            print("It is player A's turn!")
            return True
        elif self._a_turn == False and player == 'B':
            return False
        else:
            print("It is player B's turn!")
            return True

    def check_move(self, player, space):
        """Checks to make sure player is starting move on their side of the board"""
        space_num = int(space)
        if player == 'A':
            if space_num <= 6:
                return True
            else:
                return False
        if player == 'B':
            if space_num >= 7:
                return True
            else:
                return False

    def set_winner(self):
        """Sets the winner of the game"""
        board = self._board_object.get_board()

        if board['A'] > board['B']:
            return "A"
        elif board['A'] < board['B']:
            return "B"

    def is_game_over(self):
        """Returns True if this game of mancala is over"""
        if self._game_over == True:
            print("Please start a new game of Mancala.")
            return True
        else:
            return False
"""
game1 = Mancala("Emily", "Danny")
game1.move('A', '3')
game1.move('A', '2')
game1.move('B', '11')
game1.move("A", "1")
game1.move("B", "12")
game1.move("B", "10")
game1.move("B", "12")
game1.move("B", "7")
game1.move("A", "6")
game1.move("A", "3")
game1.move("A", "4")
game1.move("A", "2")
game1.move("A", "1")
game1.move("A", "6")
game1.move("A", "4")
game1.move("A", "3")
game1.move("A", "1")
game1.move("B", "12")
game1.move("B", "8")
game1.move("A", "2")
game1.move("B", "9")
game1.move("A", "6")
game1.move("A", "3")
game1.move("A", "5")
game1.move("B", "8")
game1.move("B", "10")
game1.move("A", "5")
game1.move("B", "11")
game1.move("B", "12")
game1.move("A", "1")
game1.move("A", "6")
game1.move("A", "5")
game1.move("A", "6")
game1.move("A", "4")
game1.move("B", "8")
game1.move("A", "2")
game1.move("B", "10")
game1.move("B", "12")
game1.move("B", "4")
game1.move("A", "6")
game1.move("B", "8")
game1.move("A", "3")
game1.move("B", "10")
game1.move("B", "12")
game1.move("B", "4")
game1.move("A", "5")
game1.move("B", "6")
game1.move("A", "7")
game1.move("B", "8")
game1.move("A", "9")
game1.move("B", "10")
game1.move("A", "11")
game1.move("B", "12")
game1.move("B", "3")
"""
