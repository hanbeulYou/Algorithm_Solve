def dfs(now, depth):
    global comb

    comb.append(arr[now])
    if depth == M:
        print(*comb)
        comb.pop()
        return
    
    for i in range(N):
        if arr[i] not in comb:
            dfs(i, depth+1)

    comb.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
comb = []
for i in range(N):
    dfs(i, 1)