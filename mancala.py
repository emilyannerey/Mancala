class Mancala:
    """Defines an instance of the game mancala"""

    def __init__(self):
        self._board = {'1': 4,  '2': 4,  '3': 4, '4': 4, '5': 4, '6': 4, 'A': 0,
                       '7': 4, '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, 'B': 0}
        self._playerA_route = ['1', '2', '3', '4', '5', '6', 'A', '7', '8', '9', '10', '11', '12']
        self._playerB_route = ['7', '8', '9', '10', '11', '12', 'B', '1', '2', '3', '4', '5', '6']
        self._a_turn = True  # start's off with player A's turn, used to make sure the turns are correct according to the rules
        self._first_move = True    # makes sure a player's starting move is on their own side
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
        print("the spaces. To make a move, use the move() function with the player and space as string arguments.")
        print("For example: game1.move('A', '1').")


    def move(self, player, space):
        """player chooses which space they will pick up marbles from"""
        if self.is_empty(space):
            return
        if self._a_turn and player == 'A':              # this section makes sure the correct player is taking a turn
            pass
        elif self._a_turn and player == "B":
            print("It is player A's turn!")
            return
        elif self._a_turn == False and player == 'B':
            pass
        else:
            print("It is player B's turn!")
            return

        if self.check_side(player):                  # check to see if side is empty
            pass
        elif self._first_move:
            if self.check_move(player, space):       # check to see if player makes a legal move
                pass
            else:
                print("Please pick a starting space on your side of the board!")
                return

        if player == 'A':
            route = self._playerA_route
        else:
            route = self._playerB_route

        num_marbles = self._board[space]     # how many spaces the player can move
        self._board[space] = 0               # pick up all the marbles in initial space, so it's set to zero
        route_position = route.index(space)   # index of route list
        key = space

        while num_marbles != 0:
            if route_position == 12:
                route_position -= 12
                key = route[route_position]
                self._board[key] += 1
                num_marbles -= 1
            else:
                route_position += 1        # move forward one on route list
                key = route[route_position]
                self._board[key] += 1
                num_marbles -= 1

        if self._board[key] == 1 and key != "A" and key != 'B':  # num_marbles is zero and they ended in a space with zero marbles
            if player == "A":
                self.print_board()
                print("You landed in an empty space. Player B's turn!")
                self._first_move = True
                self._a_turn = False
                return
            else:
                self.print_board()
                print("You landed in an empty space. Player A's turn!")
                self._first_move = True
                self._a_turn = True
                return

        if key == 'A' or key == 'B':  # ends in their points pile
            if self._board['A'] == 24 and self._board['B'] == 24:
                self.print_board()
                print("Score: A =", self._board['A'], "B =", self._board["B"])
                print("IT'S A TIE!")
                return
            elif self._board['A'] + self._board['B'] == 48:
                self.print_board()
                self.game_over()
                print("Score: A =", self._board['A'], "B =", self._board["B"])
                print("PLAYER", self._winner, " WINS!")
                return
            elif player == "A":
                self.print_board()
                print("You landed in your own points pile! You go again!")
                self._first_move = True
                return
            else:
                self.print_board()
                print("You landed in your own points pile! You go again!")
                self._first_move = True
                return

        if 0 < int(key) < 13 and self._board[key] > 1:  # they landed in a pile that still has marbles
            if player == "A":
                self._first_move = False
                self.move("A", key)
            else:
                self._first_move = False
                self.move("B", key)


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


    def check_side(self, player):
        """Checks to see if all spaces on player's side are empty, if so, the player is allowed to
        move from the other side"""
        if player == 'A':
            if self._board['1'] == 0 and self._board['2'] == 0 and self._board['3'] == 0 and self._board['4'] == 0 and self._board['5'] == 0 and self._board['6'] == 0:
                return True
            else:
                return False
        if player == 'B':
            if self._board['7'] == 0 and self._board['8'] == 0 and self._board['9'] == 0 and self._board['10'] == 0 and self._board['11'] == 0 and self._board['12'] == 0:
                return True
            else:
                return False

    def print_board(self):
        """Prints out the new board after each move"""
        for key in self._board:
            print(key, ":", self._board[key])
        return

    def game_over(self):
        """Sets the winner of the game"""
        if self._board['A'] > self._board['B']:
            self._winner = "A"
        elif self._board['A'] < self._board['B']:
            self._winner = "B"

    def is_empty(self, space):
        """Returns true if the space chosen is empty and prompts user to pick another space"""
        if self._board[space] == 0:
            print("This space is empty! Please pick a space with marbles in it. ")
            return True
        else:
            return False