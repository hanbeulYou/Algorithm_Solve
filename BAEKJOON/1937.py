# 욕심쟁이 판다
import sys
#sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(1000000) # 리커젼 맥시멈 늘려주기

def dfs(i, j) :
    global dp

    if dp[i][j] : # 도달한 위치에 이미 DP 값이 존재할 경우
        return dp[i][j]
    
    dp[i][j] = 1
    for k in range(4) : # 4방향 델타 탐색
        if 0 <= i + mv_y[k] < N and 0 <= j + mv_x[k] < N:
            if forest[i+mv_y[k]][j+mv_x[k]] > forest[i][j] : # 다음 칸으로 넘어갈 수 있는 조건
                dp[i][j] = max(dp[i][j], dfs(i+mv_y[k],j+mv_x[k]) + 1) # 현재까지의 DP와 다음칸 + 1개 비교해서 큰 값을 취하기
                
    return dp[i][j]


N = int(input())
forest = []
dp = []
mv_x = [1, -1, 0, 0]
mv_y = [0, 0, 1, -1]

for _ in range(N) :
    forest.append(list(map(int, sys.stdin.readline().split())))
    dp.append([0] * N)

for i in range(N) :
    for j in range(N) :
        dfs(i, j) 

print(max(map(max,dp)))