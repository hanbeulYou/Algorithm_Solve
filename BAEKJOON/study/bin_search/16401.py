import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

s = 1
e = max(snacks)

while s <= e:
    cnt = 0
    m = (s+e)//2
    if m == 0:
        print(0)
        exit()

    for snack in snacks:
        cnt += snack // m

    if cnt >= M:
        s = m + 1
    else:
        e = m - 1
        
print(e)