'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-11 09:41:45 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-11 10:15:48
 */
'''

# 1721
# 979
# 366
# 299
# 675
# 1456

def find_2_numbers_of_sum(num_list, number):
    for i in num_list:
        check_num = number - i
        if check_num in num_list:
                return i*check_num

def find_3_numbers_of_sum(num_list, number):
    for i in num_list:
        for j in num_list:
            check_num = number - i - j
            if check_num in num_list:
                return i * j * check_num


if __name__ == "__main__":
    sample_list = [1721, 979, 366, 299, 675, 1456]
    with open("input1_1.txt","r") as f:
        num_list = f.readlines()

    num_list = [int(i.strip("\n")) for i in num_list]
    # ans = find_2_numbers_of_sum(sample_list,2020)
    ans = find_3_numbers_of_sum(num_list, 2020)
    print(ans)