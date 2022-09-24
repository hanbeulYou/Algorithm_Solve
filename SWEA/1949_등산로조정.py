def dfs(route, idx, can_cut):
    global answer

    answer = max(answer, idx+1)
    visited[route[idx][0]][route[idx][1]] = True
    
    for k in range(4):
        next_i = route[idx][0] + d[k][0]
        next_j = route[idx][1] + d[k][1]
        if 0 <= next_i < N and 0 <= next_j < N:
            # 그냥 갈 수 있을 때
            if table[next_i][next_j] < route[idx][2] \
                and not visited[next_i][next_j]:
                route.append((next_i, next_j, table[next_i][next_j]))
                dfs(route, idx+1, can_cut)
                route.pop()
            # 깎아서 갈 수 있을 때
            elif table[next_i][next_j] - K < route[idx][2] \
                and not visited[next_i][next_j] and can_cut:
                route.append((next_i, next_j, route[idx][2]-1))
                dfs(route, idx+1, False)
                route.pop()
    
    visited[route[idx][0]][route[idx][1]] = False


T = int(input())
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    table = []
    max_mount = 0
    start_mount = []
    for _ in range(N):
        table.append(list(map(int, input().split())))

    # 시작 봉우리 높이 및 위치 탐색
    max_mount = max(map(max, table))
    for i in range(N):
        for j in range(N):
            if table[i][j] == max_mount:
                start_mount.append((i, j))

    # dfs 알고리즘 활용
    visited = [[False for _ in range(N)] for _ in range(N)]
    answer = 0
    for start in start_mount:
        route = [(start[0], start[1], max_mount)]
        dfs(route, 0, True)

    print('#{} {}'.format(tc, answer))