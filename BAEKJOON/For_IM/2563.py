n = int(input())
paper = [[0 for _ in range(100)] for __ in range(100)]

for _ in range(n) :
    y, x = map(int, input().split())
    for i in range(10) :
        for j in range(10) :
            if x + j == 100 or y + i == 100 :
                continue
            paper[y + i][x + j] = 1

cnt = 0
for i in range(100) :
    for j in range(100) :
        if paper[i][j] == 1 :
            cnt += 1

print(cnt)