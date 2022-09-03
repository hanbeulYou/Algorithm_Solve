N = int(input())
arr = list(map(int, input().split()))
new_arr = [-1000000001]
dp = [0]
max_dp = 0
for item in arr:
    # 더 큰 값이 있으면 추가
    if new_arr[-1] < item:
        new_arr.append(item)
        max_dp += 1
        dp.append(max_dp)
    else:
        s, e = 0, len(new_arr)
        # 이분탐색으로 시간 줄이기
        while s < e:
            m = (s+e)//2
            if new_arr[m] < item:
                s = m + 1
            else:
                e = m
        new_arr[e] = item
        dp.append(e)

print(len(new_arr)-1)
result = []
cnt = max(dp)
idx = N
while idx >= 1:
    if dp[idx] == cnt:
        result.append(arr[idx-1])
        cnt -= 1
    idx -= 1
result = result[::-1]
print(*result)