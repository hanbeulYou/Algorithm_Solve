from collections import defaultdict

N, D = map(int, input().split())
roads = []
dp = [0 for _ in range(D+1)]
end_point = defaultdict(list)
for i in range(N):
    roads.append(tuple(map(int, input().split())))
    end_point[roads[i][1]].append([roads[i][0], roads[i][2]])

for i in range(1, D+1):
    dp[i] = dp[i-1] + 1
    if i in end_point.keys():
        for start in end_point[i]:
            dp[i] = min(dp[i], dp[start[0]] + start[1])

print(dp[D])

