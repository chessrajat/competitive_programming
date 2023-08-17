def can_construct(target, word_bank):
    table = [False] * (len(target) + 1)
    table[0] = True
    for i, val in enumerate(table):
        if val is True:
            current_word = target[i:]
            for word in word_bank:
                if current_word.startswith(word):
                    j = len(word)
                    if i + j <= len(target):
                        table[i + j] = True

    return table[-1]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    can_construct(
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
