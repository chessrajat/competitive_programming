import textwrap

def wrap(string, max_width):
    output = ""
    checker = 0
    for i in string:
        output += i
        checker += 1
        if max_width == checker:
            output += "\n"
            checker = 0
    return output


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)