import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

def find_max(nums):
    for i in nums:
        small = 0
        large = 0
        for j in range(i[0],i[1]+1):
            if is_prime(j):
                small = j
                break
        for k in range(i[1],i[0] - 1,-1):
            if is_prime(k):
                large = k
                break

        # print(f"small - {small}")
        # print(f"large - {large}")

        if (small and large) == 0:
            print(-1)
        else:
            print(large - small)




if __name__ == '__main__':

    ar_count = int(input())
    nums = []
    for i in range(ar_count):
        ar = list(map(int, input().rstrip().split()))
        nums.appena(ar)

    result = find_max(nums)
