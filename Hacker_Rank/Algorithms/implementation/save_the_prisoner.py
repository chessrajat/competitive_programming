'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-02 22:58:33 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-02 23:31:24
 */
'''

def saveThePrisoner(n, m, s):
    res = (m+s-1) % n
    if res == 0:
        return n
    return res


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(result)