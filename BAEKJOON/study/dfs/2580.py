import sys
input = sys.stdin.readline

def check_row(i, v):
    for k in range(9):
        if table[i][k] == v:
            return False
    return True


def check_col(j, v):
    for k in range(9):
        if table[k][j] == v:
            return False
    return True


def check_sqr(i, j, v):
    n_i = i - i%3
    n_j = j - j%3
    for k_i in range(3):
        for k_j in range(3):
            if table[n_i+k_i][n_j+k_j] == v:
                return False
    return True


def dfs(idx):
    global table

    if idx == len(to_put):
        for i in range(9):
            print(*table[i])
        quit()

    i, j = to_put[idx][0], to_put[idx][1]
    for num in range(1, 10):
        if check_col(j, num) and check_row(i, num) and check_sqr(i, j, num):
            table[i][j] = num
            dfs(idx+1)
            table[i][j] = 0

table = []
to_put = []

for i in range(9):
    table.append(list(map(int, input().split())))
    for j in range(9):
        if table[i][j] == 0:
            to_put.append((i, j))

dfs(0)

