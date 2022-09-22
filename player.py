class Player:
    """Creates a player object for the game Mancala. Initialized in the Mancala class init method."""

    def __init__(self, A_or_B, name):
        self._player = A_or_B
        self._player_name = name
        self._board_object = None
        if self._player == "A":
            self._player_route = ['1', '2', '3', '4', '5', '6', 'A', '7', '8', '9', '10', '11', '12']
        else:
            self._player_route = ['7', '8', '9', '10', '11', '12', 'B', '1', '2', '3', '4', '5', '6']

    def get_player(self):
        """Returns "A" or "B" """
        return self._player

    def get_player_name(self):
        """Returns player's name"""
        return self._player_name

    def update_board_object(self, board_object):
        """Sets board object data member to board object given as an argument"""
        self._board_object = board_object

    def wrong_player(self):
        """Returns True if wrong player is taking a turn, and False if it's the correct player"""
        if self._board_object.get_a_turn() and self._player == 'A':  # this section makes sure the correct player is taking a turn
            return False
        elif self._board_object.get_a_turn() and self._player == "B":
            print("It is player A's turn!")
            return True
        elif self._board_object.get_a_turn() == False and self._player == 'B':
            return False
        else:
            print("It is player B's turn!")
            return True

    def next_turn(self, space):
        """Returns true if the current turn is over, and it's now the other player's turn. Returns false, otherwise"""
        board_object = self._board_object
        board = self._board_object.get_board()
        key = space

        if board[key] == 1 and key != "A" and key != 'B':  # num_marbles is zero and they ended in a space with zero marbles
            board_object.print_board()
            if self._player == "A":
                print("You landed in an empty space. Player B's turn!")
                board_object.update_first_move(True)
                board_object.update_a_turn(False)
            else:
                print("You landed in an empty space. Player A's turn!")
                board_object.update_first_move(True)
                board_object.update_a_turn(True)
            return True
        else:
            return False

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
                return True
            elif board['A'] + board['B'] == 48:
                print("Score: A =", board['A'], "B =", board["B"])
                if board_object.compare_goals():
                    print("PLAYER A WINS!")
                    return True
                else:
                    print("PLAYER B WINS!")
                    return True
            else:
                print("You landed in your own points pile! You go again!")
                board_object.update_first_move(True)
                return True
        else:
            return False

    def move(self, space):
        """player chooses which space they will pick up marbles from"""
        board = self._board_object.get_board()

        if self._board_object.is_empty(space):  # makes sure player chooses a space with marbles
            return

        if self.wrong_player():
            return

        if self._board_object.check_side(self._player):  # check to see if side is empty
            pass
        elif self._board_object.get_first_move():
            if self._board_object.check_move(self._player, space):  # check to see if player makes a legal move
                pass
            else:
                print("Please pick a starting space on your side of the board!")
                return

        num_marbles = board[space]  # how many spaces the player can move
        board[space] = 0  # pick up all the marbles in initial space, so it's set to zero
        route_position = self._player_route.index(space)  # index of route list
        key = space

        while num_marbles != 0:
            if route_position == 12:
                route_position -= 12
                key = self._player_route[route_position]
                board[key] += 1
                num_marbles -= 1
            else:
                route_position += 1  # move forward one on route list
                key = self._player_route[route_position]
                board[key] += 1
                num_marbles -= 1

        if self.next_turn(key):
            return

        if self.ends_in_goal(key):
            return

        self._board_object.update_first_move(False)
        self.move(key)