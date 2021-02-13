


def birthday(s, d, m):
    ways = 0
    for i in range(len(s)):
        n =0
        sum = 0
        for num in range(i,len(s)):
            n += 1
            sum += s[num]
            if sum == d and n == m:
                ways += 1
                break
            if sum>d:
                break
    return ways


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(result)

