'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-27 12:12:43 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-27 12:41:58
 */
'''

def getTotalX(a, b):
    # Write your code here
    low_b = min(b)
    b_factors = []
    for i in range(1,low_b+1):
        if low_b%i == 0:
            b_factors.append(i)

    a_factor = []
    for i in b_factors:
        if all(i % x == 0 for x in a):
            a_factor.append(i)

    factors = []
    for i in a_factor:
        if all(x%i == 0 for x in b):
            factors.append(i)

    return len(factors)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)