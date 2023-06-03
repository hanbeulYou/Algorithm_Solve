import sys
input = sys.stdin.readline

def multiplication(matrix1, matrix2):
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            value = 0
            for k in range(N):
                value += matrix1[i][k] * matrix2[k][j]
            result[i][j] = value % 1000

    return result


def divide(now, now_matrix):
    if now == 1:
        return now_matrix
    tmp_matrix = divide(now//2, now_matrix)
    if now % 2:
        return multiplication(multiplication(tmp_matrix, tmp_matrix), matrix)
    return multiplication(tmp_matrix, tmp_matrix)


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = divide(B, matrix)

for i in range(N):
    for j in range(N):
        print(answer[i][j]% 1000, end=' ')
    print() 