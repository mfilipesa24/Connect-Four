from board import Board as br
from player import Player as pl

# Registers players in a Connect Four game.
def register_players():
  players = []
  id_count = 1
  while id_count < 3:
    players.append(pl(id_count))
    id_count += 1
  return players

# Obtains the current Player instance, bearing "current_player_id" value for "id" attribute.
def get_current_player(current_player_id):
  return players[current_player_id - 1]

# Allows to change the player, at the start of a new game turn.
def change_player(current_player_id):
  if current_player_id == 1:
    return 2
  else:
    return 1

# Allows for players to execute a valid play, registering in in the board object.
def play(board):
  print("Game start.\n")
  is_valid_move = False
  alignment = False
  tie = False
  # Contains information about the current player holding the turn. By default, the first player holding the first turn will be player 1.
  current_player_id = 1
  while not alignment and not tie: 
    while not is_valid_move:
      move = input("Player " + str(current_player_id) + " make your move.\n")
      if move == "exit":
        raise TypeError("Program stopped.")
      # While the player does not provide a valid mode, the user will be displayed a notification saying he still has not provided a valid move.
      is_valid_move = br.is_valid_play(board, move)
      
    # Only and once if it has been successfully verified that a player supplied a valid move, his play is registered on the board.
    valid_move = br.get_valid_move_coordinates(board, move)
    current_player = get_current_player(current_player_id)
    current_player_symbol = pl.get_player_symbol(current_player)
    br.register_move(board, valid_move, current_player_symbol)
        
    # The move is also added in the applicable list containing the history all moves from the current player, for that Board instance.
    pl.add_valid_move(current_player, valid_move)
    print(board)
    current_player_moves = pl.get_player_moves(current_player)
      
    # Check if a four coordinate alignment has occured, in any row, column or diagonal where the current player has made a valid move.
    diagonal_check = br.check_diagonals(board, current_player_moves, current_player_symbol)
    row_check = br.check_rows(board, current_player_moves, current_player_symbol)
    column_check = br.check_columns(board, current_player_moves, current_player_symbol)
    
    alignment = diagonal_check or row_check or column_check
    
    # If an alignment has been detected, the game ends and the player holding the turn wins it.
    if alignment:
      print("Player " + str(current_player_id) + " is the winner.")
      break
          
    # If no alignment was found, verify if the game is still untied. If a tie has been detected, the game ends.
    tie = br.check_ties(board)
    if tie:
      print("Game is a tie.")
      break
        
    # Finally, when the player's move has been registered in the board, it's the player's opponent turn to play.
    current_player_id = change_player(current_player_id)
    is_valid_move = False

# Generates board to start the game.
print("""\n
         * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
         *     _ _ _ _ _       _ _ _ _ _        _ _ _ _ _        _ _ _ _ _        _ _ _ _ _       _ _ _ _ _     _ _ _ _ _ _  *  
         *    |               |         |      |         |      |         |      |               |                   |       *
         *    |               |         |      |         |      |         |      |               |                   |       *
         *    |               |         |      |         |      |         |      |_ _ _ _        |                   |       *
         *    |               |         |      |         |      |         |      |               |                   |       *
         *    |               |         |      |         |      |         |      |               |                   |       *
         *    |_ _ _ _ _      |_ _ _ _ _|      |         |      |         |      |_ _ _ _ _      |_ _ _ _ _          |       *      
         *                             _ _ _ _      _ _ _ _ _                         _ _ _ _                                *
         *                            |            |         |      |         |      |       |                               *
         *                            |            |         |      |         |      |       |                               *
         *                            |_ _ _       |         |      |         |      |_ _ _ _|                               *
         *                            |            |         |      |         |      |     |                                 *
         *                            |            |         |      |         |      |     |                                 *
         *                            |            |_ _ _ _ _|      |_ _ _ _ _|      |     |_ _                              *
         *                                                                                                                   *
         * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
      """)

print("----------------------------------------------------------Game Rules:--------------------------------------------------------\n")
print("Align four symbols consecutively, before your opponent does, to win the game.")
print('Moves must be written with a c-column number, where 1 < c < 7. For example:"3".\n')
print("Should a four-symbol alignment no longer becomes possible, the game is a tie.")
print('Program will terminate if either of the players write "exit".')
print("------------------------------------------------------------:------------------------------------------------------------------\n")
board = br()
print(board)

#  [ [  [][][][] ]
#    [  [][][][] ]
#    [  [][][][] ]  ]

# Creates the players 1 and 2 within a Connect Four game, with their symbols, respectively.
players = register_players()

# Established that 1st player to play is player 1. Player 1 makes his move. Then, turn goes to player 2, who makes his move.
play(board)
