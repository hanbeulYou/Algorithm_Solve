import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
maze = []
queue = deque()

for i in range(r) :
    maze.append(list(sys.stdin.readline()))
    if 'F' in maze[i] :
        queue.appendleft(('F', i, maze[i].index('F'), 1))
    if 'J' in maze[i] :
        queue.append(('J', i, maze[i].index('J'), 1))

dir_i = [0, 0, 1, -1]
dir_j = [1, -1, 0, 0]

while queue :
    who, i, j, time = queue.popleft()
    if who == 'F' :
        for k in range(4) :
            new_i = i + dir_i[k]
            new_j = j + dir_j[k]
            if 0 <= new_i < r and 0 <= new_j < r :
                if maze[new_i][new_j] != '#' and maze[new_i][new_j] != 'F' :
                    maze[new_i][new_j] = 'F'
                    queue.append(('F', new_i, new_j, time+1))
    else :
        for k in range(4) :
            new_i = i + dir_i[k]
            new_j = j + dir_j[k]
            if 0 <= new_i < r and 0 <= new_j < r :
                if maze[new_i][new_j] != '#' and maze[new_i][new_j] != 'F' :
                    maze[new_i][new_j] = time + 1
                    queue.append(('J', new_i, new_j, time+1))
                    if (new_i == 0 or new_i == r - 1) or (new_j == 0 or new_j == c - 1) :
                        print(time + 1)
                        quit()

print('IMPOSSIBLE')