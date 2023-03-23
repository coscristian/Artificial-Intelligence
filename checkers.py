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
    """
    #Until
    for (piece, value) in [(chess.PAWN, 10), (chess.BISHOP, 30), (chess.KING, 900), (chess.QUEEN, 90), 
                           (chess.KNIGHT, 30), (chess.ROOK, 50)]:
        score += len(board.pieces(piece, chess.WHITE)) * value
        score -= len(board.pieces(piece, chess.BLACK)) * value
    if board.is_checkmate():
        score += 100
    elif board.is_check():
        score += 30
    return score
    """

#print(scoreCount(board))

def count_right_diagonal_enemies(x, y, board):
  total_right_diag = 0
  while y < len(board[0]) - 1 and x > 0 and board[x - 1][y + 1] > 2:
    total_right_diag += 1
    x -= 1
    y += 1
  print("Right Enemies: ", total_right_diag)
  return total_right_diag

def count_left_diagonal_enemies(x, y, board):
  total_left_diag = 0
  while y > 0 and x > 0 and board[x - 1][y - 1] > 2:
    total_left_diag += 1
    x -= 1
    y -= 1
  print("Left Enemies: ", total_left_diag)
  return total_left_diag

"""
def check_up_move(x, y, board):
    if board[x-1][y] == 0:
      legal_moves.append((x-1, y)) #Add the legal up movement


If y == 0
  check right diagonal
elif y == last_column
  check left diagonal
else:
  check both diagonal sides
"""

def check_move_left_diagonal(x, y, board):
  
  if board[x-1][y-1] == 0:
    return (x - 1, y - 1)

  #Can eat at least one enemy piece, but must check if can eat more enemy pieces
  #So, count the pieces which are in the diagonal
  #amount_left_diag_pieces, amount_right_diag_pieces = count_enemy_pieces_diagonal(x, y, board)

  amount_left_diag_pieces = count_left_diagonal_enemies(x, y, board)
  
  #Check if my piece can be placed in a casilla after eating the enemy pieces
  if y - amount_left_diag_pieces > 0 and x - amount_left_diag_pieces > 0:
    legal_x = x - amount_left_diag_pieces - 1
    legal_y = y - amount_left_diag_pieces - 1
    return (legal_x, legal_y)
    #board[x - amount_left_diag_pieces - 1][y - amount_left_diag_pieces - 1] = 1 #Place the player one
  return None

def check_move_right_diagonal(x, y, board):
  if board[x-1][y + 1] == 0:
    return (x - 1, y + 1)

  #Can eat at least one enemy piece, but must check if can eat more enemy pieces
  #So, count the pieces which are in the diagonal
  amount_right_diag_enemies = count_right_diagonal_enemies(x, y, board)
  
  #Check if my piece can be placed in a casilla after eating the enemy pieces
  if y + amount_right_diag_enemies < len(board[0]) - 1 and x - amount_right_diag_enemies > 0:
    legal_x = x - amount_right_diag_enemies - 1
    legal_y = y + amount_right_diag_enemies + 1
    return (legal_x, legal_y)
    #board[x - amount_left_diag_pieces - 1][y - amount_left_diag_pieces - 1] = 1 #Place the player one
  return None

def check_diagonal_moves(x,y,board):
  moves = []
  if x > 0: #Can move up
    if y == 0: # Check only right diagonal
      legal_move = check_move_right_diagonal(x, y, board)
      moves.append(legal_move)
    elif y == len(board[0]) - 1: # Check only left diagonal
      legal_move = check_move_left_diagonal(x, y, board)
      moves.append(legal_move)
    else: #check both diagonal sides
      left_legal_move = check_move_left_diagonal(x, y, board)
      right_legal_move = check_move_right_diagonal(x, y, board)
      moves.append(left_legal_move)
      moves.append(right_legal_move)
  
  return moves

"""
Parameters
  player: tuple() Stores the position x, y of the player
  board: Board of the game

Return 
  legal_moves: [] Legal movemements for the player
"""
def generate_legal_moves(player, board):
  legal_moves = []
  x = player[0]
  y = player[1]
  legal_moves = check_diagonal_moves(x,y,board)
  
  for move in legal_moves:
    if move != None:
      print(move) 
  #print(legal_moves) 

board = [[0,0,0,0],
         [0,4,0,0],
         [0,0,3,0],
         [0,2,0,1]
         ]
generate_legal_moves((3,3), board)
     
#print(generar_movimientos(board1, 'o'))
"""
def minimax(board, depth, max_player, alpha, beta):
    if depth==0 or board.is_game_over():
        return scoreCount(board), None
    moves = list(board.legal_moves)
    random.shuffle(moves)
    if max_player:
        max_eval = -float("Inf")
        for move in moves:
            board.push(move)
            current_eval,curMove= minimax(board, depth-1,False, alpha,beta)
            board.pop()
            if current_eval>max_eval:
                max_eval = current_eval
                best_move = move
                alpha = max(alpha, max_eval)
                if beta<=alpha:
                    break
        return max_eval, best_move
    else:
        min_eval = float("Inf")
        for move in moves:
            board.push(move)
            current_eval,curMove = minimax(board, depth-1,True,alpha, beta)
            board.pop()
            if current_eval<min_eval:
                min_eval = current_eval
                best_move = move
                beta = min(beta, min_eval)
                if beta<=alpha:
                    break
        return min_eval, best_move

"""



"""
        if board[x-1][y-1] == 0:
          moves.append((x-1,y-1))
        else: 
          #Can eat at least one enemy piece, but must check if can eat more enemy pieces
          #So, count the pieces which are in the diagonal
          #amount_left_diag_pieces, amount_right_diag_pieces = count_enemy_pieces_diagonal(x, y, board)

          amount_left_diag_pieces = count_left_diagonal_enemies(x, y, board)
        
        #Check if my piece can be placed in a casilla after eating the enemy pieces
        if y - amount_left_diag_pieces > 0 and x - amount_left_diag_pieces > 0:
          legal_x = x - amount_left_diag_pieces - 1
          legal_y = y - amount_left_diag_pieces - 1
          moves.append((legal_x, legal_y))
          #board[x - amount_left_diag_pieces - 1][y - amount_left_diag_pieces - 1] = 1 #Place the player one

        if y + amount_right_diag_pieces < len(board[0]) - 1 and x - amount_right_diag_pieces > 0:
          legal_x = x + amount_left_diag_pieces + 1
          legal_y = y + amount_left_diag_pieces + 1
          moves.append((legal_x, legal_y))
        
        #Positions to delete every enemy piece
        new_x = x 
        new_y = y
        #Delete the enemy pieces that have been eaten
        for i in range(amount_left_diag_pieces):
          new_x -= 1
          new_y -= 1
          board[new_x][new_y] = 0

  #Right diagonal move
  if y < len(board[0]) - 1:
    if board[x-1][y + 1] == 0:
      moves.append((x-1, y+1))
    else:
      #Can eat at least one enemy piece, but must check if can eat more enemy pieces
      #So, count the pieces which are in the diagonal
      amount_right_diag_pieces = count_enemy_pieces_diagonal(x, y, board)[1]
      
      #Check if my piece can be placed in a casilla after eating the enemy pieces
      if y + amount_right_diag_pieces < len(board[0]) - 1 and x - amount_right_diag_pieces > 0:
        legal_x = x + amount_left_diag_pieces + 1
        legal_y = y + amount_left_diag_pieces + 1
        moves.append((legal_x, legal_y))
        #board[x - amount_left_diag_pieces - 1][y - amount_left_diag_pieces - 1] = 1 #Place the player one

      #Positions to delete every enemy piece
      new_x = x 
      new_y = y
      #Delete the enemy pieces that have been eaten
      for i in range(amount_left_diag_pieces):
        new_x -= 1
        new_y -= 1
        board[new_x][new_y] = 0

      #amount_right_diag_pieces = count_enemy_pieces_diagonal(x, y, board)[1]
"""