
def sockMerchant(n, ar):
    pairs = 0
    ar_s = set(ar)
    for color in ar_s:
        c = ar.count(color)
        pairs += c//2
    
    return pairs


if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)