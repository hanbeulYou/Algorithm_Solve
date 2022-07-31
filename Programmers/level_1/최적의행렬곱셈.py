"""
def solution(matrix_sizes):
    matrix = []
    for size in matrix_sizes :
        matrix += size
    
    sum_size = 0
    while len(matrix) > 2 :
        max_size = max_idx = 0
        for idx, size in enumerate(matrix) :
            if idx == 0 or idx == len(matrix) - 1 :
                continue
            if max_size < size :
                max_size = size
                max_idx = idx
        sum_size += matrix[max_idx - 1] * matrix[max_idx] * matrix[max_idx + 2]
        del matrix[max_idx + 1]
        del matrix[max_idx]
    
    return sum_size
"""

def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for cnt in range (2, n + 1) : # 행렬의 갯수
        for i in range(0, n) : # 시작 idx
            for j in range(cnt) : 


print(solution([[5,3],[3,10],[10,6]]))