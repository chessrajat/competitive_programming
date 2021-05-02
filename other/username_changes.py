
def possibleChanges(usernames):
    # Write your code here
    result = []
    
    for username in usernames:
        flag = False
        for i in range(len(username)-1):
            if username[i] <= username[i+1]:
                continue
            else:
                result.append("YES")
                flag = True
                break
        if not flag:
            result.append("NO")
    return result
    


if __name__ == '__main__':
  

    usernames_count = int(input().strip())

    usernames = []

    for _ in range(usernames_count):
        usernames_item = input()
        usernames.append(usernames_item)

    result = possibleChanges(usernames)
    print(result)