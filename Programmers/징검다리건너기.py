def solution(stones, k):
    s = 1
    e = max(stones)
    m = (s+e)//2
    result = 0

    while s < e:
        cnt = 0
        for stone in stones:
            if stone <= m:
                cnt += 1
                if cnt >= k:
                    e = m
                    m = (s+e)//2
                    break
            else:
                cnt = 0
            
        else:
            result = max(result, m)
            s = m + 1
            m = (s+e)//2

    return result + 1

# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))