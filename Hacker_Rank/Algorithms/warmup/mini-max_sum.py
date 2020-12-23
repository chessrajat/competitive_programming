'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-22 15:02:43 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-22 15:07:37
 */
'''

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)