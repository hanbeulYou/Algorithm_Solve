import sys

def dfs(start, now, next, weight) :
    global N
    global far
    global nodes 
    for i in range(N) :
        if nodes[i][0] == next :
            far[start][next] = dfs(start, next, nodes[i][1], nodes[i][2]) + far[now][next]
    else :
        return weight

N = int(input())
nodes = []
far = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N-1) :
    nodes.append(list(map(int, sys.stdin.readline().split())))
    far[nodes[i][0]][nodes[i][1]] = nodes[i][2]

dfs(nodes[0][0], nodes[0][0], nodes[0][1], nodes[0][2])

print(far)