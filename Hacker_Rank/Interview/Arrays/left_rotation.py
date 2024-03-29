#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#


def rotLeft(a, d):
    if len(a) >= d:
        sub_items = a[0:d]
        left_array = a[d:]

        new_arr = left_array + sub_items
        return new_arr
    else:
        times = d//len(a)
        left = d - (len(a) * times)
        if left==0:
            return a


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)
