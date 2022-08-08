n, k = map(int, input().split())

if n <= k :
    print(0)
else :
    power = []
    for i in range(25) :
        power.append(2**i)

    water = 0
    while k > 1 and n - water != 0:
        for i in range(24,0,-1) :
            if power[i] > n - water and power[i-1] <= n - water :
                water += power[i-1]
                k -= 1
                break
        else :
            water += power[0]
            k -= 1
            
    for i in range(24,0,-1) :
        if power[i] > n - water and power[i-1] <= n - water :
            water += power[i]
            k -= 1
            break
    else :
        water += power[0]

    print(water - n)