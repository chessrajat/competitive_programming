# find the number of ways the target can be constructed.


def count_construct(target_word, words):
    if target_word == "":
        return 1

    output = 0
    for word in words:
        if target_word.startswith(word):
            new_word = target_word.replace(word, "")
            output += count_construct(new_word, words)

    return output


print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
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
