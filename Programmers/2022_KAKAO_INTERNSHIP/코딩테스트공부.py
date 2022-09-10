def solution(alp, cop, problems):
    n = len(problems)
    visited = [0 for _ in range(n)]
    max_alp, max_cop = 0, 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    
    dp = [[0 for _ in range(max_alp+1)] for _ in range(max_cop+1)]
    for i in range(1, max_alp):
        for j in range(1, max_cop):
            dp[i][j] = max
    return answer

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))