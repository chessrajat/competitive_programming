import itertools

def get_subsequence(string):
    combs = []
    result = []
    for l in range(1, len(string)+1):
        combs.append(list(itertools.combinations(string, l)))

    for c in combs:
        for t in c:
            result.append(''.join(t))
    
    return result

def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
 
    j = 0    # Index of str1
    i = 0    # Index of str2
 
    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1
 
    return j == m

def report(composition, ar):
    # r = get_subsequence(composition)
    for a in ar:
        print("POSITIVE" if isSubSequence(a, composition) else "NEGATIVE")




if __name__=="__main__":

    compsition = input()
    people = int(input())

    ar = []
    for i in range(people):
        ar.append(input())

    result = report(compsition, ar)