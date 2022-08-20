N = int(input())
arr = list(map(int, input().split()))
dp = []
without_dp = []

# 한 번도 제외시키지 않고 만들 수 있는 최적의 해
dp.append(arr[0])
# 한 번 제외시키고 만들 수 있는 최적의 해
without_dp.append(dp[0])
    
for idx in range(1, N) :
    # 현재 값을 포함해 제외 없이 만들 수 있는 최선의 해 
    # 한번도 제외 안한 애들의 최선의 해 + 현재 값 vs 현재 값
    dp.append(max(dp[idx-1] + arr[idx], arr[idx]))
    
    # 현재 값을 포함해 한 번의 제외로 만들 수 있는 최선의 해 
    # 한 번도 제외 안했을 때 현재 값 제외 vs 앞의 것들에서 한 번이라도 제외했을 때 최선의 해 + 현재 값
    without_dp.append(max(dp[idx-1], without_dp[idx-1]+arr[idx]))
    
print(max(map(max, dp, without_dp)))