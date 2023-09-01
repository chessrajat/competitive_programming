import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total_sum = sum(arr)
    min_number = min(arr)
    max_number = max(arr)

    min_sum = total_sum - max_number
    max_sum = total_sum - min_number

    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr) # Returns