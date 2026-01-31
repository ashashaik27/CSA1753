def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    # Rows
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

    # Columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        try:
            r = int(input("Enter row (0-2): "))
            c = int(input("Enter column (0-2): "))
        except:
            print("Invalid input. Try again.")
            continue

        if r not in range(3) or c not in range(3) or board[r][c] != " ":
            print("Invalid move! Try again.")
            continue

        board[r][c] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
