import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    total = 0
    q = [i-1 for i in q]
    for key, i in enumerate(q):
        diff = i - key
        if diff > 2:
            return "Too chaotic"
        else:
             for k in q[max(i-1, 0):key]:
                if k > i:
                    total += 1

    return total


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        result = minimumBribes(q)
        print(result)
