# finding sum of n large integers

# def aVeryBigSum(ar):
#     sum = 0
#     for i in ar:
#         sum += i
#     return sum

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':


    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)