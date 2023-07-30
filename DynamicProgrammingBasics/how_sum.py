def how_sum(target_num, numbers, memo={}):
    output = []
    if target_num in memo:
        return memo[target_num]
    if target_num == 0:
        return []
    if target_num < 0:
        return None

    for n in numbers:
        remainder = target_num - n
        memo[target_num] = how_sum(remainder, numbers)
        if memo[target_num] != None:
            memo[target_num].append(n)
            return memo[target_num]

    return None


print(how_sum(7, [3,4,7]))
