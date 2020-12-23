'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-23 22:09:46 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-23 22:44:37
 */
'''
from itertools import zip_longest

def marsExploration(s):
    val = 0
    s_list = [s[i:i+3] for i in range(0, len(s), 3)]
    sos = "SOS"
    for i in s_list:
        if i != sos:
            for j in range(len(i)):
                if i[j] != sos[j]:
                    val += 1
    return val

if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

    print(result)