N = int(input())
arr = list(map(int, input().split()))
dp = [0]
idx = 1
while idx < N:
    max_idx = -1
    for i in range(idx):
        if arr[i] < arr[idx]:
            max_idx = max(max_idx, dp[i])
    dp.append(max_idx+1)
    idx += 1

result = []
cnt = max(dp)
idx -= 1
while idx >= 0:
    if dp[idx] == cnt:
        result.append(arr[idx])
        cnt -= 1
    idx -= 1
# print(dp)
print(max(dp)+1)
result = result[::-1]
print(*result)