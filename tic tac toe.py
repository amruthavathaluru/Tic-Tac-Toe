import numpy as np
import random
from time import sleep

def create_board():
    return np.array([[0, 0, 0] for _ in range(3)])

def possibilities(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i, j] == 0]

def random_place(board, player):
    selection = possibilities(board)
    if selection:
        current_loc = random.choice(selection)
        board[current_loc] = player
    return board

def row_win(board, player):
    return any(np.all(board[row] == player) for row in range(len(board)))

def col_win(board, player):
    return any(np.all(board[:, col] == player) for col in range(len(board)))

def diag_win(board, player):
    main_diag = np.all(np.diag(board) == player)
    anti_diag = np.all(np.diag(np.fliplr(board)) == player)
    return main_diag or anti_diag

def evaluate(board):
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    return -1 if np.all(board != 0) else 0

def print_board(board):
    symbols = {0: ' ', 1: 'X', 2: 'O'}
    print("\nCurrent Board:")
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(symbols[val] for val in row)}")
    print()

def play_game():
    board, winner, counter = create_board(), 0, 1
    print_board(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"Board after move {counter} by {'Player X' if player == 1 else 'Player O'}")
            print_board(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner

def main():
    winner = play_game()
    if winner == 1:
        print("🎉 Player X wins! Congratulations! 🎉")
    elif winner == 2:
        print("🎉 Player O wins! Congratulations! 🎉")
    else:
        print("It's a tie! Well played both! 😊")

if __name__ == "__main__":
    main()
