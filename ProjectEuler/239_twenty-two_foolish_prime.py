'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-23 23:10:37 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-23 23:33:27
 */
'''


n,k = map(int,input().split(" "))

a, b = 89,315
N = 10**9 + 123

# modular inverse , a.b^-1 modular N

t = pow(b,N-2,N)
res = a*t % N
print(res)
