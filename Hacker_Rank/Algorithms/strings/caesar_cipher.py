
'''/*
 * @Author: Rajat  
 * @Date: 2020-12-23 21:48:23 
 * @Last Modified by:   Rajat 
 * @Last Modified time: 2020-12-23 21:48:23 
 */
'''

def caesarCipher(s, k):
    aa = "abcdefghijklmnopqrstuvwxyz"
    aau = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in s:
        if i in aa:
            result.append(aa[(aa.index(i)+k)%26])
        elif i in aau:
            result.append(aau[(aau.index(i)+k)%26])
        else:
            result.append(i)
    return "".join(result)


if __name__ == '__main__':

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result)