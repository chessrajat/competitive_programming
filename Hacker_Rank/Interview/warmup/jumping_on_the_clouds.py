from os import truncate


def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    one_jump = False
    for i in range(1, len(c)):
        if c[i] == 0:
            if not one_jump:
                one_jump = True
                if i == len(c)-1:
                    jumps += 1
            else:
                jumps += 1
                one_jump = False
        else:
            if one_jump:
                jumps += 1
            else:
                one_jump = True
                continue
        
    return jumps


if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)