'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-03 14:40:59 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-03 15:23:30
 */
'''
def countApplesAndOranges(s, t, a, b, apples, oranges):
    app, ora = 0, 0
    correct_range = range(s,t+1)
    for apple in apples:
        if a + apple in correct_range:
            app += 1
    for orange in oranges:
        if b + orange in correct_range:
            ora += 1
        
    print(app)
    print(ora)
         

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)