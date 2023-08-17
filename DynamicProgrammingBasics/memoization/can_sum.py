# write a function canSum(target_sum, numbers) that takes in a target sum and and array of numbers
# The function should return a boolean value indicating whether or not it is possible to generate the
# target sum using the numbers.

# you may use an element of the array as many times as you want
# you may assume that all inpuut numbers are nonnegative.


def can_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for n in numbers:
        remainder = target_sum - n
        memo[remainder] = can_sum(remainder, numbers, memo) 
        if memo[remainder] == True:
            return True
    return False


print(can_sum(7, [2,4]))
