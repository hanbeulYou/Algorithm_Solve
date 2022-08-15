import sys

r, c = map(int, sys.stdin.readline().split())
maze = []
maze_fire = [[0 for _ in range(c)] for _ in range(r)]
maze_jihoon = [[0 for _ in range(c)] for _ in range(r)]
queue_fire = []
queue_jihoon = []

for i in range(r) :
    maze.append(list(input()))
    if 'F' in maze[i] :
        queue_fire.append([i, maze[i].index('F'), 1])
    if 'J' in maze[i] :
        queue_jihoon.append([i, maze[i].index('J'), 1])

dir_i = [0, 0, 1, -1]
dir_j = [1, -1, 0, 0]

while queue_fire :
    n = queue_fire.pop()
    maze_fire[n[0]][n[1]] = n[2]

    for k in range(4) :
        next_i = n[0] + dir_i[k]
        next_j = n[1] + dir_j[k]
        if 0 <= next_i < r and 0 <= next_j < c :
            if maze[next_i][next_j] != '#':
                if maze_fire[next_i][next_j] == 0 or maze_fire[next_i][next_j] > n[2] + 1 :
                   queue_fire.insert(0, [next_i, next_j, n[2] + 1])

while queue_jihoon :
    n = queue_jihoon.pop()
    maze_jihoon[n[0]][n[1]] = n[2]

    for k in range(4) :
        next_i = n[0] + dir_i[k]
        next_j = n[1] + dir_j[k]
        if 0 <= next_i < r and 0 <= next_j < c :
            if maze[next_i][next_j] != '#':
                if maze_fire[next_i][next_j] < n[2] + 1 :
                    continue
                if maze_jihoon[next_i][next_j] == 0 or maze_jihoon[next_i][next_j] > n[2] + 1 :
                   queue_jihoon.insert(0, [next_i, next_j, n[2] + 1])

escape = 1000
for i in range(r) :
    if maze_jihoon[i][0] != 0 and maze_jihoon[i][0] - maze_fire[i][0] < 0 :
        if escape > maze_jihoon[i][0] : escape = maze_jihoon[i][0]
    if maze_jihoon[i][c-1] != 0 and maze_jihoon[i][c-1] - maze_fire[i][c-1] < 0 :
        if escape > maze_jihoon[i][0] : escape = maze_jihoon[i][c-1]
        
for j in range(c) :
    if maze_jihoon[0][j] != 0 and maze_jihoon[0][j] - maze_fire[0][j] < 0 :
        if escape > maze_jihoon[0][j] : escape = maze_jihoon[0][j]
    if maze_jihoon[r-1][j] != 0 and maze_jihoon[r-1][j] - maze_fire[r-1][j] < 0 :
        if escape > maze_jihoon[r-1][j] : escape = maze_jihoon[r-1][j]
        
print(escape)