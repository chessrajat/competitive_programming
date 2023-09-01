def findMedian(arr):
    # Write your code here
    sorted_array = sorted(arr)
    middle_index = (len(sorted_array) - 1) // 2
    return sorted_array[middle_index]

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(result)