import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = list()
table = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K):
    r, c = map(int, input().split())
    table[r][c] = 1
    
snake = deque()
snake.append((1,1))
L = int(input())
# 현재 시간 및 방향
now, d = 0, 0
d_i = [0, 1, 0, -1]
d_j = [1, 0, -1, 0]

for _ in range(L):
    time, change = input().split()
    time = int(time)
    while now < time:
        now += 1
        n_i = snake[-1][0] + d_i[d]
        n_j = snake[-1][1] + d_j[d]
        if n_i == 0 or n_i == N+1 or n_j == 0 or n_j == N+1:
            print(now)
            exit()
        if (n_i, n_j) in snake:
            print(now)
            exit()
        if table[n_i][n_j] == 1:
            table[n_i][n_j] = 0
            snake.append((n_i, n_j))
        else:
            snake.append((n_i, n_j))
            snake.popleft()

    if change == 'D':
        d += 1
        d %= 4
    else:
        d -= 1
        d %= 4
        
while True:
    now += 1
    n_i = snake[-1][0] + d_i[d]
    n_j = snake[-1][1] + d_j[d]
    if n_i == 0 or n_i == N+1 or n_j == 0 or n_j == N+1:
        print(now)
        exit()
    if (n_i, n_j) in snake:
        print(now)
        exit()
    if table[n_i][n_j] == 1:
        table[n_i][n_j] = 0
        snake.append((n_i, n_j))
    else:
        snake.append((n_i, n_j))
        snake.popleft()