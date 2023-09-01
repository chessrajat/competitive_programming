def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            max_value = max(matrix[i][j], matrix[n-i-1][j], matrix[i][n-j-1], matrix[n-i-1][n-j-1])
            s += max_value
    return s

if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(result)