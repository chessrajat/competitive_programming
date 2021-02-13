

def exam(v, v_count):
    my_score = 0
    one = v.count(1)
    zero = v.count(0)
    f_score = one - zero
    for k in range(v_count - 2):
        if my_score>f_score:
            return k
        
        if v[k] == 1:
            my_score += 1
            f_score -= 1
        if v[k] == 0:
            f_score += 1
            my_score -= 1

    return v_count
        



if __name__ == "__main__":
    v_count = int(input().strip())
    v = []
    for _ in range(v_count):
        v_item = int(input().strip())
        v.append(v_item)

    result = exam(v, v_count)
    print(result)