import math
import random

# Define the size of the game board
BOARD_SIZE = 3

# Define the players
PLAYER_X = 'X'
PLAYER_O = 'O'

# Define the AI opponent
AI_PLAYER = PLAYER_O

# Initialize the game board with empty spaces
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Print the game board
def print_board():
    for row in board:
        print('|'.join(row))

# Check if a player has won
def check_win(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE-i-1] == player for i in range(BOARD_SIZE)):
        return True
    
    return False

# Check if the game is a tie
def check_tie():
    return all(board[row][col] != ' ' for row in range(BOARD_SIZE) for col in range(BOARD_SIZE))

# Get a list of possible moves
def get_moves():
    return [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE) if board[row][col] == ' ']

# Get the score for a given player
def get_score(player):
    if check_win(player):
        return 1
    elif check_win(get_opponent(player)):
        return -1
    else:
        return 0

# Get the opponent of a given player
def get_opponent(player):
    return PLAYER_O if player == PLAYER_X else PLAYER_X

# Make a move
def make_move(player, row, col):
    board[row][col] = player

# Undo a move
def undo_move(row, col):
    board[row][col] = ' '

# Get the best move using the minimax algorithm
def get_best_move(player):
    best_score = -math.inf
    best_move = None
    
    for move in get_moves():
        make_move(player, *move)
        score = minimax(player, 0, False)
        undo_move(*move)
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move

# Minimax algorithm
def minimax(player, depth, is_maximizing):
    if check_win(AI_PLAYER):
        return 1
    elif check_win(get_opponent(AI_PLAYER)):
        return -1
    elif check_tie():
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for move in get_moves():
            make_move(player, *move)
            score = minimax(player, depth+1, False)
            undo_move(*move)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in get_moves():
            make_move(get_opponent(player), *move)
            score = minimax(player, depth+1, True)
            undo_move(*move)
            best_score = min(best_score, score)
        return best_score

# Initialize the game
def game():
    print("Welcome to Tic Tac Toe!")
   
