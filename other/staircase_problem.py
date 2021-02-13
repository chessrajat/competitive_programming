
# 1.  You have 'n' number of stairs. you can only go 1stair or 2stair at a time.
#     how many ways you can go stairs up.


def staircase(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return staircase(n-1) + staircase(n-2)

def staircase_bottoms_up(n):
    first = 1
    second = 1
    sum = 0
    for i in range(n-1):
        sum = first + second
        first,second = second,sum
    return sum
    
    
def staircase_with_steps(n,x):
    if n == 0:
        return 1
    nums = [0] * (n+1)
    nums[0] = 1
    for i in range(1,n+1):
        total = 0
        for j in x:
            if i-j >=0:
                total += nums[i-j]
        nums[i] = total
    
    return nums[n]






print(staircase_with_steps(4,[1,3,5]))


