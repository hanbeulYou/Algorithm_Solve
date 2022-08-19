#2300_기지국 풀이
#2022-08-18

N = int(input())
dp = []
stations = []
for i in range(N) :
    stations.append(list(map(int, input().split())))
    stations[i][1] = abs(stations[i][1])

stations.sort(key=lambda x:(x[0], x[1]))

stations.insert(0, [0, 0])
dp.append(0)

for i in range(1, N + 1) :
    height = stations[i][1]
    dp.append(1000000)
    # 0~j까지의 최적합 + j+1~i까지 포함하는 사각형 -> j를 모두 돌려 그중에 최적합을 찾음
    for j in range(i-1, -1, -1) :
        height = max(height, stations[j+1][1])
        dp[i] = min((dp[j] + max(stations[i][0] - stations[j+1][0], height * 2)), dp[i])

<<<<<<< HEAD
print(dp[N-1])
=======
print(dp[N])
>>>>>>> 973972b8cc8ac72d48c7afbf01702d7b854c891f
