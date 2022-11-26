import math

def solution(levels):
    n = len(levels)
    q = math.ceil(n / 4 * 3)
    if n < 4 :
        return -1
    else :
        return sorted(levels)[q]

print(solution([1,2,3,4]))