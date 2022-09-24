def solution(cap, n, deliveries, pickups):
    sum_d = sum(deliveries)
    sum_p = sum(pickups)

    answer = 0
    to_idx = n-1
    while sum_d or sum_p:
        deliver = cap
        pick = cap
        can_deli, can_pick = True, True
        if to_idx == -1: break
        if deliveries[to_idx] or pickups[to_idx]:
            answer += (to_idx+1)*2
            pick_idx, deli_idx = 0, 0
            
            # 2중 for문 안쓰고 -> idx로 끝에서부터 걍 계속 처리하는 방식으로 바꿔보기
            for idx in range(to_idx, -1, -1):
                if not (can_deli or can_pick):
                    to_idx = max(pick_idx, deli_idx)
                    break
                
                if can_deli and deliveries[idx]:
                    if deliver >= deliveries[idx]:
                        deliver -= deliveries[idx]
                        sum_d -= deliveries[idx]
                        deliveries[idx] = 0
                    else:
                        deliveries[idx] -= deliver
                        sum_d -= deliver
                        can_deli = False
                        deli_idx = idx
                        
                if can_pick and pickups[idx]:
                    if pick >= pickups[idx]:
                        pick -= pickups[idx]
                        sum_p -= pickups[idx]
                        pickups[idx] = 0
                    else:
                        pickups[idx] -= pick
                        sum_p -= pick
                        can_pick = False
                        pick_idx = idx
        else:
            to_idx -= 1

    return answer

#print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
#print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))

input_arr = [50 for _ in range(100000)]
print(solution(1, 100000, input_arr, input_arr))