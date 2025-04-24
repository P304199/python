def generate_magic_square(n):
    if n % 2 == 1:
        return odd_magic_square(n)
    elif n % 4 == 0:
        return doubly_even_magic_square(n)
    else:
        return singly_even_magic_square(n)

def odd_magic_square(n):
    magic = [[0]*n for _ in range(n)]
    num = 1
    i, j = 0, n // 2
    while num <= n*n:
        magic[i][j] = num
        num += 1
        newi, newj = (i-1) % n, (j+1) % n
        if magic[newi][newj]:
            i += 1
        else:
            i, j = newi, newj
    return magic

def doubly_even_magic_square(n):
    magic = [[(n*y)+x+1 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if (i % 4 == j % 4) or (i % 4 + j % 4 == 3):
                magic[i][j] = n*n + 1 - magic[i][j]
    return magic

def singly_even_magic_square(n):
    half = n // 2
    subgrid = odd_magic_square(half)
    magic = [[0]*n for _ in range(n)]
    add = [0, 2*half*half, 3*half*half, half*half]
    for i in range(n):
        for j in range(n):
            r, c = i % half, j % half
            idx = (i // half)*2 + (j // half)
            magic[i][j] = subgrid[r][c] + add[idx]
    k = (n - 2) // 4
    for i in range(n):
        for j in range(n):
            if (i < half and j < k) or (i < half and j >= n - k and j < n):
                if i == half // 2:
                    continue
                magic[i][j], magic[i + half][j] = magic[i + half][j], magic[i][j]
    for j in range(k, k + 1):
        magic[half // 2][j], magic[half + half // 2][j] = magic[half + half // 2][j], magic[half // 2][j]
    return magic

def print_magic_square(square):
    for row in square:
        print(" ".join(f"{num:2d}" for num in row))
    print()

for n in [4, 5, 6, 7, 8]:
    print(f"Magic Square for N = {n}")
    print_magic_square(generate_magic_square(n))
