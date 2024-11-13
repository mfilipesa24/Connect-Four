# Class that represents a board in a Connect Four game.
class Board:
  # class attributes
  rows = 6 
  columns = 7
  
  # type 1 diagonals: from the leftmost coordinate to the rightmost coordinate in the board, for each new coordinate,
  # both the row value and the column value will increase;
  type_1_diagonal_starting_coordinates = ["(1, 4)", "(3, 1)", "(1, 3)", "(2, 1)", "(1, 2)", "(1, 1)"]

  # type 2 diagonals: from the leftmost coordinate to the rightmost coordinate in the board, for each new coordinate,
  # the row value will decrease and the column value will increase;
  type_2_diagonal_starting_coordinates = ["(4, 1)", "(6, 4)", "(5, 1)", "(6, 3)", "(6, 1)", "(6, 2)"]
  
  # Initializes a Board object.
  def __init__(self):
  # The game board consists on a matrix of rows and columns.
  # We treat the game matrix as a list containing row sublists, wich each row sublist contaning column sublists.
    game_matrix = []
    for i in range(Board.rows):
      current_row = []
      for j in range(Board.columns):
        current_row.append([])
      game_matrix.append(current_row)
  # The information for that Board instance is stored in a "view" instance attribute.
    self.view = game_matrix

  # Due to the nature of a "Connect Four" game, we need to keep track of the already filled columns (that is, all the
  # columns that no longer have any empty coordinate left).
    self.filled_columns = []
    
  # Finally, we need to keep track of the rows, columns and diagonals where there can no longer be a winner (tie).
    self.tied_rows = []  # max 6 length elements (6 rows to check)
    self.tied_columns = []  # max 7 length elements (7 columns to check)
    self.tied_diagonals = []  # max 12 length elements (12 diagonals to check: 6 for type 1), and 6 for type 2) diagonals)

  # Verifies if the player does a valid move. Only valid moves are accepted in the game.
  # For a move to be valid, the user must type a c-column value where 0 < c < 8, and the column must still have empty rows.
  # If those conditions are met, the function returns True. Otherwise, False is returned.
  def is_valid_play(self, move):
    play_valid = False
    error_message = "Invalid move. "
    move_args = len(move)
    # The game will only move forward if the user supplies a c-column value, where 0 c < 8.
    if move_args != 1 or (move_args == 1 and move[0] == " "):
      print(error_message+ "\nMake sure you only supply one c-column value, where 0 < c < 8.\n")
      return play_valid

    # 1) Verify if the given c-column input is a digit. If so, convert it to a number.
    column_value = move[0]
    if not column_value.isdigit():
      print(error_message+ '\n The c-column value must be a number between 1 and 7 (booth included). For i.e.:"3".')
      return play_valid
  
    # 2) Verify if "c" is in the required ranges.
    column_value = int(column_value)
    if (column_value < 1 or column_value > 7):
      print(error_message + "Make sure the the column number between 1 and 7.")
      return play_valid
  
    # 3) Verify if the given c-column is already in the list of filled columns. If that is the case, it means the given column
    # is already full and the player must chose a different column value.
    if column_value in self.filled_columns:
      print(error_message + "The given column is already full! Supply a new column value.")
      return play_valid
    
    # Each of the seven c-columns in the board will contain six coordinates, top to bottom. Considering our game implementation
    # has row values increasing in a direction from top to bottom, then row values will be decreasing on the opposite direction.
    # We will be using this second type of design, since, in a "Connect Four" game, the columns must be filled upwards.
    for row_value in range(6, 0, -1):
      if row_value == 1:
      # When an empty coordinate was found for the given column, at the top (row_value = 1), it means all the remaining column
      # coordinates have already been filled. Thus, accepting the player move means that there won't be any empty coordinates
      # left for the given column. In that scenario, the designated column needs to be appended to the list of filled columns.
        if self.view[row_value - 1][column_value - 1] == []:
          play_valid = True
          self.filled_columns.append(column_value)
      elif self.view[row_value - 1][column_value - 1] == []:
        play_valid = True
        break
      else:
        continue   
    return play_valid
  
  # Function that returns a string representing the coordinates of a valid player move, in the form of "(r, c)",
  # where "r" is the row value and "c", the column value, respectively.
  def get_valid_move_coordinates(self, valid_move):
    # First, get the c-column value.
    column_value = int(valid_move)
    # Then, traversing c-column from the bottom up, obtain its first available empty coordinate, with its applicable r-row value. 
    for row_value in range(6, 0, -1):
      if self.view[row_value - 1][column_value - 1] == []:
        move_coordinates = "(" + str(row_value) + "," + " " + valid_move + ")"
        break
        # Since "move_coordinates" is a string, the string representation of column_value ("valid_move") will be used.
      else:
        continue
    return move_coordinates
  
  # Verifies if the current player holding the turn has four symbols consecutively aligned in a row. If such outcome
  # takes place, True is returned. Otherwise, the function returns False.
  def check_rows(self, current_player_moves, current_player_symbol):
    alignment_detected = False
    for valid_move in current_player_moves:
      base_coordinate = valid_move
    # Verify 4 symbol alignment in that row
      current_row = self.get_row_coordinates(base_coordinate)
      alignment_detected = self.check_four_symbol_alignment(current_player_symbol, current_row, base_coordinate)
      if alignment_detected:
        break
    return alignment_detected

  # Function that checks if a tie has been obtained on the game board. 
  # If a tie has been found, the function will return True. Otherwise, it will return False.
  def check_ties(self):
    
    # First, check all rows. "i" is used to represent the row index.
    for i in range(1, 7):
      if i in self.tied_rows:
        continue
      else:
        # If the row in not on the tied row list, get all the coordinates for that row.
        # For convenience purposes, the leftmost coordinate of each row (i, 1) will be used as
        # base coordinate to extract all the current row's coordinates.
        base_coordinate = "(" + str(i) + "," + " " + "1)"
        all_row_coordinates = self.get_row_coordinates(base_coordinate)
        if self.lookup_list_is_tied(all_row_coordinates):
          self.tied_rows.append(i) 
    
    # Then, check all columns. "j" is used to represent the column index.  
    for j in range(1, 8):
      if j in self.tied_columns:
        continue
      else:
        # If the column in not on the tied row list, get all the coordinates for that column.
        # For convenience purposes, the upmost coordinate of each row (1, j) will be used as
        # base coordinate to extract all the current column's coordinates.
        base_coordinate = "(1," + " " + str(j) + ")"
        all_column_coordinates = self.get_column_coordinates(base_coordinate)
        if self.lookup_list_is_tied(all_column_coordinates):
          self.tied_columns.append(j) 
    
    # Finally, check all diagonals. 
    # For convenience, we add all diagonal types start coordinates into one single list.
    all_start_coordinates = self.get_all_diagonals_starting_coordinates()
    for base_coordinate in all_start_coordinates:
      if base_coordinate in self.tied_diagonals:
        continue
      else:
        # If the starting coordinate of the applicable diagonal is not on the tied diagonals
        # list, obtain all that diagonal's coordinates.
        all_diagonal_coordinates = self.get_diagonal_coordinates(base_coordinate)
        if self.lookup_list_is_tied(all_diagonal_coordinates):
          self.tied_diagonals.append(base_coordinate)
    
    return (len(self.tied_rows) == 6 and len(self.tied_columns) == 7 and len(self.tied_diagonals) == 12)
  
  # Function that returns a list of all the starting coordinates from every diagonal in the game board, first, with the
  # coordinates corresponding to type 1 diagonals, then, with those corresponding to type 2 diagoanals, as per the way
  # they appear in Board attributes "type_1_diagonal_starting_coordinates" and "type_1_diagonal_starting_coordinates",
  # respectively. 
  def get_all_diagonals_starting_coordinates(self):
    all_diagonals_starting_coordinates = []
    for start_index in range(len(Board.type_1_diagonal_starting_coordinates)):
      all_diagonals_starting_coordinates.append(Board.type_1_diagonal_starting_coordinates[start_index])
    for start_index in range(len(Board.type_2_diagonal_starting_coordinates)):
      all_diagonals_starting_coordinates.append(Board.type_2_diagonal_starting_coordinates[start_index])
    return all_diagonals_starting_coordinates
    
  # Function that implements the tie mechanism of check_ties() function, that is, it verifies if in any given list of lookup
  # coordinates (be it row, column and diagonal of the current game board), any tie has been detected. When a tie is detected
  # in the applicable lookup list type, that list is added to the respective tied list type. The function will only check ties 
  # on rows, columns or diagonals that still have not been added to the applicable tied list type.The game will only proceed if
  # no tie has been found. 
  def lookup_list_is_tied(self, lookup_coordinates):
    lookup_list_is_tied = False

    # First, check if there are at least two different symbols in the applicable group of lookup coordinates. Where there are less
    # than two symbols found, it means that a tie can not take place in the given list of coordinates.
    two_symbols_found = self.two_symbols_found(lookup_coordinates)
    
    # Where at least two symbols have been found in the applicable type of lookup coordinates, check for any potential ties in
    # that given list type. Since we want to check each group of four adjacent coordinates to the base coordinate, every time
    # a group of coordinates can not constitute a potential group of four alignable coordinates, each of those coordinates are
    # removed from the list of traversable coordinates.
    if two_symbols_found:
      # By hypothesis, there can be a tie in the lookup group of coordinates every time where exactly two symbols are found.
      lookup_list_is_tied = True
      for base_coordinate in lookup_coordinates:    
        current_row = int(base_coordinate[1])
        current_column = int(base_coordinate[4])
      
      # In case a player symbol is found on the base coordinate, check all the adjacent coordinates to that coordinate until - and if -
      # a group of four consecutive coordinates, with the appicable player symbol, can still be obtained for subsequent game turns. All 
      # potential groups of four consecutive coordinates where a symbol alignment for each of the players may still take place will be
      # checked, combining all applicable directions from the given coordinate's lookup list(1st direction, stemming on a right to
      # leftwise motion from the base coordinate; 2nd direction, stemming on a left to rightwise motion from the base coordinate).
        if self.view[current_row - 1][current_column - 1] != []:
          applicable_player_symbol = self.view[current_row - 1][current_column - 1] 
          alignable_coordinates = 1
          current_base_index = lookup_coordinates.index(base_coordinate)
        # A counter will keep track of all potential four consecutive coordinates that can still be obtained for subsequent turns, for
        # each base coordinate that bears an applicable player symbol. If, after traversing the given list of lookup coordinates, that
        # counter never reached four, it means neither of the players can no longer obtain a four symbol alignment, within the given
        # list of lookup coordinates. In such scneario, a tie has been obtained for the applicable list type of lookup coordinates
        # (which can be a row, a column or a diagonal in the game board).
        else:
          # If a player symbol is not found, continue to iterate in the lookup coordinates until it is found.
          continue
      
        # First, check all existing adjacent coordinates to the base coordinate, in the 1st direction (-).
        while current_base_index != -1 and alignable_coordinates != 4:
          if current_base_index - 1 == -1:
            current_base_index = -1
          else:
            current_base_index-= 1
            if self.view[int(lookup_coordinates[current_base_index][1]) - 1][int(lookup_coordinates[current_base_index][4]) - 1] \
             == applicable_player_symbol\
              or self.view[int(lookup_coordinates[current_base_index][1]) - 1][int(lookup_coordinates[current_base_index][4]) - 1] \
                == []:
              alignable_coordinates+= 1
            else:
              # When a symbol that is not the applicable player symbol is detected, the 1st direction "while" cycle stops.
              current_base_index = -1
              
        # Then, check all existing adjacent coordinates to the base coordinate, in the 2nd direction (+).
        current_base_index = lookup_coordinates.index(base_coordinate)
        while current_base_index != len(lookup_coordinates) and alignable_coordinates != 4:
          if current_base_index + 1 == len(lookup_coordinates):
            current_base_index = len(lookup_coordinates)
          else:
            current_base_index+= 1
            if self.view[int(lookup_coordinates[current_base_index][1]) - 1][int(lookup_coordinates[current_base_index][4]) - 1] \
            == applicable_player_symbol\
            or self.view[int(lookup_coordinates[current_base_index][1]) - 1][int(lookup_coordinates[current_base_index][4]) - 1] \
            == []:
              alignable_coordinates+= 1
            else:
              #  When a symbol that is not the applicable player symbol is detected, the 2nd direction "while" cycle stops.
              current_base_index = len(lookup_coordinates)
        
          # When at least four alignable coordinates are found for one player, it means that lookup group of coordinates is not tied.
        if alignable_coordinates == 4:
          lookup_list_is_tied = False
          break
    return lookup_list_is_tied
    
  # Function that verifies if at least two different player symbols are present in a given list of lookup coordinates. When that
  # outcome takes place, the function returns True. Otherwise, False is returned.
  def two_symbols_found(self, lookup_coordinates):
    two_symbols_found = False
    symbols_detected = []
    for base_coordinate in lookup_coordinates:
      current_row = int(base_coordinate[1])
      current_column = int(base_coordinate[4])
      # Check if any of the two players's respective symbols are present in the current base coordinate. If yes, in case that
      # symbol is still not present in the list of detected symbols, add it.
      if self.view[current_row - 1][current_column - 1] != []:
        applicable_player_symbol = self.view[current_row - 1][current_column - 1]
        if applicable_player_symbol not in symbols_detected:
          symbols_detected.append(applicable_player_symbol)
          # If two symbols have been detected, a tie can no longer be ruled out in the applicable list of lookup coordinates.
          if len(symbols_detected) == 2:
            two_symbols_found = True
            break
      else:
        continue
    # Should the "for" cycle end with less than two symbols detected, a tie is excluded within the list of lookup coordinates.  
    return two_symbols_found
      
  # Function that returns all the row coordinates in a row from the current player.
  def get_row_coordinates(self, base_coordinate):
    all_row_coordinates = []
    for i in range(7):
      current_coordinate = "(" + base_coordinate[1] + "," + " " + str(i + 1) + ")"
      all_row_coordinates.append(current_coordinate)
    return all_row_coordinates

  # Verifies if the current player holding the turn has four symbols consecutively aligned in a column. If such outcome
  # takes place, True is returned. Otherwise, the function returns False.
  def check_columns(self, current_player_moves, current_player_symbol):
    alignment_detected = False
    for valid_move in current_player_moves:
      base_coordinate = valid_move
      # Verify 4 symbol alignment in that column
      current_column = self.get_column_coordinates(base_coordinate)
      alignment_detected = self.check_four_symbol_alignment(current_player_symbol, current_column, base_coordinate)
      if alignment_detected:
        break
    return alignment_detected

  # Function that returns all the column coordinates in a column from the current player.
  def get_column_coordinates(self, base_coordinate):
    all_column_coordinates = []
    for i in range(6):
      current_coordinate = "(" + str(i + 1) + "," + " " + base_coordinate[4] + ")"
      all_column_coordinates.append(current_coordinate)
    return all_column_coordinates

  # Function that returns the diagonal type for a given diagonal, spanning from the leftmost starting coordinate.
  # - type 1 diagonal (integer 1): from the rightmost coordinate to the leftmost coordinate, for each new coordinate,
  #                                   both the row value and the column value will increase;
  # - type 2 diagonal (integer 2): from the rightmost coordinate to the leftmost coordinate, for each new coordinate,
  #                                   the row value will decrease and the column value will increase.
  def get_diagonal_type(self, leftmost_coordinate):
    if leftmost_coordinate in Board.type_1_diagonal_starting_coordinates:
      return 1
    else:
      return 2

  # Function that returns the leftmost coordinate in the diagonal with, at least, one coordinate taken by the current player.
  def get_all_leftmost_coordinates(self, valid_move):
    all_leftmost_coordinates = []
    current_row = int(valid_move[1])
    current_column = int(valid_move[4])
    # Verify if the diagonal candidate is contained in a type 1 diagonal.
    while current_row > 0 and current_column > 0:
      last_coordinate_found = ("(" + str(current_row) + "," + " " + str(current_column) + ")")
      if last_coordinate_found in Board.type_1_diagonal_starting_coordinates:
        all_leftmost_coordinates.append(last_coordinate_found)
      current_row -= 1
      current_column -= 1
    # Verify if the diagonal candidate is contained in a type 2 diagonal.
    current_row = int(valid_move[1])
    current_column = int(valid_move[4])
    while current_row < 7 and current_column > 0:
      last_coordinate_found = ("(" + str(current_row) + "," + " " + str(current_column) + ")")
      if last_coordinate_found in Board.type_2_diagonal_starting_coordinates:
        all_leftmost_coordinates.append(last_coordinate_found)
      current_row += 1
      current_column -= 1
    return all_leftmost_coordinates

  # Function that returns a list with all the diagonal coordinates, knowing that diagonal's type (1 or 2) and its leftmost starting coordinate.
  def get_diagonal_coordinates(self, leftmost_coordinate):
    diagonal_coordinates = []
    diagonal_coordinates.append(leftmost_coordinate)
    current_row = int(leftmost_coordinate[1])
    current_column = int(leftmost_coordinate[4])
    # Get the diagonal's type.
    diagonal_type = self.get_diagonal_type(leftmost_coordinate)
    # For a type 1 diagonal.
    if diagonal_type == 1:
      while current_row < 6 and current_column < 7:
        current_row += 1
        current_column += 1
        # Obtain the current diagonal's coordinate.
        current_coordinate = ("(" + str(current_row) + "," + " " + str(current_column) + ")")
        diagonal_coordinates.append(current_coordinate)
    # For a type 2 diagonal.
    else:
      while current_row > 1 and current_column < 7:
        current_row -= 1
        current_column += 1
        # Obtain the current diagonal's coordinate.
        current_coordinate = ("(" + str(current_row) + "," + " " + str(current_column) + ")")
        diagonal_coordinates.append(current_coordinate)
    return diagonal_coordinates
  
  # Function that returns the list with tied rows for a Board instance.
  def get_tied_rows(self):
    return self.tied_rows

  # Function that returns the list with tied columns for a Board instance.
  def get_tied_columns(self):
    return self.tied_columns

  #Function that returns the list with tied diagonals for a Board instance.
  def get_tied_diagonals(self):
    return self.tied_diagonals

  # Function that verifies if the current player holding the turn has four symbols consecutively aligned, given a certain
  # group of lookup coordinates (whether from a diagonal, row or column) and a given base coordinate in that group. In that
  # group of coordinates, both opposite directions - first and second directions - are checked. As for the base coordinate,
  # which has to be a valid move from the current player, we know it bears the symbol of the current player.
  # Only two directions are possible:
  #  - First direction: all the coordinates of the lookup coordinates to the leftside(-) of the base coordinate.
  #  - Second direction: all the coordinates of the lookup coordinates to the rightside(+) of the base coordinate.
  def check_four_symbol_alignment(self, current_player_symbol, lookup_coordinates, base_coordinate):
    aligned_coordinates = 1
    first_direction_current_index = lookup_coordinates.index(base_coordinate)
    second_direction_current_index = first_direction_current_index

    first_direction_current_row = int(lookup_coordinates[first_direction_current_index][1])
    first_direction_current_column = int(lookup_coordinates[first_direction_current_index][4])
    first_direction_checked = False

    second_direction_current_row = first_direction_current_row
    second_direction_current_column = first_direction_current_column
    second_direction_checked = first_direction_checked

    while not first_direction_checked or not second_direction_checked:
    # First, verify if the next-would-be coordinate of first/and second direction is within the lookup coordinates index bound.
    # If the next would-be coordinate is within bounds, everytime an opponent symbol is detected in the applicable direction,
    # alignment is no longer checked in that direction.

    # First direction check(-).
      if first_direction_current_index - 1 == -1 or\
          (self.view[int(lookup_coordinates[first_direction_current_index - 1][1]) - 1][int(lookup_coordinates[first_direction_current_index - 1][4]) - 1]
                != current_player_symbol):
        first_direction_checked = True
      else:
        first_direction_current_index = first_direction_current_index - 1
    
    # Second direction check(+).
      if second_direction_current_index + 1 == len(lookup_coordinates) or\
          (self.view[int(lookup_coordinates[second_direction_current_index + 1][1]) - 1][int(lookup_coordinates[second_direction_current_index + 1][4]) - 1]
                != current_player_symbol):
        second_direction_checked = True
      else:
        second_direction_current_index = second_direction_current_index + 1
        
      # Then, if the next-would-be-coordinate in first/and second direction is within bounds, get its row and column values.
      # Everytime the current player symbol is detected in the current coordinate, in each applicable direction, increment
      # "aligned coordinates" value. Should four aligned coordinates be found, immediately stop the "while" cycle.
      
      # First direction check.
      if not first_direction_checked:
        first_direction_current_row = int(lookup_coordinates[first_direction_current_index][1])
        first_direction_current_column = int(lookup_coordinates[first_direction_current_index][4])
        if (self.view[first_direction_current_row - 1][first_direction_current_column - 1] == current_player_symbol):
          aligned_coordinates += 1
          if aligned_coordinates == 4:
            first_direction_checked = True
            second_direction_checked = True

      # Second direction check.
      if not second_direction_checked:
        second_direction_current_row = int(lookup_coordinates[second_direction_current_index][1])
        second_direction_current_column = int(lookup_coordinates[second_direction_current_index][4])
        if (self.view[second_direction_current_row - 1][second_direction_current_column - 1] == current_player_symbol):
          aligned_coordinates += 1
          if aligned_coordinates == 4:
            first_direction_checked = True
            second_direction_checked = True

    return aligned_coordinates == 4

  # Verifies if the current player holding the turn has four symbols consecutively aligned in a diagonal. If such outcome
  # takes place, True is returned. Otherwise, the function returns False.
  def check_diagonals(self, current_player_moves, current_player_symbol):
    alignment_detected = False
    diagonal_start_coordinates_checked = []
    for valid_move in current_player_moves:
      leftmost_coordinates_list = self.get_all_leftmost_coordinates(valid_move)
    for lefmost_coordinate in leftmost_coordinates_list:
      all_diagonal_coordinates = self.get_diagonal_coordinates(lefmost_coordinate)
      diagonal_start_coordinates_checked.append(lefmost_coordinate)
      # Verify 4 symbol alignment in that diagonal
      base_coordinate = current_player_moves[len(current_player_moves)-1]
      alignment_detected = self.check_four_symbol_alignment(current_player_symbol, all_diagonal_coordinates, base_coordinate)
      if alignment_detected:
        break
    return alignment_detected

  # Visual representation of the Board object.
  def __repr__(self):
  # Generate the game matrix, containing rows.
    game_matrix = ""
    # Then, generate the rows of the board. In each row, generate the columns of the board.
    # ROW START
    for i in range(Board.rows):
      # COLUMN START
      if i != 0:
        game_matrix += "\n| "
      else:
        game_matrix += "| "
      # When a player has already used a particular coordinate, the coordinate location will display the applicable player symbol.
      for j in range(Board.columns):
        if self.view[i][j] != []:
          game_matrix += "["
          game_matrix += self.view[i][j]
        else:
          game_matrix += "[ "
        if j != Board.columns:
          game_matrix += "] "
        else:
          game_matrix += "|"
      game_matrix += "|"
        # Finally, show the current status of the board, containing updated information of all previous player's moves until present turn.
    return game_matrix

  # Registers a valid board play.
  def register_move(board, valid_move, current_player_symbol):
    row_input = int(valid_move[1])
    column_input = int(valid_move[4])
    board.view[row_input - 1][column_input - 1] = current_player_symbol
