def solution(n, s, a, b, fares):
    inf = 1<<31
    f_w = [[inf for _ in range(n+1)] for _ in range(n+1)]
    for i, j, fee in fares:
        f_w[i][j] = f_w[j][i] = fee

    for i in range(1, n+1):
        f_w[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                tmp = min(f_w[i][j], f_w[i][k]+f_w[k][j])
                f_w[i][j] = f_w[j][i] = tmp
    
    answer = inf
    for k in range(1, n+1):
        answer = min(answer, f_w[s][k] + f_w[k][a] + f_w[k][b])

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))