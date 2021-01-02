'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-02 22:20:27 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-02 22:21:54
 */
'''

def simpleArraySum(ar):
    #
    # Write your code here.
    return sum(ar)

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
