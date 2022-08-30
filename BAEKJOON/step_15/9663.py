def check(idx, value):
    for i in range(idx):
        if arr[i] == value:
            return False
        if abs(idx - i) == abs(value - arr[i]):
            return False
    return True


def dfs(idx):
    global cnt
    global arr
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        if check(idx, i):
            arr[idx] = i
            dfs(idx+1)
            arr[idx] = 0        


N = int(input())
arr = [0 for _ in range(N)]
cnt = 0
dfs(0)
print(cnt)