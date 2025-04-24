def generate_magic_square(n):
    if n % 2 != 0:  
        return generate_odd_magic_square(n)
    elif n % 4 == 0: 
        return generate_doubly_even_magic_square(n)
    else:  
        return generate_singly_even_magic_square(n)

def generate_odd_magic_square(n):
    square = [[0 for _ in range(n)] for _ in range(n)]
    row, col = 0, n // 2  
    
    for num in range(1, n*n + 1):
        square[row][col] = num
        new_row, new_col = (row - 1) % n, (col + 1) % n  
        if square[new_row][new_col]:  
            row += 1  
        else:
            row, col = new_row, new_col  
    return square

def generate_doubly_even_magic_square(n):
    square = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            square[i][j] = n * i + j + 1

    for i in range(0, n, 4):
        for j in range(0, n, 4):
            for k in range(4):
                for l in range(4):
                    if (k + l) % 2 == 0:
                        square[i + k][j + l] = n*n - (n*(i + k) + (j + l))
    return square

def generate_singly_even_magic_square(n):
    square = [[0 for _ in range(n)] for _ in range(n)]
    sub_square_size = n // 2

    sub_square_1 = generate_odd_magic_square(sub_square_size)
    sub_square_2 = generate_odd_magic_square(sub_square_size)
    

    for i in range(sub_square_size):
        for j in range(sub_square_size):
            square[i][j] = sub_square_1[i][j]
            square[i + sub_square_size][j + sub_square_size] = sub_square_2[i][j]
    

    for i in range(sub_square_size):
        for j in range(sub_square_size):
            square[i + sub_square_size][j] = sub_square_2[i][j] + sub_square_size * sub_square_size
            square[i][j + sub_square_size] = sub_square_1[i][j] + sub_square_size * sub_square_size
    return square

def print_square(square):
    for row in square:
        print("\t".join(str(num) for num in row))


for size in [4, 5, 6, 7, 8]:
    print(f"Magic square for N={size}:")
    magic_square = generate_magic_square(size)
    print_square(magic_square)
    print("\n")
