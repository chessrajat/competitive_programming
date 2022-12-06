#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    a_count = s.count("a")
    occurences = n//len(s)
    left = n%len(s)
    left_string = s[0:left]
    left_count = left_string.count("a")
    total_count = (a_count * occurences) + left_count
    return total_count

if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)
    print(result)