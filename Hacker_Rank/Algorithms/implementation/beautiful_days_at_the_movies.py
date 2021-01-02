'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-02 22:23:38 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-02 22:36:02
 */
'''
def reversen(num):
    return int(str(num)[::-1])

def beautifulDays(i, j, k):
    count = 0
    for ii in range(i,j+1):
        res = (ii - reversen(ii)) / k
        if res.is_integer():
            count += 1
    
    return count


if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)
