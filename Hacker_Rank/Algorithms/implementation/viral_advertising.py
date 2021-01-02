'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-02 22:52:29 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-02 22:55:39
 */
'''

def viralAdvertising(n):
    likes = 0
    value = 5
    for i in range(n):
        l = value // 2
        likes += l
        value = l * 3
    
    return likes

if __name__ == '__main__':

    n = int(input())

    result = viralAdvertising(n)
    print(result)
