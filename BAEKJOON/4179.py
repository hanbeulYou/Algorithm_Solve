import sys
sys.setrecursionlimit(1000000)

def bfs_fire(i, j, time) :
    global maze_fire
    global r, c
    if i < r - 1 :
        if maze_fire[i+1][j] != -1 and (maze_fire[i+1][j] > time + 1 or maze_fire[i+1][j] == 0):
            maze_fire[i+1][j] = time + 1 
            bfs_fire(i+1, j, time+1)
            
    if i > 0 :
        if maze_fire[i-1][j] != -1 and (maze_fire[i-1][j] > time + 1 or maze_fire[i-1][j] == 0) :
            maze_fire[i-1][j] = time + 1 
            bfs_fire(i-1, j, time+1)
            
    if j < c - 1 :
        if maze_fire[i][j+1] != -1 and (maze_fire[i][j+1] > time + 1 or maze_fire[i][j+1] == 0) :
            maze_fire[i][j+1] = time + 1
            bfs_fire(i, j+1, time+1)
            
    if j > 0 :
        if maze_fire[i][j-1] != -1 and (maze_fire[i][j-1] > time + 1 or maze_fire[i][j-1] == 0) :
            maze_fire[i][j-1] = time + 1 
            bfs_fire(i, j-1, time+1)

def bfs_jihoon(i, j, time) :
    global maze_jihoon
    global r, c
    if i < r - 1 :
        if maze_jihoon[i+1][j] != -1 and (maze_jihoon[i+1][j] > time + 1 or maze_jihoon[i+1][j] == 0):
            maze_jihoon[i+1][j] = time + 1 
            bfs_jihoon(i+1, j, time+1)
            
    if i > 0 :
        if maze_jihoon[i-1][j] != -1 and (maze_jihoon[i-1][j] > time + 1 or maze_jihoon[i-1][j] == 0) :
            maze_jihoon[i-1][j] = time + 1 
            bfs_jihoon(i-1, j, time+1)
            
    if j < c - 1 :
        if maze_jihoon[i][j+1] != -1 and (maze_jihoon[i][j+1] > time + 1 or maze_jihoon[i][j+1] == 0) :
            maze_jihoon[i][j+1] = time + 1
            bfs_jihoon(i, j+1, time+1)
            
    if j > 0 :
        if maze_jihoon[i][j-1] != -1 and (maze_jihoon[i][j-1] > time + 1 or maze_jihoon[i][j-1] == 0) :
            maze_jihoon[i][j-1] = time + 1 
            bfs_jihoon(i, j-1, time+1)
                        

r, c = map(int, input().split())
maze = []
maze_fire = []
maze_jihoon = []
fire = ()
jihoon = ()
for i in range(r) :
    maze.append(list(input()))
    maze_fire.append([])
    maze_jihoon.append([])

    for j, m in enumerate(maze[i]) :
        if m == 'J' :
            maze_fire[i].append(0)
            maze_jihoon[i].append(1)
            jihoon = (i, j)
        elif m == 'F' :
            maze_fire[i].append(1)
            maze_jihoon[i].append(0)
            fire = (i, j)
        elif m == '#' :
            maze_fire[i].append(-1)
            maze_jihoon[i].append(-1)
        else :
            maze_fire[i].append(0)
            maze_jihoon[i].append(0)

bfs_fire(fire[0], fire[1], 1)
bfs_jihoon(jihoon[0], jihoon[1], 1)

escape = 1000
for i in range(r) :
    if maze_jihoon[i][0] != -1 and maze_jihoon[i][0] - maze_fire[i][0] < 0 :
        if escape > maze_jihoon[i][0] : escape = maze_jihoon[i][0]
    if maze_jihoon[i][c-1] != -1 and maze_jihoon[i][c-1] - maze_fire[i][c-1] < 0 :
        if escape > maze_jihoon[i][0] : escape = maze_jihoon[i][c-1]
        
for j in range(c) :
    if maze_jihoon[0][j] != -1 and maze_jihoon[0][j] - maze_fire[0][j] < 0 :
        if escape > maze_jihoon[0][j] : escape = maze_jihoon[0][j]
    if maze_jihoon[r-1][j] != -1 and maze_jihoon[r-1][j] - maze_fire[r-1][j] < 0 :
        if escape > maze_jihoon[r-1][j] : escape = maze_jihoon[r-1][j]

for i in range(r) : 
    for j in range(c) : 
        print(maze_jihoon[i][j], end='')
    print(end='  ')
    for j in range(c) : 
        print(maze_fire[i][j], end='')
    print()
print(escape)