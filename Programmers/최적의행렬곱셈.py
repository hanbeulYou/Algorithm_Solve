def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for cnt in range (2, n + 1) : # 계산할 행렬 갯수
        for i in range(0, n) : # 시작 idx
            min_dp = []
            for j in range(1, cnt + 1) :
                if i + j > n :
                    break
                min_dp.append(dp[i][i + j - 1] + dp[i + j][cnt - 1] + matrix_sizes[i + j - 1][0] * matrix_sizes[i + j - 1][1] * matrix_sizes[i + j][1])
            else :
                dp[i][i + cnt - 1] = min(min_dp)
    
    print(dp)



solution([[5,3],[3,10],[10,6]])