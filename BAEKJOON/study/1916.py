import sys
import heapq
input = sys.stdin.readline

INF = 1<<31
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
S, E = map(int, input().split())

def dijkstra():
    distance[S] = 0
    queue = [(0, S)]
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for next in graph[now]:
            tmp = dist + next[1]
            if tmp < distance[next[0]]:
                distance[next[0]] = tmp
                heapq.heappush(queue, (tmp, next[0]))

dijkstra()
print(distance[E])