def solution(cap, n, deliveries, pickups):
    sum_d = sum(deliveries)
    sum_p = sum(pickups)

    answer = 0
    to_idx = n-1
    while sum_d or sum_p:
        can_stack = cap
        stack = 0

        if deliveries[to_idx] or pickups[to_idx]:
            answer += (to_idx+1)*2
        
            for idx in range(to_idx, -1, -1):
                if deliveries[idx]:
                    if stack + deliveries[idx] > can_stack:
                        deliveries[idx] -= can_stack
                        stack += can_stack
                        sum_d -= can_stack
                        to_idx = idx
                        break
                    else:
                        stack += deliveries[idx]
                        sum_d -= deliveries[idx]
                        deliveries[idx] = 0
                if pickups[idx]:
                    sum_p -= pickups[idx]
                    if pickups[idx] > can_stack:
                        pickups[idx] = pickups - can_stack
                        sum_p += pickups - can_stack
                        to_idx = idx
                        break
                    else:
                        can_stack -= pickups[idx]
                        pickups[idx] = 0
        
        else:
            to_idx -= 1

    return answer

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))