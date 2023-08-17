def how_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i, val in enumerate(table):
        if val is not None:
            for j in numbers:
                if i+j <= target_sum:
                    table[i+j] = [*table[i], j]

    return table[-1]


print(how_sum(7, [2,3]))
print(how_sum(7, [5,3,4,7]))
print(how_sum(7, [2,4]))
print(how_sum(8, [2,3,5]))
print(how_sum(300, [7,14]))