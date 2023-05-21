def check(now, n_visited):
    global answer
    global visited
    global check_depth

    if check_depth == 7:
        answer += 1
        return
    
    d_i = [0, 0, 1, -1]
    d_j = [1, -1, 0, 0]

    for k in range(4): 
        n_i = visited[now][0] + d_i[k]
        n_j = visited[now][1] + d_j[k]
        if 0 > n_i or n_i > 4 or 0 > n_j or n_j > 4: continue
        for l in range(7):
            if visited[l] == (n_i, n_j) and n_visited[l] == False:
                n_visited[l] = True
                check_depth += 1
                check(l, n_visited)
                if check_depth == 7:
                    return
    

def dfs(i, j, depth):
    global s, y
    global visited
    global check_depth

    if depth == 7:
        if s >= 4:
            n_visited = [False for _ in range(7)]
            n_visited[0] = True
            check_depth = 1
            check(0, n_visited)
        return
    
    for n_i in range(i, 5):
        for n_j in range(5):
            if n_i == i and n_j <= j: continue
            y += 1 if arr[n_i][n_j] == 'Y' else 0
            s += 1 if arr[n_i][n_j] == 'S' else 0
            if y > 3:
                y -= 1 if arr[n_i][n_j] == 'Y' else 0
                s -= 1 if arr[n_i][n_j] == 'S' else 0
                continue
            visited.append((n_i, n_j))
            dfs(n_i, n_j, depth+1)
            visited.pop()
            y -= 1 if arr[n_i][n_j] == 'Y' else 0
            s -= 1 if arr[n_i][n_j] == 'S' else 0


arr = []
for _ in range(5):
    arr.append(input())
visited = []
check_depth = 0

answer = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'Y':
            s, y = 0, 1
        else:
            s, y = 1, 0
        visited.append((i, j))
        dfs(i, j, 1)
        visited.pop()

print(answer)