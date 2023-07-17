
def magic_wand(n, m, arr, queries):
    arr.sort()
    res = []
    for q in queries:
        diff = [abs(q - x) for x in arr]
        diff.sort()
        cost = [0] * n
        cost[0] = diff[0]
        for i in range(1, n):
            cost[i] = cost[i-1] + diff[i]
        res.append(cost[-1])
    return res


if __name__=="__main__":

    vals = list(map(int, input().split()))
    N = vals[0]
    M = vals[1]
    spaces = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    result = magic_wand(N, M, spaces, queries)
    print(" ".join(map(str, result)))
  
