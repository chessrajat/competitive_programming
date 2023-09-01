import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Write your code here
    a.sort()
    a.append(0)
    for i in range(0, len(a), 2):
        if a[i] != a[i + 1]:
            return a[i]


if __name__ == "__main__":
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)
