class Board:
    """Creates a board object for the game Mancala. Initialized in the Mancala class init method."""

    def __init__(self, player1, player2):
        self._player1_object = player1
        self._player2_object = player2
        self._a_turn = True
        self._first_move = True
        self._board = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, 'A': 0,
                       '7': 4, '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, 'B': 0}

    def get_board(self):
        """Returns dictionary that represent the game board"""
        return self._board

    def get_a_turn(self):
        """returns a_turn bool"""
        return self._a_turn

    def update_a_turn(self, new_bool):
        """Updates a_turn to new_bool"""
        self._a_turn = new_bool

    def get_first_move(self):
        """Returns first_move data member"""
        return self._first_move

    def update_first_move(self, new_bool):
        """Updates first_move to new_bool"""
        self._first_move = new_bool

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
            if self._board['1'] == 0 and self._board['2'] == 0 and self._board['3'] == 0 and self._board['4'] == 0 and \
                    self._board['5'] == 0 and self._board['6'] == 0:
                return True
            else:
                return False
        if player == 'B':
            if self._board['7'] == 0 and self._board['8'] == 0 and self._board['9'] == 0 and self._board['10'] == 0 and \
                    self._board['11'] == 0 and self._board['12'] == 0:
                return True
            else:
                return False

    def print_board(self):
        """Prints out the new board after each move"""
        for key in self._board:
            print(key, ":", self._board[key])
        return

    def is_empty(self, space):
        """Returns true if the space chosen is empty and prompts user to pick another space"""
        if self._board[space] == 0:
            print("This space is empty! Please pick a space with marbles in it. ")
            return True
        else:
            return False

    def game_over(self):
        """Sets the winner of the game"""
        if self._board['A'] > self._board['B']:
            return "A"
        elif self._board['A'] < self._board['B']:
            return "B"

    def compare_goals(self):
        """Returns true if player A has more marbles in their goal than player B and false otherwise"""
        if self._board['A'] > self._board['B']:
            return True
        else:
            return False