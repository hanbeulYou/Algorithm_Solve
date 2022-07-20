
k = int(input())
edges = [[0 for i in range(2)] for j in range(6)]
check = [0 for i in range(5)]
check_edge = []

for i in range(6) :
    edges[i] = list(map(int, input().split()))
    check[edges[i][0]] += 1
    if check[edges[i][0]] == 2 :
        check_edge.append(edges[i][0])

for i in range(6) :
    if edges[0][0] == edges[2][0] and edges[1][0] == edges[3][0] :
        break
    else :
        edges.append(edges[0])
        del edges[0]

print(edges)
print(k * (edges[4][1] * edges[5][1] - edges[2][1] * edges[1][1]))

"""
    if edges[i][0] == check_edge[0] :
        if edges[i + 2][0] == check_edge[0] :
            d
"""

"""
k = int(input())
edges = [[0 for i in range(2)] for j in range(5)]
check = []

for i in range(6) :
    dir, edge = map(int,input().split())
    if edges[dir][0] == 0 :
        edges[dir][0] = edge
    else :
        edges[dir][1] = edge
        check.append(dir)

area = 0
if check[0] == 1 and check[1] == 3 :
    area = edges[2][0] * edges[4][0]
    area -= edges[1][1] * edges[3][0]
elif check[0] == 3 and check[1] == 1 :
    area = edges[2][0] * edges[4][0]
    area -= edges[1][0] * edges[3][1]

elif check[0] == 1 and check[1] == 4 :
    area = edges[2][0] * edges[3][0]
    area -= edges[1][1] * edges[4][0]
elif check[0] == 4 and check[1] == 1 :
    area = edges[2][0] * edges[3][0]
    area -= edges[1][0] * edges[4][1]

elif check [0] == 2 and check[1] == 3 :
    area = edges[1][0] * edges[4][0]
    area -= edges[2][1] * edges[3][0]
elif check [0] == 3 and check[1] == 2 :
    area = edges[1][0] * edges[4][0]
    area -= edges[2][0] * edges[3][1]

elif check [0] == 2 and check[1] == 4 :
    area = edges[1][0] * edges[3][0]
    area -= edges[2][1] * edges[4][0]
else :
    area = edges[1][0] * edges[3][0]
    area -= edges[2][0] * edges[4][1]

print(area * k)
"""