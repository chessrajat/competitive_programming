

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev = 0
    current = 1
    for _ in range(2, n+1):
        temp = prev
        prev = current
        current = current + temp
    
    return current



print(fib(1))