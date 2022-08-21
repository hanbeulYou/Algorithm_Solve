import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    n = int(input())
    stickers = []
    for _ in range(2) :
        stickers.append(list(map(int, input().split())))
    dp = [[0 for _ in range(n+2)] for _ in range(2)]
    
    for j in range(n) :
        for i in range(2) :
            other_i = 1^i
            dp[i][j+2] = max(dp[0][j], dp[1][j], dp[other_i][j+1]) + stickers[i][j]
    
    print(max(map(max, dp[0], dp[1])))