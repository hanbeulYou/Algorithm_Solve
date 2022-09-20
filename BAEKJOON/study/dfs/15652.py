def dfs(now, depth):
    global arr

    arr.append(now)
    if depth == M:
        print(*arr)
        arr.pop()
        return
    
    for i in range(now, N+1):
        dfs(i, depth+1)

    arr.pop()

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    dfs(i, 1)