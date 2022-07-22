def slope(x, y) :
    global home_x, home_y
    return ((home_y - y) / (home_x - x))

dist_x, dist_y = map(int, input().split())
n = int(input())
stores = [0 for _ in range(n)]
for idx in range(n + 1) :
    dir, loc = map(int, input().split())
    if dir == 1 :
        stores[idx] = (loc, dist_y)
    elif dir == 2 :
        stores[idx] = (loc, 0)
    elif dir == 3 :
        stores[idx] = (0, loc)
    else :
        stores[idx] = (dist_x, loc)

home_x, home_y = stores[n][0], stores[n][1]
rev_home_x = dist_x - home_x
rev_home_y = dist_y - home_y
home_slope = slope(rev_home_x, rev_home_y)

sum_dist = 0
for idx in range(n) :
    if home_slope >= slope(stores[idx][0], stores[idx][1]) :
        sum_dist += abs(home_x - )