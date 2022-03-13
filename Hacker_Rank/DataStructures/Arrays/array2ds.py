
def hourglassSum(arr):
    # Write your code here
    sums = []
    for i in range(len(arr)-2):
        sarr = arr[i]
        for j in range(len(sarr) -2):
            a = sarr[j]
            b = sarr[j+1]
            c = sarr[j+2]
            d = arr[i+1][j+1]
            e = arr[i+2][j]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2]
            sumthis = a+b+c+d+e+f+g
            sums.append(sumthis)
    sums.sort()
    return sums[-1]
         
     

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)