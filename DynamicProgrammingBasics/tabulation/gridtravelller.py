def grid_traveller(m, n):
    if m < 1 and n < 1:
        return 0
    table = [[0 for _ in range(n+1)] for _ in range(m+1)] 
    table[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if i + 1 <= m:
                table[i + 1][j] += current
            if j + 1 <= n:
                table[i][j + 1] += current
    return table[m][n]


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 2))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
