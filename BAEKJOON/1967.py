import sys
sys.setrecursionlimit(1000000)

def make_table(start, now, weight) :
#    global table
    for idx, next_w in enumerate(table[now]) :
        if next_w != 0 and table[start][idx] == 0:
            table[start][idx] = weight + next_w
            make_table(start, idx, weight + next_w)
    
n = int(input())
table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
tmp = []

for i in range(n-1) :
    parent, child, weight = map(int, sys.stdin.readline().split())
    table[parent][parent] = -1
    table[child][child] = -1
    table[parent][child] = weight
    table[child][parent] = weight
    if parent == 1 :
        tmp.append((child, weight))
    

for child, weight in enumerate(table[1]) :
    if weight :
        make_table(1, child, weight)

max_node = max(table[1])
max_idx = table[1].index(max_node)

for i in range(n + 1) :
    table[1][i] = 0

table[1][1] = -1
for t in tmp :
    table[1][t[0]] = t[1]

for child, weight in enumerate(table[max_idx]) :
    if weight :
        make_table(max_idx, child, weight)

max_w = max(table[max_idx])
print(max_w)