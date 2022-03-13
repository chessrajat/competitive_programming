
def countingValleys(steps, path):
    current = 0
    valley = 0
    valley_flag = False
    for i in path:
        if i == "U":
            current += 1
        elif i == "D":
            current -= 1
        if current == -1 and valley_flag is False:
            valley_flag = True
        if current == 0 and valley_flag is True:
            valley += 1
            valley_flag = False
    return valley

    

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)