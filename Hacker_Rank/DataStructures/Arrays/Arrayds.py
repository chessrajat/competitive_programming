
from hashlib import new


def reverseArray(a):
    # Write your code here
    new_array = []
    for i in a:
        new_array.insert(0, i)
    return new_array

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(res)