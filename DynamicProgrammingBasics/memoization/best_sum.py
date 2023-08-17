
def best_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = target_sum - num
        result = best_sum(remainder, numbers, memo)
        if result != None:
            result.append(num)
            if shortestCombination is None or len(result) < len(shortestCombination):
                shortestCombination = result

    memo[target_sum] = shortestCombination
    return shortestCombination


print(best_sum(50, [5, 3, 4, 25]))


# Some issue