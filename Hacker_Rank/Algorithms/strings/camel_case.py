

def camelcase(s):
    # Write your code here
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count +1

if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(result)

