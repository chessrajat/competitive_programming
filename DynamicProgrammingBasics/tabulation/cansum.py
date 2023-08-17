def can_sum(target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True
    for i, val in enumerate(table):
        if val == False:
            continue
        for j in numbers:
            if i + j <= target_sum:
                table[i + j] = True
    return table[-1]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
