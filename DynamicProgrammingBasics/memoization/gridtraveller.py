# You are the traveller on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down or right.
# How many ways you can travel to the goal in m*n grid?


def grid_traveller(m, n, memo={}):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if (m, n) in memo:
        return memo[(m, n)]
    memo[(m, n)] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)
    return memo[(m, n)]


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
