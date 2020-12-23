'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-22 13:23:54 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-22 14:47:05
 */
 '''

def staircase(n):
    for i in range(n):
        print(" "*(n-i-1)+"#"*(i+1))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
