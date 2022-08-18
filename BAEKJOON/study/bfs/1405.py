n, east, west, south, north = map(int, input().split())
route = [(0,0)]
prob = 0

def move(route, x, y, p, l) :
    global n, east, west, south, north, prob
    if l == n :
        prob += p / (100 ** n)
        return

    if east != 0 and (x+1, y) not in route :
        route.append((x+1, y))
        move(route, x+1, y, p * east, l+1)
        del route[-1]
        
    if west != 0 and (x-1, y) not in route :
        route.append((x-1, y))
        move(route, x-1, y, p * west, l+1)
        del route[-1]
        
    if south != 0 and (x, y-1) not in route :
        route.append((x, y-1))
        move(route, x, y-1, p * south, l+1)
        del route[-1]
        
    if north != 0 and (x, y+1) not in route :
        route.append((x, y+1))
        move(route, x, y+1, p * north, l+1)
        del route[-1]
        
move(route, 0, 0, 1, 0)
print(prob)