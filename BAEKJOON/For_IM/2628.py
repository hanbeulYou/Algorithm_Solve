x, y = map(int,input().split())
n = int(input())

x_cuts = [0]
y_cuts = [0]

if x > 0 :
    y_cuts.append(x)
if y > 0 :
    x_cuts.append(y)

for _ in range(n) :
    xy_type, xy = map(int,input().split())
    if xy_type == 0 :
        x_cuts.append(xy)
    else :
        y_cuts.append(xy)

x_cuts.sort()
y_cuts.sort()

max_x = max_y = 0
for idx in range(len(y_cuts) - 1) :
    if max_x < y_cuts[idx + 1] - y_cuts[idx] : 
        max_x = y_cuts[idx + 1] - y_cuts[idx]

for idx in range(len(x_cuts) - 1) :
    if max_y < x_cuts[idx + 1] - x_cuts[idx] : 
        max_y = x_cuts[idx + 1] - x_cuts[idx]

print(max_x * max_y)