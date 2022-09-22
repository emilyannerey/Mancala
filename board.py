class Board:
    """Creates a board object for the game Mancala. Initialized in the Mancala class init method."""

    def __init__(self):
        self._board = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, 'A': 0,
                       '7': 4, '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, 'B': 0}

    def get_board(self):
        """Returns dictionary that represent the game board"""
        return self._board

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
