k = int(input())
edges = [[0 for i in range(2)] for j in range(6)]

for i in range(6) :
    edges[i] = list(map(int, input().split()))

for i in range(6) :
    if edges[0][0] == edges[2][0] and edges[1][0] == edges[3][0] :
        break
    else :
        edges.append(edges[0])
        del edges[0]

print(k * (edges[4][1] * edges[5][1] - edges[2][1] * edges[1][1]))