import sys
input = sys.stdin.readline

def count_broken_egg():
    cnt = 0
    for a in arr:
        if a[0] <= 0:
            cnt += 1
    return cnt


def dfs(depth):
    global answer

    if depth == N:
        answer = max(count_broken_egg(), answer)
        return
    if arr[depth][0] > 0:
        tmp = 0
        for i in range(N):
            if i == depth or arr[i][0] <= 0:
                tmp += 1
                continue
            else:
                arr[i][0] -= arr[depth][1]
                arr[depth][0] -= arr[i][1]
                dfs(depth+1)
                arr[i][0] += arr[depth][1]
                arr[depth][0] += arr[i][1]
        if tmp == depth+1:
            dfs(depth+1)
    else:
        dfs(depth+1)


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
answer = float('-INF')
dfs(0)
print(answer)