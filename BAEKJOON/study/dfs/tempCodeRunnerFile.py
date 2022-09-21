def dfs(now, depth):
    global comb
    global answer

    comb.append(arr[now])
    if depth == M:
        if tuple(comb) not in answer:
            answer.append(tuple(comb))
        comb.pop()
        return
    
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        dfs(i, depth+1)
        visited[i] = False

    comb.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
comb = []
answer = []
visited = [False for _ in range(N)]
for i in range(N):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False
for a in answer:
    print(*a)