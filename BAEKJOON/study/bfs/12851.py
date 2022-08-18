from collections import deque

N, K = map(int, input().split())
loc = [[0 for _ in range(2)] for _ in range(150001)]
move = deque()
move.append((N, 0))
loc[N][0] = -1

while move :
    nxt = move.popleft()
    if loc[K][0] != 0 :
        if nxt[1] == loc[K][0] :
            break

    if nxt[0] + 1 < 150001 :
        if loc[nxt[0]+1][0] == 0 or loc[nxt[0]+1][0] == nxt[1] + 1 :
            loc[nxt[0]+1][0] = nxt[1] + 1
            loc[nxt[0]+1][1] += 1
            move.append((nxt[0]+1, nxt[1]+1))
        elif loc[nxt[0]+1][0] > nxt[1] :
            loc[nxt[0]+1][0] = nxt[1] + 1
            loc[nxt[0]+1][1] = 1
            move.append((nxt[0]+1, nxt[1]+1))

    if nxt[0] - 1 >= 0 :
        if loc[nxt[0]-1][0] == 0 or loc[nxt[0]-1][0] == nxt[1] + 1 :
            loc[nxt[0]-1][0] = nxt[1] + 1
            loc[nxt[0]-1][1] += 1
            move.append((nxt[0]-1, nxt[1]+1))
        elif loc[nxt[0]-1][0] > nxt[1] :
            loc[nxt[0]-1][0] = nxt[1] + 1
            loc[nxt[0]-1][1] = 1
            move.append((nxt[0]-1, nxt[1]+1))

    if nxt[0] * 2 < 150001 :
        if loc[nxt[0]*2][0] == 0 or loc[nxt[0]*2][0] == nxt[1] + 1 :
            loc[nxt[0]*2][0] = nxt[1] + 1
            loc[nxt[0]*2][1] += 1
            move.append((nxt[0]*2, nxt[1]+1))
        elif loc[nxt[0]*2][0] > nxt[1] :
            loc[nxt[0]*2][0] = nxt[1] + 1
            loc[nxt[0]*2][1] = 1
            move.append((nxt[0]*2, nxt[1]+1))

if N == K :
    print(0)
    print(1)
else :
    print(loc[K][0])
    print(loc[K][1])