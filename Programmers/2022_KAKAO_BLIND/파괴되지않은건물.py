def solution(board, skills):
    n = len(board)
    m = len(board[0])
    answer = 0

    for skill in skills:
        for i in range(skill[1], skill[3]+1):
            for j in range(skill[2], skill[4]+1):
                board[i][j] += (skill[0] * 2 - 3) * skill[5]
                
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                answer += 1
    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))