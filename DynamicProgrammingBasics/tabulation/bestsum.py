def best_sum(target_sum, numbers):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i, val in enumerate(table):
        if val is not None:
            for j in numbers:
                if i + j <= target_sum:
                    new_array = [*table[i], j]
                    if table[i + j] is None:
                        table[i + j] = new_array
                    else:
                        if len(table[i + j]) > len(new_array):
                            table[i + j] = new_array

    return table[-1]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
