def solution(orders):
    last_box = 1
    cnt = 1
    stack = []
    new_orders = [0 for _ in range(len(orders))]

    for order in orders:
        new_orders[order-1] = cnt
        cnt+=1

    cnt = 0
    for order in new_orders:
        if order == last_box:
            last_box += 1
            cnt += 1
        else:
            while stack:
                top = stack.pop()
                if top == last_box:
                    last_box += 1
                    cnt += 1
                else:
                    stack.append(top)
                    break
            stack.append(order)
    if stack:
        while stack:
            top = stack.pop()
            if top == last_box:
                last_box += 1
                cnt += 1
            else:
                stack.append(top)
                break
        stack.append(order)
    return cnt

print(solution([4, 3, 1, 2, 5]))