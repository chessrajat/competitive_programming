# check if target can be constructed by concatinating the words in array


def can_construct(target_word, words):
    if target_word == "":
        return True

    for word in words:
        if target_word.startswith(word):
            new_word = target_word.replace(word, "")
            result = can_construct(new_word, words)
            if result:
                return True
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
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
