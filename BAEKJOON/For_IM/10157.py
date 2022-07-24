def numbering(num, x, y, dir) :
    global sits
    
    sits[y][x] = num
    if num >= 199 :
        pass
    if dir == 'up' :
        if y == R - 1 :
            dir = 'right'
        elif sits[y + 1][x] != 0 :
            dir = 'right'
            
    elif dir == 'right' :
        if x == C - 1 :
            dir = 'down'
        elif sits[y][x + 1] != 0 :
            dir = 'down'
            
    elif dir == 'down' :
        if y == 0 :
            dir = 'left'
        elif sits[y - 1][x] != 0 :
            dir = 'left'
            
    elif dir == 'left' :
        if x == 0 :
            dir = 'up'
        elif sits[y][x - 1] != 0:
            dir = 'up'
            
    return dir

C, R = map(int,input().split())
sit = int(input())
sits = [[0 for _ in range(C)] for __ in range(R)]

x = 0
y = 0
dir = 'up'
if C * R < sit :
    print (0)
else :
    for num in range(1, sit + 1) : 
        dir = numbering(num , x, y, dir)
        if num != sit :
            if dir == 'up' :
                x, y = x, y + 1
            elif dir == 'right' :
                x, y = x + 1, y
            elif dir == 'down' :
                x, y = x, y - 1
            else :
                x, y = x - 1, y
        
    print(x + 1, y + 1)