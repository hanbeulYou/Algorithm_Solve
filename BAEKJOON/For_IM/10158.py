map_x, map_y = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

x += t
y += t

if (x // map_x) % 2 == 1 :
    x = map_x - x % map_x
else :
    x = x % map_x
if (y // map_y) % 2 == 1 :
    y = map_y - y % map_y
else :
    y = y % map_y
    
print(x, y)