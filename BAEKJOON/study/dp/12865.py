N, K = map(int, input().split())
packages = [(0, 0)]
for _ in range(N) :
    packages.append(tuple(map(int, input().split())))

packages.sort(key=lambda x:x[0])
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1) :
    for j in range(1, K+1) :
        if j < packages[i][0] :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-packages[i][0]] + packages[i][1])

print(dp[i][j])