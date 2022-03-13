
def continous_combi(arr, length):
    result = []
    for i in range (0, len(arr)+1-length):
        entry = []
        for j in range (0, length):
            entry.append(arr[i+j])
        result.append(entry)
    return result

def find_combinations(arr):
    all_comb = []
    for i in range(1,len(arr) + 1):
        comb_obj = continous_combi(arr,i)
        all_comb += (list(comb_obj))
    return all_comb


def find_mean(all_comb, val):
    output = 0
    for s in all_comb:
        if not len(s) == 0:
            if sum(s)/len(s) == val:
                output += 1
    return output
    
if __name__=="__main__":
    a = list(map(int,input().split()))
    s = int(input())
    comb = find_combinations(a)
    times = find_mean(comb, s)
    print(times)