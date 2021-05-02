
def front_flip(n,p):
    flips = 0
    for i in range(2,n,2):
        flips += 1
        if p == i or p== (i+1):
            return flips

def back_flip(n,p):
    flips = 0
    if n%2 == 0:
        #even
        if n==p:
            return 0
        for i in range(n-1,0,-2):
            flips += 1
            if p == i or p== (i+1):
                return flips
    else:
        #odd
        if p==n or p==n-1:
            return 0
        for i in range(n,0,-2):
            flips += 1
            if p == i or p== (i+1):
                return flips

def pageCount(n, p):
    flips = []
    if p==1:
        return 0
    
    flips.append(back_flip(n,p))
    flips.append(front_flip(n,p))
    return min(flips)


if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)
