N = int(input())
sol = sorted(list(map(int, input().split())))
s_idx = 0
e_idx = len(sol) - 1
min_sol = abs(sol[s_idx] + sol[e_idx])
min_idx = [s_idx, e_idx]

while s_idx != e_idx :
    if abs(sol[s_idx] + sol[e_idx]) < min_sol :
        min_sol = abs(sol[s_idx] + sol[e_idx])
        min_idx = [s_idx, e_idx]
    else :
        if abs(sol[s_idx] + sol[e_idx]) > abs(sol[s_idx + 1] + sol[e_idx]) :
            s_idx += 1
        else :
            e_idx -= 1
    
print(sol[min_idx[0]], sol[min_idx[1]])