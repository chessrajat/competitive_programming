


def minimumNumber(n, password):
    a = 0
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    chars = [numbers,lower_case,upper_case,special_characters]
    for c in chars:
        res = any([x in password for x in c])
        if not res:
            a += 1
    
    if a + n < 6:
        a = a + (6 - (a+n))
   
       
    return a


if __name__ == '__main__':

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)