def scoreCount(board):
    score = 0 
    for row in board:
      for column in row:
        if column != 0:
          if column > 2: #Enemy pieces
            score -= 1
          if column <= 2: #My pieces
            score += 1
    return score  

def count_right_diagonal_enemies(x, y, board, enemy_turn):
  if enemy_turn:
    enemy_piece =  board[x - 1][y - 1] <= 2
  else:
    enemy_piece =  board[x - 1][y - 1] > 2

  total_right_diag = 0
  while y < len(board[0]) - 1 and x > 0 and enemy_piece and board[x - 1][y - 1] != 0:
    total_right_diag += 1
    x -= 1
    y += 1
    if enemy_turn:
        enemy_piece =  board[x - 1][y - 1] <= 2
    else:
        enemy_piece =  board[x - 1][y - 1] > 2
  print("Right Enemies: ", total_right_diag)
  return total_right_diag

def count_left_diagonal_enemies(x, y, board, enemy_turn):

  if enemy_turn:
    enemy_piece =  board[x - 1][y - 1] <= 2
  else:
    enemy_piece =  board[x - 1][y - 1] > 2

  total_left_diag = 0
  while y > 0 and x > 0 and enemy_piece and board[x - 1][y - 1] != 0:
    
    total_left_diag += 1
    x -= 1
    y -= 1
    if enemy_turn:
        enemy_piece =  board[x - 1][y - 1] <= 2
    else:
        enemy_piece =  board[x - 1][y - 1] > 2

  print("Left Enemies: ", total_left_diag)
  return total_left_diag

def check_move_left_diagonal(x, y, board, enemy_turn):
  if enemy_turn:
    if board[x-1][y-1] >= 3:
        return None
  else:
    if 0 < board[x-1][y-1] <= 2:
        return None

  if board[x-1][y-1] == 0:
    return (x - 1, y - 1)

  #Can eat at least one enemy piece, but must check if can eat more enemy pieces
  #So, count the pieces which are in the diagonal
  #amount_left_diag_pieces, amount_right_diag_pieces = count_enemy_pieces_diagonal(x, y, board)

  amount_left_diag_pieces = count_left_diagonal_enemies(x, y, board, enemy_turn)
  
  #Check if my piece can be placed in a casilla after eating the enemy pieces
  if y - amount_left_diag_pieces > 0 and x - amount_left_diag_pieces > 0:
    legal_x = x - amount_left_diag_pieces - 1
    legal_y = y - amount_left_diag_pieces - 1
    
    return (legal_x, legal_y)
    #board[x - amount_left_diag_pieces - 1][y - amount_left_diag_pieces - 1] = 1 #Place the player one
  
  return None

def check_move_right_diagonal(x, y, board, enemy_turn):
  if enemy_turn:
    if board[x-1][y + 1] >= 3:
        return None
  else:
    if 0 < board[x-1][y + 1] <= 2:
        return None
    
  if board[x-1][y + 1] == 0:
    return (x - 1, y + 1)

  #Can eat at least one enemy piece, but must check if can eat more enemy pieces
  #So, count the pieces which are in the diagonal
  amount_right_diag_enemies = count_right_diagonal_enemies(x, y, board, enemy_turn)
  
  #Check if my piece can be placed in a casilla after eating the enemy pieces
  if y + amount_right_diag_enemies < len(board[0]) - 1 and x - amount_right_diag_enemies > 0:
    legal_x = x - amount_right_diag_enemies - 1
    legal_y = y + amount_right_diag_enemies + 1
    return (legal_x, legal_y)
    #board[x - amount_left_diag_pieces - 1][y - amount_left_diag_pieces - 1] = 1 #Place the player one
  return None

def count_legal_moves(moves):
   legal_moves = []
   for move in moves:
      if move != None:
         legal_moves.append()
   return len(legal_moves)

def get_enemy_board_pieces(board, enemy_turn):
  board_pieces = []
  for i in range(len(board)):
    for j in range(len(board[i])):
        if not enemy_turn:   
          if board[i][j] > 2:
            board_pieces.append(board[i][j])
        elif board[i][j] <= 2:
            board_pieces.append(board[i][j])
  return board_pieces

def get_piece_position(board, piece):
   for i in range(len(board)):
      for j in range(len(board[i])):
         if board[i][j] == piece:
            return (i, j)

def can_only_eat_one_piece(board, x, y):
  if board[x - 1][y - 1] != 0 or board[x-1][y + 1] != 0:
    return True
  return False

"""
  Checks if a piece with a given position can eat a enemy piece
  if can eat
    returns the position to eat
  else:
    returns a tuple of None
"""
def can_eat(board, x, y, enemy_turn):
  enemy_pieces = get_enemy_board_pieces(board, enemy_turn)
  for enemy_piece in enemy_pieces:
    if enemy_piece == board[x - 1][y - 1]:
      return [x - 1, y - 1]
    elif enemy_piece == board[x - 1][y + 1]:
      return [x - 1, y + 1]
  return (None, None)

def eat_piece(board, x_to_eat, y_to_eat):
  print(x_to_eat)
  board[x_to_eat][y_to_eat] = 0

def move_to_new_position(board, x_to_move, y_to_move):
  board[x_to_move][y_to_move] = 3 #Change this piece, it must be dinamically

def delete_current_position(board, x, y):
  board[x][y] = 0

def can_eat_both_pieces(board, x, y, enemy_turn):
  enemy_pieces = get_enemy_board_pieces(board, enemy_turn)
  if board[x - 1][y - 1] not in enemy_pieces:
      return False
  if board[x - 1][y + 1] not in enemy_pieces:
      return False
  return True

def check_diagonal_moves(x, y, board, enemy_turn):
  moves = []
  if x > 0: #Can move up
    if y == 0: # Check only right diagonal
      legal_move = check_move_right_diagonal(x, y, board, enemy_turn)
      if legal_move is not None: 
        moves.append(legal_move)
    elif y == len(board[0]) - 1: # Check only left diagonal
      legal_move = check_move_left_diagonal(x, y, board, enemy_turn)
      if legal_move is not None: 
        moves.append(legal_move)
    else: #check both diagonal sides
      left_legal_move = check_move_left_diagonal(x, y, board, enemy_turn)
      right_legal_move = check_move_right_diagonal(x, y, board, enemy_turn)
      if left_legal_move is not None: 
        moves.append(left_legal_move)
      if right_legal_move is not None: 
        moves.append(right_legal_move)

    number_legal_moves = len(moves)
    if number_legal_moves == 1:
      x_to_eat, y_to_eat = can_eat(board, x, y, enemy_turn)
      x_to_move = moves[0][0]
      y_to_move = moves[0][1]
      if x_to_eat is not None:
        eat_piece(board, x_to_eat, y_to_eat)
        #move_to_new_position(board, x_to_eat - 1, y_to_eat - 1)
      move_to_new_position(board, x_to_move, y_to_move)
      delete_current_position(board, x, y)
    elif number_legal_moves == 2:
      if can_eat_both_pieces(board, x, y, enemy_turn):
         #if not enemy_turn:
        x_to_eat, y_to_eat = get_piece_position(board, min(get_enemy_board_pieces(board, enemy_turn)))
        eat_piece(board, x_to_eat, y_to_eat)
        move_to_new_position(board, x_to_eat - 1, y_to_eat - 1)
        delete_current_position(board, x, y)
         #else:
        #    x_to_eat, y_to_eat = get_piece_position(board, min(get_enemy_board_pieces(board, enemy_turn)))
        #    get_piece_position()
      elif can_only_eat_one_piece(board, x, y): # There is a empty position and a busy position
        x_to_eat, y_to_eat = x - 1, y - 1 if board[x-1][y+1] == 0 else x - 1, y + 1
        #if position_has_enemy(moves, enemy_turn):
        eat_piece(x_to_eat, y_to_eat)
        move_to_new_position(board, x_to_eat - 1, y_to_eat - 1)
        delete_current_position(board, x, y)
      else:
        move_to_new_position(board, x - 1, y - 1)
        delete_current_position(board, x, y)
  return moves

def print_board(board):
  for i in board:
    for j in i:
      print(j, end=" ")
    print()

def inverse_board(board):
  result = []
  board.reverse()
  for row in board:
    row.reverse()
    result.append(row)
  return result

def convert_moves(moves):
    converted_moves = []
    for index, pair in enumerate(moves):
        converted_moves.append((3 - pair[0], 3 - pair[1]))
    return converted_moves

def generate_legal_moves(player, board):
  enemy_turn = False
  legal_moves = []
  x = player[0]
  y = player[1]

  #try:
  if enemy_turn:
      board = inverse_board(board[:])
      legal_moves = check_diagonal_moves(3 - x, 3 - y, board, enemy_turn)
      legal_moves = convert_moves(legal_moves)
  else:
      legal_moves = check_diagonal_moves(x, y, board, False)
  print("Legal moves")
  for move in legal_moves:
      if move != None:
          print(move) 
  print_board(board)
 # except Exception:
  #  print("No hay movimientos disponibles")

board = [[0,0,0,0],
         [0,4,0,3],
         [0,0,1,0],
         [0,2,0,0]
         ]

generate_legal_moves((2,2), board)
     
