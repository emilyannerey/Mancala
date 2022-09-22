class Player:
    """Creates a player object for the game Mancala. Initialized in the Mancala class init method."""

    def __init__(self, A_or_B, name):
        self._player = A_or_B
        self._player_name = name
        self._points = 0
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

    def get_points(self):
        """Returns the number of points player currently has"""
        return self._points

    def update_points(self):
        """Adds 1 to player points when player scores"""
        self._points += 1

