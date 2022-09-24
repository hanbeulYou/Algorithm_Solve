from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = set()
for case in permutations(arr, M):
    if case not in answer:
        answer.add(case)
        for c in case:
            print(c, end=' ')
        print()