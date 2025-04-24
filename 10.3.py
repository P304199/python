def is_safe(position, row, col):
    for i in range(row):
        if position[i] == col or \
           position[i] - i == col - row or \
           position[i] + i == col + row:
            return False
    return True

def solve_queens(row=0, position=[-1]*8):
    if row == 8:
        print_board(position)
        return True
    for col in range(8):
        if col not in position[:row] and is_safe(position, row, col):
            position[row] = col
            if solve_queens(row + 1, position):
                return True
    return False

def print_board(position):
    for row in range(8):
        line = ["Q" if col == position[row] else "." for col in range(8)]
        print(" ".join(line))
    print()

solve_queens()
