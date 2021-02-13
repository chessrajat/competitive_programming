'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-17 16:41:18 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-17 18:20:35
 */
'''

def kangaroo(x1, v1, x2, v2):
    if x2>x1 and v2 >= v1:
        return "NO"
    count = 0
    while(count<=10000):
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"
        count += 1
    return "NO"

# if x1 > x2:
#     if v2 > v1 and (x1-x2) % (v2-v1) == 0:
#         print("YES")
#     else:
#         print("NO")
# elif x1 < x2:
#     if v1 > v2 and (x2-x1) % (v1-v2) == 0:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("YES")
    

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)