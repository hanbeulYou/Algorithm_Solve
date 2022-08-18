import sys
sys.setrecursionlimit(100000)

def make_table(start, now, w) :
    global weight
    weight[now] = w

    for node in nodes :
        if node[0] == now and weight[node[1]] == 0 :
            weight[node[1]] = w + node[2]
            make_table(start, node[1], w + node[2])
        elif node[1] == now and weight[node[0]] == 0 :
            weight[node[0]] = w + node[2]
            make_table(start, node[0], w + node[2])
    
n = int(input())
nodes = []
weight = [0 for _ in range(n + 1)]

for i in range(n-1) :
    nodes.append(list(map(int, sys.stdin.readline().split())))
    
weight[1] = -1
for node in nodes :
    if node[0] == 1 :
        make_table(node[0], node[1], node[2])
    else :
        break

max_idx = weight.index(max(weight))
weight = [0 for _ in range(n + 1)]
weight[max_idx] = -1

for node in nodes :
    if node[0] == max_idx :
        make_table(node[0], node[1], node[2])
    elif node[1] == max_idx :
        make_table(node[1], node[0], node[2])

print(max(weight))

# 파이파이! 파이파이! 파이파이! 파이파이! 파이파이! 파이파이! 파이파이! 