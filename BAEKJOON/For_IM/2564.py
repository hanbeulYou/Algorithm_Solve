x, y = map(int, input().split())
n = int(input())
stores = []
for _ in range(n) :
    stores.append(tuple(map(int, input().split())))
home_dir, home_loc = map(int, input().split())

dist = 0
for store in stores :
    if home_dir == 1 :
        if store[0] == 1 :
            dist += abs(home_loc - store[1])
        elif store[0] == 2 :
            route_a = home_loc + store[1] + y
            route_b = (x - home_loc) + (x - store[1]) + y
            dist += route_a if route_a < route_b else route_b
        elif store[0] == 4 :
            dist += x - home_loc + store[1]
        else :
            dist += home_loc + store[1]
    elif home_dir == 2 :
        if store[0] == 1 :
            route_a = home_loc + store[1] + y
            route_b = (x - home_loc) + (x - store[1]) + y
            dist += route_a if route_a < route_b else route_b
        elif store[0] == 2 :
            dist += abs(home_loc - store[1])
        elif store[0] == 4 :
            dist += (x - home_loc) + (y - store[1])
        else :
            dist += home_loc + (y - store[1])

    elif home_dir == 4 :
        if store[0] == 1 :
            dist += (x - store[1]) + home_loc
        elif store[0] == 2 :
            dist += (x - store[1]) + (y - home_loc)
        elif store[0] == 4 :
            dist += abs(home_loc - store[1])
        else :
            route_a = home_loc + store[1] + x
            route_b = (y - home_loc) + (y - store[1]) + x
            dist += route_a if route_a < route_b else route_b
    
    else :
        if store[0] == 1 :
            dist += home_loc + store[1]
        elif store[0] == 2 :
            dist += (y - home_loc) + store[1]
        elif store[0] == 4 :
            route_a = home_loc + store[1] + x
            route_b = (y - home_loc) + (y - store[1]) + x
            dist += route_a if route_a < route_b else route_b
        else :
            dist += abs(home_loc - store[1])

print(dist)