def solution(stones, k):
    n = len(stones)
    s = min(stones)
    e = max(stones)

    while s <= e:
        m = (s+e)//2
        zero_stone = 0
        cnt = 0
        idx = 0
        while idx < n - k:
            if stones[idx] <= m:
                cnt += 1
                zero_stone = max(zero_stone, cnt)
            else:
                cnt = 0
            idx += 1
            
        if zero_stone > k:
            e = m - 1
        else:
            s = m + 1

    return m - 1

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))