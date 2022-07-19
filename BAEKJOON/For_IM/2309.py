dwarfs = [0 for i in range(9)]

for i in range(9) :
    dwarfs[i] = int(input())

over = sum(dwarfs) - 100

flag = False
for i in range(9) :
    if dwarfs[i] >= over :
        continue
    else :
        for j in range(i + 1, 9) :
            if (dwarfs[i] + dwarfs[j]) == over :
                del dwarfs[j]
                del dwarfs[i]
                flag = True
                break
        if flag :
            break

for dwarf in sorted(dwarfs) :
    print(dwarf)