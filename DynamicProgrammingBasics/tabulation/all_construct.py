def all_construct(target, word_bank):
    table = [[]] * (len(target) + 1)
    for i in range(len(target) + 1):
        table[i] = []
    table[0] = [[]]

    for i in range(len(target)):
        for word in word_bank:
            current_word = target[i:]
            if current_word.startswith(word):
                new_combinations = []
                for subarray in table[i]:
                    new_combinations.append([*subarray, word])
                table[i + len(word)].extend(new_combinations)
    
    return table[-1]
        

print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))