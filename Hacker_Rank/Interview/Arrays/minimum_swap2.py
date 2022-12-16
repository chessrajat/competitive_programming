import enum
import math
import os
import random
import re
import sys
import  numpy as np

# Complete the minimumSwaps function below.
def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# def minimumSwaps(arr):
#     swaps = 0
#     for key in range(len(arr)):
#         curr_min = min(arr[key:])
#         curr_index = arr.index(curr_min)
#         if curr_index != key:
#             arr = swapPositions(arr, key, curr_index)
#             swaps  += 1
    
#     return swaps

def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
         while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            swaps += 1
    
    return swaps



    

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)