




def filledOrders(order, k):
    # Write your code here
    total = 0
    order.sort()
    for i in range(len(order)):
        if total + order[i] <=k:
            total += order[i]
        else:
            return i
    return len(order)

    
    


if __name__ == '__main__':
    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    k = int(input().strip())

    result = filledOrders(order, k)
    print(result)
   