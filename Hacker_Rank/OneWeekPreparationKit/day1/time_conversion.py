import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    am_pm = s[-2:]
    time = s[:-2]
    hr, mi, sec = time.split(":")
    
    if am_pm == "AM":
        if hr == "12":
            return f"00:{mi}:{sec}"
        else:
            return f"{hr}:{mi}:{sec}"
    elif am_pm == "PM":
        if hr == "12":
            return f"{hr}:{mi}:{sec}"
        else:
            hr = int(hr) + 12
            return f"{hr}:{mi}:{sec}"

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)