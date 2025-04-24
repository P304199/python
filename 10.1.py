def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:  
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:  
            return False
        if col + (row - i) < 8 and board[i][col + (row - i)] == 1:  
            return False
    return True

def solve_n_queens(board, row=0):
    if row == 8:
        print_board(board)
        return True  
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0  
    return False

board = [[0 for _ in range(8)] for _ in range(8)]

solve_n_queens(board)
