import sys

n = int(input())
table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
nodes = []

def make_table() :
    global table
    global n

for i in range(n-1) :
    nodes.append(tuple(map(int, sys.stdin.readline().split())))
    table[nodes[i][0]][nodes[i][1]] = nodes[i][2]
    table[nodes[i][1]][nodes[i][0]] = nodes[i][2]
    
