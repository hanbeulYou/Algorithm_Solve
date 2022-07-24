n = int(input())
table = [[0 for _ in range(1001)] for __ in range(1001)]
for num in range(1, n + 1) :
    x, y, width, height = map(int, input().split())
    
    for h in range(height) :
        for w in range(width) :
            table[y + h][x + w] = num

cnt_list = [0 for _ in range(n)]

for i in range(1001) :
    for j in range(1001) :
        if table[i][j] != 0 :
            cnt_list[table[i][j] - 1] += 1
            
for i in range(n) :
    print (cnt_list[i])