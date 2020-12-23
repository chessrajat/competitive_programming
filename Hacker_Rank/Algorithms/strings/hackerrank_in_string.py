'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-23 22:52:31 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-23 22:59:26
 */
'''

def hackerrankInString(s):
    a = "hackerrank"
    a_counter = 0
    for i in s:
        if i == a[a_counter]:
            a_counter += 1
        if a_counter == 10:
            break
    print(a_counter)
    if a_counter == len(a):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)
