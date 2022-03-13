




if __name__=="__main__":
    t = int(input())
    for i in range(t):
        pots, a,b =map(int, input().split())
        res = cal_money(pots,a ,b)
        print(res)