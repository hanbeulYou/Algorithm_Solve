N = int(input())
arr = list(map(int, input().split()))
dp = []
without_dp = []

if arr[0] < 0 :
    dp.append(0)
else :
    dp.append(arr[0])
without_dp.append(dp[0])
    
for idx in range(1, N) :
    # 새로운 값이 더해지는게 최선이 아닐 경우
    if arr[idx] + dp[idx-1] < dp[idx-1] :
        dp.append(max(0, arr[idx] + dp[idx-1]))
        # 새로운 값을 제외했을 때 최선의 값
        without_dp.append(max(without_dp[idx-1], dp[idx-1]))
        
    else :
        dp.append(dp[idx-1] + arr[idx])
        without_dp.append(dp[idx-1] + arr[idx])

print(dp)
print(without_dp)