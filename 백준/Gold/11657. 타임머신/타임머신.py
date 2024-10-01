import sys

input = sys.stdin.readline

INF = float("inf")

N, M = map(int, input().split())
edges = []

for _ in range(M):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))

dist = [INF for _ in range(N+1)]
dist[1] = 0

for i in range(N):
    for edge in edges:
        (a, b, c) = edge
        if dist[b] > dist[a] + c:
            if i == N - 1:
                print(-1)
                exit() 
            
            dist[b] = dist[a] + c

for i in range(2, N+1):
    print(dist[i] if dist[i] != INF else -1)