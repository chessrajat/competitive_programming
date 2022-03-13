# 1 -> 1
# 2 -> 1 + 1 -> 3
# 3 -> 1 + 1 + 1 -> 4
# 4 -> 2 + 2 -> 1 + 1 + 1 + 1 -> 7 
# 5 -> 6
# 6 -> 2+2+2 -> 1 + 1 + 1 + 1 + 1 + 1 -> 10
# 8 -> 4 + 4 -> 2+2+2+2 -> 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
# 12 -> 6 + 6 -> 2+2+2
moves = 0
def find_moves(balls):
    global moves
    for i in range(balls-1,0, -1):
        if balls % i == 0 and i%2 == 0:
            moves += find_moves(i)
    if balls == 1:
        return 1
    if balls % 2 != 0:
        return balls + 1
    
    return moves



if __name__=="__main__":

    bags = input()
    balls = list(map(int, input().split()))

    print(balls)
    all_moves = 0
    for b in balls:
        res = find_moves(b)
        all_moves += res

    print(all_moves)