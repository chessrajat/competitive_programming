'''
/*
 * @Author: Rajat  
 * @Date: 2020-12-12 11:31:16 
 * @Last Modified by: Rajat
 * @Last Modified time: 2020-12-12 11:40:14
 */
'''

# --- Day 3: Toboggan Trajectory ---

def trajectory_treversing(tree_map, forward, down):
    current_row = 0
    tree_map_length = len(tree_map)
    for row in tree_map:
        





if __name__ == '__main__':
    with open("./Advent_Of_Code_2020/day3/day3.txt","r") as f:
        tree_map = f.readlines()
    
    tree_map = [i.strip("\n") for i in tree_map]

    result = trajectory_treversing(tree_map, 3, 1)