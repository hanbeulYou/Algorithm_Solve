def dfs(now, depth):
    global comb

    comb.append(arr[now])
    if depth == M:
        if tuple(comb) not in answer:
            answer.add(tuple(comb))
            print(*comb)
        comb.pop()
        return
    
    for i in range(now+1, N):
        dfs(i, depth+1)

    comb.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
comb = []
answer = set()
for i in range(N):
    dfs(i, 1)