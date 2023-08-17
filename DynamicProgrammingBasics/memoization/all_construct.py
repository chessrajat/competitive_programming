

def all_construct(target_word, words):
    if target_word == "":
        return [[]]

    output = []
    for word in words:
        if target_word.startswith(word):
            new_word = target_word.replace(word, "")
            result = all_construct(new_word, words)
            # this results in None because insert changes the original variable and returns None.
            # target_ways = list(map(lambda x: x.insert(0, word), result))``
            target_ways = [x.insert(0, word) or x for x in result]
            output.extend(target_ways)

    
    return output


print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
