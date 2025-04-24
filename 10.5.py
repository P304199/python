import random

def is_safe(position, row, col):
    for i in range(row):
        if position[i] == col or \
           position[i] - i == col - row or \
           position[i] + i == col + row:
            return False
    return True

def random_queen_solver():
    solutions = set()
    attempts = 0
    while len(solutions) < 92:
        position = [-1] * 8
        rows = list(range(8))
        cols = list(range(8))
        random.shuffle(cols)
        success = True
        for row in rows:
            placed = False
            random.shuffle(cols)
            for col in cols:
                if is_safe(position, row, col):
                    position[row] = col
                    placed = True
                    break
            if not placed:
                success = False
                break
        if success:
            solutions.add(tuple(position))
        attempts += 1
        if attempts > 100000:
            break
    for pos in solutions:
        print_board(pos)
    print(f"Total unique solutions found: {len(solutions)}")

def print_board(position):
    for row in range(8):
        line = ["Q" if col == position[row] else "." for col in range(8)]
        print(" ".join(line))
    print()

random_queen_solver()
