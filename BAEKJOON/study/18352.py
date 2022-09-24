import sys
from collections import deque

input = sys.stdin.readline
INF = 1<<31
N, M, K, X = map(int, input().split())

edges = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]
queue = deque()

for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)

distance[X] = 0
for edge in edges[X]:
    queue.append((X, edge))

while queue:
    s, e = queue.popleft()
    distance[e] = min(distance[s]+1, distance[e])
    for edge in edges[e]:
        if distance[s] + 1 < distance[edge]:
            queue.append((e, edge))
    
flag = False
answer = []
for idx, d in enumerate(distance):
    if d == K:
        answer.append(idx)
        flag = True

if not flag:
    answer.append(-1)

answer.sort()
for a in answer:
    print(a)