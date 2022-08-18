n, m = map(int, input().split())
space = []

def cnt_safe(i_idx, j_idx) :
    global n, m
    global space
    shark = True
    size = 1
    while shark :
        for i in range(i_idx - size, i_idx + size + 1) :
            for j in range(j_idx - size, j_idx + size + 1) :
                if i < 0 or i >= n or j < 0 or j >= m :
                    continue
                if space[i][j] == 1 :
                    shark = False
                    return size
        size += 1
    return size

for _ in range(n) :
    space.append(list(map(int, input().split())))

max_safe = 0
for i in range(n) :
    for j in range(m) :
        if space[i][j] == 0 :
            safe = cnt_safe(i, j)
            if max_safe < safe :
                max_safe = safe
            
print (max_safe)