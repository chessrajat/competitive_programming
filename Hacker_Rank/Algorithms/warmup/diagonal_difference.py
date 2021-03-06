# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1+5+9. The right to left diagonal = 3+5+9 . Their absolute difference is . 
# 15 - 17 = 2

# def diagonalDifference(arr):
#     primary_diagonal_sum = 0
#     secondary_diagonal_sum = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 primary_diagonal_sum += arr[i][j]
            
#             if (i+j) == (n-1):
#                 secondary_diagonal_sum += arr[i][j]
    
#     difference = primary_diagonal_sum - secondary_diagonal_sum
#     return abs(difference)

def diagonalDifference(arr):
    d1, d2 = 0, 0
    n = len(arr)
    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[n-i-1][i]
    difference = d1 - d2
    return abs(difference)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
