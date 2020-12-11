'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-11 20:30:45 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-11 22:12:52
 */
'''

# --- Day 2: Password Philosophy ---
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number of times a given letter must 
# appear for the password to be valid. 
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

def clean_output(lpass):
    range_chr,password = lpass.split(":")
    range,character = range_chr.split(" ")
    password = password.strip()
    start,end = range.split("-")
    return int(start.strip()), int(end.strip()), character, password

def password_philosophy(pass_list):
    valid_count = 0
    for lpass in pass_list:
        start, end, character, password = clean_output(lpass)
        chr_occurence = password.count(character)
        if start<=chr_occurence<=end:
            valid_count += 1
    return valid_count


def password_philosophy2(pass_list):
    valid_count = 0
    for lpass in pass_list:
        start, end, character, password = clean_output(lpass)
        try:
            a = password[start-1] == character
            b = password[end-1] == character
            if a^b == 1:
                valid_count += 1
        except:
            print("Index error")
    return valid_count


if __name__ == "__main__":
    sample_list = ["1-3 a: abcde","1-3 b: cdefg"]
    with open("day2_1.txt","r") as f:
        pass_list = f.readlines()
    
    pass_list = [i.strip("\n") for i in pass_list]
    a = password_philosophy2(pass_list)
    print(a)