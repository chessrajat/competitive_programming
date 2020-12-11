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

def find_numbers_of_sum(num_list, number):
    for i in num_list:
        check_num = number - i
        for j in num_list:
            if check_num == j:
                return i*j



if __name__ == "__main__":
    with open("input1_1.txt","r") as f:
        num_list = f.readlines()

    num_list = [int(i.strip("\n")) for i in num_list]
    ans = find_numbers_of_sum(num_list,2020)
    print(ans)