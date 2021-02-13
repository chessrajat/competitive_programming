'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-27 13:10:44 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-27 13:21:46
 */
'''

def breakingRecords(scores):
    l_count = 0
    h_count = 0
    low = scores[0]
    high = scores[0]
    for i in scores:
        if i<low:
            low = i
            l_count += 1
        elif i> high:
            high = i
            h_count += 1
        else:
            continue
    
    return [h_count, l_count]


if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
