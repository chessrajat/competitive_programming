

def find_p(N, X, levels):
    sorted_levels = sorted(levels, key=lambda x: x)
    min_p = sorted_levels[-(X)]
    found_animals =  sorted_levels.index(min_p)
    if X < N - found_animals:
        return -1
    return min_p


if __name__=="__main__":

    vals = list(map(int, input().split()))
    N = vals[0]
    X = vals[1]
    levels = list(map(int, input().split()))

    print(find_p(N, X, levels))