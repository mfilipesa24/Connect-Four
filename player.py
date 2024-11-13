# Class that represents a player in a Connect Four game.
class Player:

  # Instantiates a player object.
  def __init__(self, id_count):
    self.id = id_count
    self.symbol = input("Player " + str(self.id) + " choose your symbol.\n")
    if self.symbol == "exit":
      raise TypeError("Program stopped.")
      # For convenience purposes, the moves of each of the players will be stored separately.
    self.moves = []

  # Returns the id of a player instance.
  def get_player_id(self):
    return self.id

  # Returns the symbol of a player instance.
  def get_player_symbol(self):
    return self.symbol

  # Returns a list containing the history of a player's moves, for a particular Board instance.
  def get_player_moves(self):
    return self.moves

  # Adds a valid move to the list containing the history of a player's moves, for a particular Board instance.
  def add_valid_move(self, valid_move):
    valid_coordinates = "(" + valid_move[1] + ", " + valid_move[4] + ")"
    self.moves.append(valid_coordinates)
