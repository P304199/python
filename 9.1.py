def is_safe(board, row, col):

    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col  
            if solve_queens(board, row + 1):  
                return True
            board[row] = -1  

    return False

def print_solution(board):
    for row in range(len(board)):
        line = ["Q" if col == board[row] else "." for col in range(len(board))]
        print(" ".join(line))

def eight_queens():
    board = [-1] * 8  
    
    if solve_queens(board, 0):
        print_solution(board)
    else:
        print("Solution does not exist.")

eight_queens()
