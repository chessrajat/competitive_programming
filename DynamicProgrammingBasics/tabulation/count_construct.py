def count_construct(target, word_bank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i, val in enumerate(table):
        if val == 0:
            continue
        current_word = target[i:]
        for word in word_bank:
            if current_word.startswith(word):
                table[i + len(word)] += val 

    return table[-1]

        



print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        [
            "e",
            "eee",
            "eeeee",
            "eeee",
            "eeeeeee",
            "e",
            "eee",
            "eeeee",
            "eeee",
            "eeeeeee",
        ],
    )
)