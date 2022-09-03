import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(now):
    global far
    global max_far
    max_far = max(max_far, far)
    
    for room in rooms[now]:
        if visited[room[0]] == False:
            visited[room[0]] = True
            far += room[1]
            dfs(room[0])
            far -= room[1]


N = int(input())
rooms = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
far, max_far = 0, 0
visited[1] = True
for _ in range(N-1):
    A, B, C = map(int, input().split())
    rooms[A].append((B,C))
    rooms[B].append((A,C))
    
dfs(1)
print(max_far)