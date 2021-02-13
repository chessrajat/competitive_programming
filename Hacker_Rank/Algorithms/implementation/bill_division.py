

def bonAppetit(bill, k, b):
    bill[k] = 0
    ann = sum(bill)//2
    diff = b - ann
    if diff == 0:
        print("Bon Appetit")
    else:
        print(diff)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
