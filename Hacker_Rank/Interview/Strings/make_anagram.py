#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

from numpy import delete


def makeAnagram(a, b):
    # Write your code here
    a = sorted(a)
    b = sorted(b)
    deleted_chars_from_a = 0
    deleted_chars_from_b = 0
    
    print(a)
    print(b)

    
    return deleted_chars_from_a + deleted_chars_from_b


if __name__ == '__main__':
    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)