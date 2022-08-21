import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
maze = []
fire = deque()
jihoon = deque()

for i in range(r) :
    maze.append(list(sys.stdin.readline()))
    if 'F' in maze[i] :
        fire.append((i, maze[i].index('F')))
    if 'J' in maze[i] :
        jihoon.append((i, maze[i].index('J')))

now_fire, now_jihoon = len(fire), len(jihoon)
now = 1

dir_i = [0, 0, 1, -1]
dir_j = [1, -1, 0, 0]

while True :
    # 불 먼저 움직이고
    for _ in range(now_fire) :
        fire_i, fire_j = fire.popleft()

        for i in range(4) :
            new_i = fire_i + dir_i[i]
            new_j = fire_j + dir_j[i]
            if 0 <= new_i < r and 0 <= new_j < c :
                if maze[new_i][new_j] != 'F' and maze[new_i][new_j] != '#':
                    maze[new_i][new_j] = 'F'
                    fire.append((new_i, new_j))
    now_fire = len(fire)
    
    # 지훈이가 움직일거임
    for _ in range(now_jihoon) :
        jihoon_i, jihoon_j = jihoon.popleft()

        if (jihoon_i == 0 or jihoon_i == r - 1) or (jihoon_j == 0 or jihoon_j == c - 1) :
            print(now)
            quit()

        for i in range(4) :
            new_i = jihoon_i + dir_i[i]
            new_j = jihoon_j + dir_j[i]
            if 0 <= new_i < r and 0 <= new_j < c :
                if maze[new_i][new_j] == '.' :
                    maze[new_i][new_j] = 'J'
                    jihoon.append((new_i, new_j))
                    
    now_jihoon = len(jihoon)
    if now_jihoon == 0 :
        print('IMPOSSIBLE')
        quit()

    now += 1