import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# def arrayManipulation(n, queries):
#     # Write your code here
#     our_list = [0] * n
#     for query in queries:
#         i = query[0]
#         j = query[1]
#         val = query[2]
#         # new_vals = np.add(our_list[i-1:j], val).tolist()
#         new_vals = list(map(lambda x: x + val, our_list[i-1:j]))
#         our_list[i-1:j] = new_vals
#         print(max(our_list))
#     return max(our_list)

def arrayManipulation(n, queries):
    # Write your code here
    our_list = [0] * (n + 1)
    for query in queries:
        i = query[0]
        j = query[1]
        val = query[2]
        our_list[i - 1] += val
        our_list[j] -= val
    
    max_num = 0
    temp = 0
    for val in our_list:
        temp += val
        max_num = max(max_num, temp)
    return max_num

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
