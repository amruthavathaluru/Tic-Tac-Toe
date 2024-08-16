import numpy as np
import random
from time import sleep

def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

def user_move(board, player, player_name):
    while True:
        try:
            move = int(input(f"{player_name}, enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError("Move must be between 1 and 9.")
            
            row, col = divmod(move - 1, 3)
            if board[row, col] != 0:
                print("Cell already taken. Choose another cell.")
            else:
                board[row, col] = player
                break
        except ValueError as e:
            print(e)

def row_win(board, player):
    for x in range(len(board)):
        if all(board[x, y] == player for y in range(len(board))):
            return True
    return False

def col_win(board, player):
    for x in range(len(board)):
        if all(board[y, x] == player for y in range(len(board))):
            return True
    return False

def diag_win(board, player):
    if all(board[x, x] == player for x in range(len(board))):
        return True
    if all(board[x, len(board) - 1 - x] == player for x in range(len(board))):
        return True
    return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(['X' if cell == 1 else 'O' if cell == 2 else ' ' for cell in row]))
        print("-" * 3 * len(board))
    print()

def play_game(player1_name, player2_name):
    board, winner, counter = create_board(), 0, 1
    print_board(board)
    sleep(2)

    while winner == 0:
        for player, name in [(1, player1_name), (2, player2_name)]:
            user_move(board, player, name)
            print(f"Board after move {counter}")
            print_board(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner

def main():
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")
    
    winner = play_game(player1_name, player2_name)
    if winner == -1:
        print("It's a Tie! Well played!")
    else:
        winner_name = player1_name if winner == 1 else player2_name
        print(f"Congratulations {winner_name}! You are the Winner!")

if __name__ == "__main__":
    main()
