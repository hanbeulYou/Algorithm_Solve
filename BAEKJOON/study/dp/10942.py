import sys
input = sys.stdin.readline

N = int(input())
nums = tuple(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]
M = int(input())

# 길이가 1, 2인 palindrome 체크
for i in range(N) :
    dp[i][i] = 1
    if i < N -1 :
        if nums[i] == nums[i+1] :
            dp[i][i+1] = 1

# 길이가 3 이상인 palindrome 체크
for length in range(2, N) :
    for start in range(N - length) :
        end = start + length
        if nums[start] == nums[end] and dp[start+1][end-1] :
            dp[start][end] = 1

for _ in range(M) :
    S, E = map(int, input().split())
    print(dp[S-1][E-1])