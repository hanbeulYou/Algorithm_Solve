plane = [[0 for _ in range(100)] for __ in range(100)]

for _ in range(4) :
    left_x, left_y, right_x, right_y = map(int, input().split())
    
    for y in range(left_y, right_y) :
        for x in range(left_x, right_x) :
            plane[y][x] = 1

total_sum = 0
for y in range(100) :
    total_sum += sum(plane[y])
    
print(total_sum)