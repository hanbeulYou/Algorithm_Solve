import heapq

def solution(n, s, a, b, fares):
    edges = [[] for _ in range(n)]
    dijkstra = [100000000 for _ in range(n)]
    dijkstra[s] = 0
    pq = heapq()

    for fare in fares:
        edges[fare[0]].append((fare[1], fare[2]))
        edges[fare[1]].append((fare[0], fare[2]))
    
    for edge in edges[s]:
        heapq.heappush(pq, (edge[1], s, edge[0]))
    
    while pq:
        fee, start, end = heapq.heappop(pq)
        dijkstra[end] = min(dijkstra[start]+fee, dijkstra[end])
        for edge in edges[end]:
            heapq.heappush(pq, (edge[1], end, edge[0]))


    answer = 0
    return answer