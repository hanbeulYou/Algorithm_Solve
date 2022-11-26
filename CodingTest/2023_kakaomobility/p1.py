def solution(flowers):
    blossom = [0 for _ in range(366)]
    for flower in flowers:
        for i in range(flower[0], flower[1]):
            blossom[i] += 1
    answer = sum(1 for b in blossom if b > 0)
    return answer

print(solution([[2, 5], [3, 7], [10, 11]]))
print(solution([[3, 4], [4, 5], [6, 7], [8, 10]]))