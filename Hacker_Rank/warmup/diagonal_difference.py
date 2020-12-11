# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1+5+9. The right to left diagonal = 3+5+9 . Their absolute difference is . 
# 15 - 17 = 2

def diagonalDifference(arr):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                primary_diagonal_sum += arr[i][j]
            
            if (i+j) == (n-1):
                secondary_diagonal_sum += arr[i][j]
    
    difference = primary_diagonal_sum - secondary_diagonal_sum
    return abs(difference)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
