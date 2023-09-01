import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    count_0 = 0
    pos_count = 0
    neg_count = 0
    for n in arr:
        if n > 0:
            pos_count += 1
        elif n < 0:
            neg_count += 1
        else:
            count_0 += 1

    arr_len = len(arr)
    print(f"{pos_count/arr_len:.6f}")
    print(f"{neg_count/arr_len:.6f}")
    print(f"{count_0/arr_len:.6f}")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
