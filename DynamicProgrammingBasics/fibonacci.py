
# O(2^n) time complexity
def fib_old(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib(n, memo={}):
    if n<=2:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


print(fib(50))
