def star(size):
    if size == 3:
        return ['***', '* *', '***']
    
    arr = star(size//3)
    stars = list()
    
    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(size//3)+i)
    for i in arr:
        stars.append(i*3)
        
    return stars


N = int(input())
print('\n'.join(star(N)))