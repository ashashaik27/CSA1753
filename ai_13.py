import math

PLAYER = 'X'   # Human
AI = 'O'       # Computer

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def check_winner(board):
    # Rows & Cols
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_terminal(board):
    return check_winner(board) or len(empty_cells(board)) == 0

def minimax(board, depth, maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 1
    if winner == PLAYER:
        return -1
    if len(empty_cells(board)) == 0:
        return 0

    if maximizing:
        best = -math.inf
        for (i, j) in empty_cells(board):
            board[i][j] = AI
            val = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best = max(best, val)
        return best
    else:
        best = math.inf
        for (i, j) in empty_cells(board):
            board[i][j] = PLAYER
            val = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best = min(best, val)
        return best

def best_move(board):
    best_val = -math.inf
    move = None
    for (i, j) in empty_cells(board):
        board[i][j] = AI
        move_val = minimax(board, 0, False)
        board[i][j] = ' '
        if move_val > best_val:
            best_val = move_val
            move = (i, j)
    return move

def play():
    board = [[' ']*3 for _ in range(3)]
    turn = PLAYER

    while not is_terminal(board):
        print_board(board)
        if turn == PLAYER:
            r = int(input("Enter row (0-2): "))
            c = int(input("Enter col (0-2): "))
            if (r, c) not in empty_cells(board):
                print("Invalid move!")
                continue
            board[r][c] = PLAYER
            turn = AI
        else:
            print("AI thinking...")
            r, c = best_move(board)
            board[r][c] = AI
            turn = PLAYER

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("Draw!")

if __name__ == "__main__":
    play()
