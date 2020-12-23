'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-22 12:30:16 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-22 13:21:49
 */
 '''


import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr,n):
    positive = len(list(filter(lambda x:x>0,arr)))
    negative = len(list(filter(lambda x:x<0,arr)))
    zero = len(list(filter(lambda x:x==0,arr)))
    
    return "{:.5f}".format(positive/n), "{:.5f}".format(negative/n), "{:.5f}".format(zero/n)

# def plusMinus2(arr,n):
#     pos = sum(map(lambda x:x>0,arr))
#     neg = sum(map(lambda x:x<0,arr))
#     zero = sum(map(lambda x:x==0,arr))
    


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus2(arr,n)
   
