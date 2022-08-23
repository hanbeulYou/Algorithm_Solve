def solution(beginning, target):
    N = len(beginning)
    sum_change = 0
    for i in range(N):
        for j in range(N):
            sum_change += beginning[i][j]^target[i][j]
    
    if sum_change % 2 != N % 2:
        return -1
    return N

print(solution([[0, 0, 0],[0, 0, 0],[0, 0, 0]], [[1, 0, 1],[0, 0, 0],[0, 0, 0]]))